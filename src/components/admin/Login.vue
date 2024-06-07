<template>
  <div class="login">
    <h2>Вход</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Имя пользователя:</label>
        <input type="text" v-model="username" required>
      </div>
      <div>
        <label for="password">Пароль:</label>
        <input type="password" v-model="password" required>
      </div>
      <button type="submit">Войти</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async login() {
      const authHeader = 'Basic ' + btoa(`${this.username}:${this.password}`);
      try {
        let response = await axios.get('http://localhost:3878/auth',  {
          headers: {
            'Authorization': authHeader
          }
        });
        const temporary_token= response.data;
        response = await axios.get('http://localhost:3878/auth-mail',  {
          headers: {
            'Authorization': 'Bearer '+temporary_token
          }
        });

        localStorage.setItem('perm_token', response.data);
        console.log(response.data)

        this.$router.push('/admin'); // Redirect to dashboard or another page
      } catch (error) {
        this.errorMessage = 'Invalid username or password';
      }
    }
  }
};
</script>

<style scoped>
.login {
  max-width: 300px;
  margin: 0 auto;
  padding: 1em;
  border: 1px solid #ccc;
  border-radius: 4px;
  position: fixed;
  top:35%;
  left:40%
}
.login h2 {
  text-align: center;
}
.login div {
  margin-bottom: 1em;
}
.login label {
  display: block;
  margin-bottom: 0.5em;
}
.login input {
  width: 100%;
  padding: 0.5em;
  box-sizing: border-box;
}
.login button {
  width: 100%;
  padding: 0.7em;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.login button:hover {
  background-color: #0056b3;
}
.login p {
  color: red;
  text-align: center;
}
</style>
