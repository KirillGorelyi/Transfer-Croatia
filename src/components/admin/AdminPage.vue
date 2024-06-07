<template>
  <div class="container-admin-page">
  <div class="admin-page">
    <h2>Admin Page</h2>
    <form @submit.prevent="addItem">
      <div class="form-group">
        <label for="entity">Добавить запись в :</label>
        <select v-model="selectedEntity.type" required>
          <option v-for="entity in entities" :key="entity.type" :value="entity.type">{{ entity.visibleName }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="name-en">Название (на английском):</label>
        <input type="text" v-model="name.en" required>
      </div>
      <div class="form-group">
        <label for="name-ru">Название (на русском):</label>
        <input type="text" v-model="name.ru" required>
      </div>
      <div class="form-group">
        <label for="description-en">Описание (на английском):</label>
        <textarea v-model="description.en"></textarea>
      </div>
      <div class="form-group">
        <label for="description-ru">Описание (на русском):</label>
        <textarea v-model="description.ru"></textarea>
      </div>
      <div class="form-group">
        <label for="picture">Загрузить фотографию:</label>
        <input type="file" @change="onFileChange" required>
      </div>
      <button type="submit">Добавить запись</button>
    </form>

    <div class="items-list">
      <h3>Added Items</h3>
      <ul>
        <li v-for="item in items" :key="item.id">
          <p><strong>{{ item.title_en }}</strong> ({{ item.category }})</p>
          <p>{{ item.description_en }}</p>
          <img :src="item.image" alt="Image" v-if="item.image"/>
        </li>
      </ul>
    </div>
  </div>
  <ItemList @edit-item="openEditDialog" />
  <EditDialog :item="selectedItem" v-if="showEditDialog" @close="showEditDialog = false" @save="saveEditItem" />
  </div>
</template>

<script>
import axios from 'axios';
import ItemList from './ItemList.vue';
import EditDialog from './EditDialog.vue';

export default {
  components: {
    ItemList,
    EditDialog
  },
  data() {
    return {
      entities: [
        { 'visibleName': 'Экскурсии', 'type': 'Excursion' },
        { 'visibleName': 'Туры', 'type': 'Tours' },
        { 'visibleName': 'Услуги', 'type': 'Services' }
      ],
      selectedEntity: '',
      name: {
        en: '',
        ru: ''
      },
      description: {
        en: '',
        ru: ''
      },
      picture: null,
      items: [],
      showEditDialog: false,
      selectedItem: null
    };
  },
  methods: {
    onFileChange(event) {
      this.picture = event.target.files[0];
    },
    async addItem() {
      const formData = new FormData();
      formData.append('category', this.selectedEntity);
      formData.append('title_en', this.name.en);
      formData.append('title_ru', this.name.ru);
      formData.append('description_en', this.description.en);
      formData.append('description_ru', this.description.ru);
      formData.append('image', this.picture);

      try {
        const response = await axios.post('http://localhost:3878/add-item', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer ' + localStorage.getItem('perm_token')
          }
        });
        if (response.status === 200) {
          alert('Item added successfully');
          this.resetForm();
          this.fetchItems();
        } else {
          alert('Failed to add item');
        }
      } catch (error) {
        console.error('Error adding item:', error);
        alert('Error adding item');
      }
    },
    resetForm() {
      this.selectedEntity = '';
      this.name.en = '';
      this.name.ru = '';
      this.description.en = '';
      this.description.ru = '';
      this.picture = null;
    },
    openEditDialog(item) {
      this.selectedItem = item;
      this.showEditDialog = true;
    },

    async saveEditItem(item) {
      try {
        const response = await axios.put(`http://localhost:3878/update-item/${item.id}`, item, {
          headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('perm_token')
          }
        });
        if (response.status === 200) {
          this.showEditDialog = false;
          await this.$refs.itemList.fetchItems();
        } else {
          alert('Failed to update item');
        }
      } catch (error) {
        console.error('Error updating item:', error);
        alert('Error updating item');
      }
    }
  },
  mounted() {
    this.fetchItems();
  }
};
</script>

<style scoped>
.admin-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
  font-weight: bold;
}

input, select, textarea {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  box-sizing: border-box;
}

button {
  padding: 10px;
  font-size: 16px;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  align-self: center;
}

button:hover {
  background-color: #0056b3;
}

.items-list {
  margin-top: 30px;
}

.items-list h3 {
  text-align: center;
  margin-bottom: 15px;
}

.items-list ul {
  list-style-type: none;
  padding: 0;
}

.items-list li {
  background-color: #fff;
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.items-list li p {
  margin: 0;
}

.items-list li img {
  max-width: 100%;
  border-radius: 4px;
  align-self: center;
}

.container-admin-page{
  display: flex
}
</style>
