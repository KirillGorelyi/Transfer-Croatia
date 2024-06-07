<template>
  <div class="edit-dialog">
    <div class="dialog-content">
      <h2>Edit Item</h2>
      <form @submit.prevent="saveItem">
        <div class="form-group">
          <label for="name-en">Название (на английском):</label>
          <input type="text" v-model="item.title_en" required>
        </div>
        <div class="form-group">
          <label for="name-ru">Название (на русском):</label>
          <input type="text" v-model="item.title_ru" required>
        </div>
        <div class="form-group">
          <label for="description-en">Описание (на английском):</label>
          <textarea v-model="item.description_en"></textarea>
        </div>
        <div class="form-group">
          <label for="description-ru">Описание (на русском):</label>
          <textarea v-model="item.description_ru"></textarea>
        </div>
        <div class="dialog-actions">
          <button type="submit" class="save-button">Save</button>
          <button type="button" class="cancel-button" @click="$emit('close')">Cancel</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    item: Object
  },
  methods: {
    saveItem() {
      this.$emit('save', this.item);
    }
  }
};
</script>

<style scoped>
.edit-dialog {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.dialog-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  font-size: 24px;
  color: #333;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

input, textarea {
  width: calc(100% - 20px);
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

textarea {
  resize: vertical;
}

.dialog-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.save-button, .cancel-button {
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.save-button {
  background-color: #007bff;
  color: white;
  transition: background-color 0.2s;
}

.save-button:hover {
  background-color: #0056b3;
}

.cancel-button {
  background-color: #ccc;
  color: #333;
  transition: background-color 0.2s;
}

.cancel-button:hover {
  background-color: #999;
}
</style>
