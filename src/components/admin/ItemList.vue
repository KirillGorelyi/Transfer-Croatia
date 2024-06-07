<template>
  <div class="items-list">
    <h3>Added Items</h3>
    <ul>
      <li v-for="item in items" :key="item.id" class="item">
        <div class="item-content">
          <p class="item-title"><strong>{{ item.title_en }}</strong> ({{ item.category }})</p>
          <p class="item-description">{{ item.description_en }}</p>
          <img :src="item.image" alt="Image" v-if="item.image" class="item-image"/>
        </div>
        <button @click="$emit('edit-item', item)" class="edit-button">Edit</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: []
    };
  },
  methods: {
    async fetchItems() {
      try {
        const response = await axios.get('http://localhost:3878/get-items', {
          headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('perm_token')
          }
        });
        this.items = response.data.items;
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    }
  },
  mounted() {
    this.fetchItems();
  }
};
</script>

<style scoped>
.items-list {
  margin-top: 30px;
}

.items-list h3 {
  text-align: center;
  margin-bottom: 15px;
  font-size: 24px;
  color: #333;
}

.items-list ul {
  list-style-type: none;
  padding: 0;
}

.item {
  background-color: #fff;
  padding: 20px;
  margin-bottom: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: transform 0.2s;
}

.item:hover {
  transform: scale(1.02);
}

.item-content {
  max-width: 80%;
}

.item-title {
  font-size: 18px;
  color: #333;
  margin: 0;
}

.item-description {
  font-size: 14px;
  color: #666;
  margin: 5px 0 0;
}

.item-image {
  max-width: 100px;
  max-height: 100px;
  border-radius: 4px;
  margin-top: 10px;
}

.edit-button {
  padding: 10px 15px;
  font-size: 14px;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.edit-button:hover {
  background-color: #0056b3;
}
</style>
