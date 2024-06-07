<template>
  <div>
  <LanguageSwitcher />
    <nav>
      <ul>
        <li ><router-link to="/">{{ $t('home') }}</router-link></li>
        <li><router-link to="/excursions">{{ $t('excursions') }}</router-link></li>
        <li><router-link to="/tours">{{ $t('tours') }}</router-link></li>
        <li><router-link to="/contact">{{ $t('contact') }}</router-link></li>
        <li><router-link to="/services">{{ $t('services') }}</router-link></li>
        <li><router-link to="/about-us">{{ $t('about_us_title') }}</router-link></li>
      </ul>
    </nav>
  </div>
</template>

<script>
import LanguageSwitcher from './LanguageSwitcher.vue';
export default {
  name: 'Header',
  components: {
    LanguageSwitcher
  }
};
</script>

<style>
header {
  background-color: #333;
  color: #fff;
}
nav ul {
  list-style-type: none;
}
nav ul li {
  display: grid;
  margin-right: 10px;
}

li {
  width: auto;
}
</style>
