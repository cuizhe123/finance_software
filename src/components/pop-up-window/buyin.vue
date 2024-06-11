<template>
  <div class="buy-in-popup">
    <button class="exit-button" @click="close">关闭</button>
    <div class="popup-title-container">
      <p class="popup-title1">您当前的持仓数量为:{{this.total_quantity}}</p>
      <p class="popup-title2">持有金额为{{this.cash}}</p>
      <p class="popup-title">您要买入的数量为：</p>
    </div>
    <div class="input-container">
      <input type="number" v-model="buy_quantity" placeholder="请输入数量" min="1" step="1">
    </div>
    <button class="confirm-button" @click="buyin">确认</button>
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

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
    username: {
      type: String,
      required: true
    },
    currentPrice: {
     type: Number,
      required: true
    }
  },
  data() {
    return {
      total_quantity: 100, //总数量
      buy_quantity: 1, // 数量
      errorMessage: '', // 错误消息
      successMessage: '', // 成功消息
      cash:10,
    };
  },
  mounted() {
    this.GetMessage()
    this.getstock()
  },
  methods: {
    close() {
      this.$emit('close');
    },
    async buyin() {
          try {
                  const response = await axios.post('http://127.0.0.1:5000/trade/buyin', {
                    'username': this.username,
                    'stock_code': this.code,
                    'stock_name': this.stockname,
                    'buy_quantity': this.buy_quantity,
                    'price': this.currentPrice
                  });
              const data = response.data;
            const result = data.result;
            console.log(this.username, this.code, this.stockname,this.buy_quantity, this.currentPrice)
            console.log('购买结果', result);
            if (result) {
              //购买成功，进行跳转或其他操作
              this.GetMessage()
              this.getstock()
              this.errorMessage = '';
            }
            else {
              console.log('报错');
              this.errorMessage = '购买失败，资金不足';
            }   
          }
          catch (error) {
                  console.error('请求失败:', error);
                  // 显示通用错误消息
                  this.errorMessage = '失败，请稍后重试';
              }
    },
    async GetMessage() {
          try {
                  // 发送异步请求到后端验证用户名和密码
                  const response = await axios.post('http://127.0.0.1:5000/user/by_name', {
                      'username': this.username
                  });
                  // 后端返回验证结果
                //成功的话，返回[user的信息,'successful']，失败的话返回[None,错误信息]
              const data = response.data;
              const user = data.user;
                // console.log(data.user.name)
              if (data.user != null) {
                  this.cash = user.money
                    //登录成功，进行跳转或其他操作
                  //user的结构：{'id':0, 'name':0, 'password':0, 'question':0, 'answer':0, 'money':0}
                      
                  } else {
                      // 显示错误消息
                      this.errorMessage = '用户名或密码错误';
                  }
              } catch (error) {
                  console.error('登录请求失败:', error);
                  // 显示通用错误消息
                  this.errorMessage = '登录失败，请稍后重试';
              }
    },
    async getstock() {
                // 这里可以提交表单数据到后端保存用户注册信息
                try {
                    //将这四个参数传到后端
                    const response = await axios.post('http://127.0.0.1:5000/user/my_single_stock', {
                      'username': this.username,
                        'code':this.code
                    });
                  const data = response.data; //data的数据结构，[{'name': ,'code': ,'price': ,'quantity': },{...},{...}]
                  const num = data.result;
                  console.log('我的持仓', num);
                  this.total_quantity = num;
                }
                catch (error) {
                  console.error('查看持仓失败:', error);
                    this.errorMessage = '查看持仓失败，请稍后再试';
                }
        },


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
    top:10%;
    left: 50%;
    width: 50%;
    height: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    background-color: rgb(3, 215, 74);
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
    top:65%;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    display: block;
    width: 30%;
    padding: 10px;
    background-color: #828384;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .confirm-button:hover {
    background-color: #323333;
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
  