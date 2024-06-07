<template>
  <div id="app">
    <header v-show="login !== 'true'">
      <Header/>
    </header>
    <main>
      <router-view/>
    </main>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import axios from "axios";

export default {
  name: 'App',
  components: {
    Header
  },
  data() {
    return {
      login: localStorage.getItem('login') || ''
    };
  },
  created() {
    window.addEventListener('storage', this.updateLocalStorageValue);
  },
  beforeDestroy() {
    window.removeEventListener('storage', this.updateLocalStorageValue);
  },
  methods: {
    updateLocalStorageValue(event) {
      if (event.key === 'login') {
        this.login = event.newValue;
      }
    }
  },
  watch: {
    async '$route'(to, from) {
      console.log(to)
      console.log(from)
      console.log(to.path)
      console.log(from.path)

      if (to.path === '/login' || to.path === '/admin') {
        if (to.path === '/admin') {

          await axios.get('http://localhost:3878/check-privilege', {
            headers: {
              'Authorization': 'Bearer ' + localStorage.getItem('perm_token')
            }
          }).catch(_ => {
                this.$router.push('/login');
              }
          );

        }
        this.login = 'true';
        localStorage.setItem('login', "true");
      } else {
        this.login = 'false';
        localStorage.setItem('login', "false");
      }
    }
  }
};
</script>


<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  .head {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  header {
    height: 100%;
    width: 200px;
    position: absolute;
    top: 0;
    left: 0;
  }

  main {
    position: absolute;
    top: 30%;
    left: 250px;
  }

  h1, h2, h3 {
    font-size: 2em;
    color: #333;
    text-align: center;
    margin-bottom: 20px;
  }
}
</style>
