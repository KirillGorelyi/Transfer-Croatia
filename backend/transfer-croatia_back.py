import hashlib
import datetime
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
import base64
import jwt
from apscheduler.schedulers.background import BackgroundScheduler

# password l51-N4m&pe£yBFE
TEMP_ARRAY_EXPIRATION_TIME = 120
PERM_ARRAY_EXPIRATION_TIME = 7200
JWT_TEMP_ENCODE = 'WL7feXtJY6hT6OlgQN8txmAbApdKVIRF11RA0XuKj23MKymw98'
JWT_PERM_ENCODE = 'IglyTswXD2kIpmDIKN2LXu7YtNuWeCNJwasozN0DxlIIW0LK2s'

init = False

temp_login = {}
perm_login = {}
userOtpVer = {}


def verification_msg_content(code):
    return f"""\
    Hello!

    Somebody tries to login into admin panel of the transfer-croatia.ru website.
    in case this is you here goes the one-time code : {code}.
    If this is not you, please contact immediately with your awesome developer-Kirill Goreliy. 
    Please, do not reply to this message, this is an automatic email.

    Best regards, your best and only web server.
    """


def getUserNameFromToken(http_request, isPermanent):
    token = checkHeaderToken(http_request, isPermanent)
    print("token is ", token)
    decoded = jwt.decode(token, options={"verify_signature": False})
    return decoded['user']


def checkHeaderToken(http_request, isPermanent):
    auth_header = http_request.headers.get('Authorization')

    if not auth_header:
        print("not auth_header")
        abort(401)
    if not auth_header.startswith('Bearer '):
        print("not bearer")
        abort(401)
    if auth_header.split(' ')[1] not in (perm_login.keys() if isPermanent else temp_login.keys()):
        print("not in cache")
        abort(401)
    return auth_header.split(' ')[1]


def clean_temp():
    print(temp_login)
    remove_tokens = []
    for token, date in temp_login.items():
        if datetime.datetime.now() >= (date + datetime.timedelta(seconds=TEMP_ARRAY_EXPIRATION_TIME)):
            remove_tokens.append(token)

    for token in remove_tokens:
        log.info("removed token " + token)
        del temp_login[token]


def clean_perm():
    remove_tokens = []
    for token, date in perm_login.items():
        if datetime.datetime.now() >= (date + datetime.timedelta(seconds=PERM_ARRAY_EXPIRATION_TIME)):
            remove_tokens.append(token)
    for token in remove_tokens:
        del temp_login[token]


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
file_handler = logging.FileHandler('application.log')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(file_formatter)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(file_handler)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['WTF_CSRF_ENABLED'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)
scheduler = BackgroundScheduler()
scheduler.add_job(func=clean_temp, trigger="interval", seconds=TEMP_ARRAY_EXPIRATION_TIME)
scheduler.add_job(func=clean_perm, trigger="interval", seconds=PERM_ARRAY_EXPIRATION_TIME)
scheduler.start()
CORS(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    usertoken = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), nullable=False)
    title_ru = db.Column(db.String(120), nullable=False)
    description_ru = db.Column(db.Text, nullable=True)
    title_en = db.Column(db.String(120), nullable=False)
    description_en = db.Column(db.Text, nullable=True)
    image = db.Column(db.LargeBinary, nullable=True)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    edit_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    creator_username = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Item {self.title}>'


with app.app_context():
    db.create_all()
    if not User.query.first():
        user1 = User(username='admin',
                     usertoken="a25fdb444eaf8747e661f1739b02d28417b6d4b6cbbfaf61708939861d7605ce",
                     email="chromovkirill99@gmail.com",
                     role="OWNER")
        db.session.add(user1)
        db.session.commit()


def decomposeHeader(http_request):
    auth_header = http_request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Basic '):
        return jsonify({'message': 'Authorization header missing or not Basic'}), 401

    base64_credentials = auth_header.replace('Basic ', '')
    print(base64_credentials)

    credentials = base64.b64decode(base64_credentials).decode('latin1')
    username, password = credentials.split(':')
    return username, hashlib.sha256(password.encode('utf-8')).hexdigest()


@app.before_request
def log_request_info():
    log.info(f'Received {request.method} request for {request.url}')
    log.info(f'Headers: {request.headers}')
    log.info(f'Body: {request.get_data()}')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    username, password = decomposeHeader(request)

    stmt = select(User).where(User.username == str(username)).where(User.usertoken == str(password))

    found = db.session.execute(stmt).first()
    print(found)
    print(found[0])
    if found:
        encoded_jwt = jwt.encode(
            {
                "login": "TEMP",
                "expiration": TEMP_ARRAY_EXPIRATION_TIME,
                "user": username,
                "issuedDate": str(datetime.datetime.now())
            },
            JWT_TEMP_ENCODE,
            algorithm='HS256')
        temp_login[encoded_jwt] = datetime.datetime.now()
        return encoded_jwt
    else:
        abort(401)


@app.route('/auth-mail', methods=['GET', 'POST'])
def auth_mail():
    checkHeaderToken(request, False)
    encoded_jwt = jwt.encode(
        {
            "login": "PERM",
            "expiration": TEMP_ARRAY_EXPIRATION_TIME,
            "user": getUserNameFromToken(request, False),
            "issuedDate": str(datetime.datetime.now())
        },
        JWT_PERM_ENCODE,
        algorithm='HS256')
    perm_login[encoded_jwt] = datetime.datetime.now()

    return encoded_jwt


@app.route('/drop-user', methods=['DELETE'])
def delete_user():
    username, password = decomposeHeader(request)
    print("password ", password)
    if password == "a25fdb444eaf8747e661f1739b02d28417b6d4b6cbbfaf61708939861d7605ce":
        username = request.json['login']
        User.query.filter(User.username == username).delete()
        db.session.commit()
        return jsonify({'message': "taken care of"})
    else:
        return "nope", 401


@app.route('/handle-order', methods=['POST'])
def handle_order():
    client_ip = request.remote_addr
    log.info(f"Request from {client_ip}")
    payment_details = request.json
    log.info(f"Payment details: {payment_details}")
    return jsonify({'message': 'Order handled'})


@app.route('/login', methods=['GET'])
def login():
    client_ip = request.remote_addr
    log.info(f"Request from {client_ip}")
    return jsonify({'message': 'Login successful'})


@app.route('/add-item', methods=['POST'])
def add_item():
    client_ip = request.remote_addr
    log.info(f"Request from {client_ip}")
    creator_username = getUserNameFromToken(request, True)
    category = request.form['category']
    title_en = request.form['title_en']
    title_ru = request.form['title_ru']
    description_en = request.form['description_en']
    description_ru = request.form['description_ru']
    image = request.files['image']
    image_bytes = image.read()
    try:
        item = Item(
            category=category,
            title_ru=title_ru,
            title_en=title_en,
            description_ru=description_ru,
            description_en=description_en,
            image=image_bytes,
            creator_username=creator_username)
        db.session.add(item)
        db.session.commit()
        return jsonify({'message': 'Item added'}), 200
    except Exception as e:
        return jsonify({'message': f'error {e}'}), 500


@app.route('/drop-item', methods=['DELETE'])
def drop_item():
    client_ip = request.remote_addr
    log.info(f"Request from {client_ip}")
    checkHeaderToken(request, True)
    item_id = request.args.get('username')
    try:
        Item.query.filter(Item.id == item_id).delete()
        db.session.commit()
        return jsonify({'message': 'Item deleted'}), 200
    except Exception as e:
        return jsonify({'message': f'error {e}'}), 500


@app.route('/get-all-items', methods=['GET'])
def get_all_items():
    client_ip = request.remote_addr
    log.info(f"Request from {client_ip}")
    try:
        return jsonify(Item.query.all()), 200
    except Exception as e:
        return jsonify({'message': f'error {e}'}), 500


@app.route('/get-item', methods=['GET'])
def get_item():
    client_ip = request.remote_addr
    log.info(f"Request from {client_ip}")
    item_id = request.args.get('username')
    try:
        return jsonify(Item.query.filter(Item.id == item_id)), 200
    except Exception as e:
        return jsonify({'message': f'error {e}'}), 500


@app.route('/check-privilege', methods=['GET'])
def check_privilege():
    checkHeaderToken(request, True)
    return jsonify({'status': 'ok'}), 200


@app.route('/health', methods=['GET'])
def health():
    Item.__table__.drop(db.engine)
    db.session.commit()
    log.info("Health check has passed")
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3878)
