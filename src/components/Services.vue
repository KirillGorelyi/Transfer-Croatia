<template>
  <div>
    <h1>{{ $t('services') }}</h1>
    <div class="service-list">
      <div class="service-item" v-for="service in services" :key="service.id">
        <h2>{{ service.title }}</h2>
        <p>{{ service.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Services',
  computed: {
    services() {
      return [
        { id: 1, title: this.$t('service1_title'), description: this.$t('service1_desc') },
        { id: 2, title: this.$t('service2_title'), description: this.$t('service2_desc') },
        { id: 3, title: this.$t('service3_title'), description: this.$t('service3_desc') }
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
.service-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.service-item {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 10px;
  width: 30%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.service-item h2 {
  font-size: 1.5em;
  margin-bottom: 10px;
}
.service-item p {
  font-size: 1em;
  color: #555;
}

h2 {
  color: black;
}
</style>
