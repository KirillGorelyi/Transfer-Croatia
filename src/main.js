import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import { createI18n } from 'vue-i18n';
import en from './locale/en.json';
import ru from './locale/ru.json';
import router from "@/router/index.js";

const i18n = createI18n({
    locale: 'ru', // set locale
    fallbackLocale: 'ru', // set fallback locale
    messages: {
        en,
        ru
    }
});

const app = createApp(App);
app.use(i18n);
app.use(router)
app.mount('#app');