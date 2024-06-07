<template>
  <div class="language-switcher">
    <span @click="changeLocale('ru')" :class="{ active: currentLocale === 'ru' }">Русский</span>
    <span> | </span>
    <span @click="changeLocale('en')" :class="{ active: currentLocale === 'en' }">English</span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentLocale: this.$i18n.locale
    };
  },
  methods: {
    changeLocale(locale) {
      this.$i18n.locale = locale;
      this.currentLocale = locale;
      localStorage.setItem('language', locale);
    }
  }
};
</script>


<style scoped>
.language-switcher {
  position: absolute;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.language-switcher span {
  margin: 0 5px;
  color: #fff;
  cursor: pointer;
}
.language-switcher span.active {
  font-weight: bold;
}
.language-switcher span:hover {
  text-decoration: underline;
}
</style>
