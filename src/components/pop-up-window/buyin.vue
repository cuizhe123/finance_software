<template>
    <div class="buy-in-popup">
        <button class="exit-button" @click="close">关闭</button>
        <div class="popup-title-container">
            <p class="popup-title">您要买入的数量为：</p>
        </div>
        <div class="input-container">
            <input type="number" v-model="quantity" placeholder="请输入数量" min="1" step="1">
        </div>
        <button class="confirm-button" @click="confirm">确认</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        quantity: 1 // 默认数量为1
      };
    },
    methods: {
      close() {
        this.$emit('close');
      },
      confirm() {
        // 在这里执行确认购买的逻辑，可以使用 this.quantity 获取输入的数量
        console.log('确认购买数量为:', this.quantity);
        // 在这里可以触发关闭浮窗的事件或者执行其他操作
      }
    }
  };
  </script>
  
  <style scoped>
  .buy-in-popup {
    z-index: 1;
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  }
  
  .popup-title-container {
    position: absolute;
    top:15%;
    left: 50%;
    width: 50%;
    height: 30%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    background-color: rgb(3, 215, 74);
    font-weight: bold;
    margin-bottom: 15px;
  }
  .popup-title{
    position: absolute;
    top:17%;
    left: 50%;
    width: 50%;
    height: 30%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    font-size: 18px;
  }
  
  .input-container {
    position: absolute;
    top:30%;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    margin-bottom: 15px;
  }
  
  input[type="number"] {
    width: calc(100% - 22px);
    padding: 8px;
    border: 1px solid #0c0c0c;
    border-radius: 4px;
  }
  
  .confirm-button {
    position: absolute;
    top:50%;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    display: block;
    width: 30%;
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .confirm-button:hover {
    background-color: #0056b3;
  }
  </style>
  