<template>
  <div>
    <h1>{{ $t('excursions') }}</h1>
    <div class="excursion-list">
      <div class="excursion-item" v-for="excursion in excursions" :key="excursion.id">
        <h2>{{ excursion.title }}</h2>
        <p>{{ excursion.description }}</p>
        <button @click="openDialog(excursion)">{{ $t('order') }}</button>
      </div>
    </div>
    <OrderDialog
        :show="showDialog"
        :selectedItem="selectedItem"
        @close="closeDialog"/>
  </div>
</template>

<script>
import OrderDialog from "@/components/OrderDialog.vue";

export default {
  name: 'Excursion',
  components: {OrderDialog},
  computed: {
    excursions() {
      return [
        { id: 1, title: this.$t('excursion1_title'), description: this.$t('excursion1_desc') },
        { id: 2, title: this.$t('excursion2_title'), description: this.$t('excursion2_desc') },
        { id: 3, title: this.$t('excursion3_title'), description: this.$t('excursion3_desc') }
      ];
    }
  },
  data() {
    return {
      showDialog: false,
      selectedItem: {}
    }
  },
  methods: {
    openDialog(excursion) {
      this.showDialog = true
      this.selectedItem = excursion
    },
    closeDialog() {
      this.showDialog = false;
    }
  }
};
</script>

<style scoped>
h1, h2 {
  font-size: 2em;
  color: #333;
  text-align: center;
  margin-bottom: 20px;
}
.excursion-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.excursion-item {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 10px;
  width: 30%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.excursion-item h2 {
  font-size: 1.5em;
  margin-bottom: 10px;
}
.excursion-item p {
  font-size: 1em;
  color: #555;
}
</style>
