<template>
  <div>
    <h1>{{ $t('contact') }}</h1>
    <div>
      <label>{{ $t('vk') }}</label>
      <a>https://vk.com/gid.horvatia</a>
    </div>
    <div>
      <label>{{ $t('mail') }}</label>
      <a href="mailto:ulika2210@mail.ru">ulika2210@mail.ru</a>
    </div>
    <div>
      <label>{{ $t('phone') }}</label>
      <a href="tel:+385981706998">+385981706998</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Contact',
  data() {
    return {
      form: {
      }
    };
  },
  methods: {
    submitForm() {

      console.log(this.form);
      alert('Form submitted!');
    }
  }
};
</script>

<style scoped>
h1 {
  font-size: 2em;
  color: #333;
}
form {
  max-width: 600px;
  margin: 0 auto;
}
form div {
  margin-bottom: 15px;
}
label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}
input, textarea {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}
button {
  background-color: #2196F3;
  color: white;
  padding: 10px 15px;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #0b7dda;
}
</style>
