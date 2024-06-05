<template>
    <div class="sell-out-popup">
      <button class="exit-button" @click="close">关闭</button>
      <div class="popup-title-container">
        <p class="popup-title1">您当前的持仓数量为:{{this.total_quantity}}</p>
        <p class="popup-title2">持有金额为{{this.cash}}</p>
        <p class="popup-title">您要卖出的数量为:</p>
      </div>
      <div class="input-container">
        <input type="number" v-model="sell_quantity" placeholder="请输入数量" min="1" step="1">
      </div>
      <button class="confirm-button" @click="confirm">确认</button>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      stockname: {
        type: String,
        required: true
      },
      code: {
        type: String,
        required: true
      },
      //currentPrice: {
       // type: Number,
        //required: true
      //},
      //cash: {
        //type: Number,
        //required: true
      //}
    },
    data() {
      return {
        total_quantity: 10, //总数量
        sell_quantity: 1, // 数量
        errorMessage: '', // 错误消息
        successMessage: '', // 成功消息
        cash:10,
        currentPrice:10
      };
    },
    methods: {
      close() {
        this.$emit('close');
      },
      confirm() {
        const totalPrice = this.sell_quantity * this.currentPrice;
        const a = this.sell_quantity - this.total_quantity;
        if ( a > 0 ) {
          this.errorMessage = '卖出数量超过您的持仓数量，请重新输入';
          this.successMessage = '';
        } else {
          // 购买成功，触发成功交易事件
          this.successMessage = `成功卖出 ${this.sell_quantity} 股 ${this.stockname}`;
          this.errorMessage = '';
          // 更新已有金额和持仓信息
          this.cash += totalPrice;
          this.total_quantity -=this.sell_quantity;
          // 在这里可以触发更新持仓信息的事件或者执行其他操作
        }
      }
    }
  };
  </script>
    
    <style scoped>
    .sell-out-popup {
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
        top:10%;
        left: 50%;
        width: 50%;
        height: 50%;
        transform: translateX(-50%); /* 平移自身宽度的一半 */
        background-color: rgb(237, 35, 39);
        font-weight: bold;
        margin-bottom: 15px;
      }
      .popup-title1{
        position: absolute;
        top:10%;
        left: 50%;
        width: 50%;
        height: 30%;
        transform: translateX(-50%); /* 平移自身宽度的一半 */
        font-size: 18px;
      }

      .popup-title2{
        position: absolute;
        top:28%;
        left: 50%;
        width: 50%;
        height: 30%;
        transform: translateX(-50%); /* 平移自身宽度的一半 */
        font-size: 18px;
      }

      .popup-title{
        position: absolute;
        top:47%;
        left: 50%;
        width: 50%;
        height: 30%;
        transform: translateX(-50%); /* 平移自身宽度的一半 */
        font-size: 18px;
      }
      
      .input-container {
        position: absolute;
        top:45%;
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
        top:60%;
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
    
      .error-message{
        position: absolute;
        top: 90%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 8px;
        background-color: #ffcccc;
        color: #f80f0b;
        border: 1px solid #e40808;
        border-radius: 4px;
      }
    .success-message {
      position: absolute;
      top: 90%;
      left: 50%;
      transform: translate(-50%, -50%);
      padding: 8px;
      background-color: #ccffd5;
      color: green;
      border: 1px solid #08e43b;
      border-radius: 4px;
    }
    </style>
    