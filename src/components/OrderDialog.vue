<template>
  <div v-if="show" class="dialog" @click.self="$emit('close')">
    <span class="close" @click="$emit('close')">&times;</span>
    <div class="dialog-content">
      <h2>{{ $t('order-details') }}</h2>
      <form @submit.prevent="submitOrder">
        <div>
          <label>{{ $t('payment-for') + selectedItem.title }}</label>
        </div>
        <div>
          <label>{{ $t('name') }}</label>
          <input type="text" v-model="orderForm.name" required>
        </div>
        <div>
          <label>{{ $t('email') }}</label>
          <input type="email" v-model="orderForm.email" required>
        </div>
        <div>
          <label>{{ $t('card_number') }}</label>
          <input type="text" v-model="orderForm.cardNumber" required>
        </div>
        <div class="expiry-date">
          <label>{{ $t('card_expiry') }}</label>
          <div class="expiry-inputs">
            <input
                type="text"
                v-model="orderForm.expiryMonth"
                maxlength="2"
                @input="formatMonth"
                required
            >
            <span style="color: #333">/</span>
            <input
                type="text"
                v-model="orderForm.expiryYear"
                maxlength="2"
                required
            >
          </div>
        </div>
        <div>
          <label>{{ $t('card_cvv') }}</label>
          <input type="text" v-model="orderForm.cardCVV" maxlength="3" required>
        </div>
        <button type="submit">{{ $t('submit') }}</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrderDialog',
  props: {
    show: {
      type: Boolean,
      required: true
    },
    selectedItem: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      orderForm: {
        name: '',
        email: '',
        payment: '',
        cardNumber:'',
        expiryMonth:'',
        expiryYear:'',
        cardCVV:''
      }
    };
  },
  methods: {
    submitOrder() {
      console.log(this.orderForm);
      alert('Order submitted!');
      this.$emit('close');
    },
    formatMonth() {
      if (this.orderForm.expiryMonth.length === 1 && this.orderForm.expiryMonth > 1) {
        this.orderForm.expiryMonth = '0' + this.orderForm.expiryMonth;
      }
    }
  }
};
</script>

<style scoped>
.dialog {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.dialog-content {
  position: relative;
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 90%;
  height: 90%;
  max-width: 800px;
  max-height: 800px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  overflow-y: auto;
}
.dialog-content h2 {
  margin-top: 0;
}
.dialog-content form {
  display: flex;
  flex-direction: column;
}
.dialog-content form div {
  margin-bottom: 15px;
}
.dialog-content form label {
  font-weight: bold;
  margin-bottom: 5px;
}
.dialog-content form input {
  padding: 8px;
  box-sizing: border-box;
  width: 100%;
}
.dialog-content button {
  background-color: #2196F3;
  color: white;
  padding: 10px;
  border: none;
  cursor: pointer;
  margin-top: 10px;
}
.dialog-content button:hover {
  background-color: #0b7dda;
}
.close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  cursor: pointer;
  color: #aaa;
}
.close:hover {
  color: #000;
}

.expiry-date {
  display: flex;
  flex-direction: column;
}
.expiry-inputs {
  display: flex;
  align-items: center;
}
.expiry-inputs input {
  width: 50px;
  margin-right: 5px;
  text-align: center;
}
.expiry-inputs span {
  margin: 0 5px;
}
h1, h2, label {
  color:#333;
}
</style>
