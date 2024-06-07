<template>
  <div>
    <h1>{{ $t('tours') }}</h1>
    <div class="tour-list">
      <div class="tour-item" v-for="service in services" :key="service.id">
        <h2>{{ service.title }}</h2>
        <p>{{ service.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Tours',
  computed: {
    services() {
      return [
        { id: 1, title: this.$t('tour1_title'), description: this.$t('tour1_desc') },
        { id: 2, title: this.$t('tour2_title'), description: this.$t('tour2_desc') },
        { id: 3, title: this.$t('tour3_title'), description: this.$t('tour3_desc') }
      ];
    }
  }
};
</script>

<style scoped>
h1 {
  font-size: 2em;
  color: #333;
  text-align: left;
  margin-bottom: 20px;
}
.tour-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.tour-item {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 10px;
  width: 30%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.tour-item h2 {
  font-size: 1.5em;
  margin-bottom: 10px;
}
.tour-item p {
  font-size: 1em;
  color: #555;
}

h2 {
  color: black;
}
</style>
