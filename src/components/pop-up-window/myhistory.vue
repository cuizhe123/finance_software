<template>
    <div class="mydetail">
      <div class="page">
        <button class="exit-button" @click="close">关闭</button>
        <div class="info-message">以下为您的历史交易记录</div>
        <table class="stock-table">
          <thead>
            <tr>
              <th>时间</th>
              <th>序号</th>
              <th>代号</th>
              <th>买卖</th>
              <th>交易价格</th>
              <th>交易数量</th>
              <th>盈亏</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in history" :key="index">
              <td>{{ item.time }}</td>
              <td>{{ item.number}}</td>
              <td>{{ item.code}}</td>
              <td>{{ item.buysell}}</td>
              <td>{{ item.price }}</td>
              <td>{{ item.quantity }}</td>
              <td>{{ item.gain }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>  
  </template>
    
  <script>
  import axios from 'axios';
  export default {
    props: {
      username: {
        type: String,
        required: true
      },
    },
    data() {
      return {
        history: [
          { 'time':0 , 'number':0 , 'code': '001','buysell':'买', 'price': 10.5, 'quantity': 100,'gain':0 },
        ]
      };
    },
    mounted()
    {
      this.GetHistory()
    },
    methods: {
      async GetHistory() {
                // 这里可以提交表单数据到后端保存用户注册信息
                try {
                    //将这四个参数传到后端
                    const response = await axios.post('http://127.0.0.1:5000/user/history', {
                        'username': this.username,
                    });
                    const data = response.data; //data的数据结构，[{ 'time':0 , 'number':0 , 'code': '001','buysell':'买', 'price': 10.5, 'quantity': 100,'gain':0 },{...},{...}]
                    this.history = data.result;
                    console.log('我的交易历史')
                    } catch (error) {
                    console.error('查看历史失败:', error);
                    this.errorMessage = '查看历史失败，请稍后再试';
                }
                    
          
        },

      close() {
        this.$emit('close');
      },
    },
  }
  </script>
    
  <style>
    .mydetail {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: #f0eeee;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      width: 80%; /* 调整浮窗宽度 */
      max-height: 80vh; /* 设置最大高度为屏幕高度的80%，超出部分可滚动 */
      overflow-y: auto; /* 垂直方向溢出部分滚动 */
      height: 70%; /* 调整浮窗高度 */
      padding: 0; /* 去除内边距 */
    }
    
    .page {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      padding: 0;
    }
    
    .stock-table {
      width: 100%;
      border-collapse: collapse;
      margin: 0; /* 确保表格的外边距为0 */
    }
    
    .stock-table th,
    .stock-table td {
      border: 1px solid #ddd;
      padding: 10px 30px;
      text-align: left;
      font-size: 20px; /* 放大字体 */
    }
    
    .stock-table th {
      background-color: #b0adad;
    }
    
    .info-message {
      background-color: #1670d0;
      color: white;
      padding: 30px;
      text-align: center;
    }
    
    .exit-button {
      position: absolute;
      top: -20px; /* 尝试将按钮上移以消除上方间距 */
      left: 0;
      background-color: #847d7d;
      color: #000;
      font-size: 18px;
      height: 50px; 
      width: 80px;
      z-index: 1; /* 确保按钮位于标签图层的上面 */
      
    }
    
    .exit-button:hover {
      background-color: #3e4146; /* 按钮悬停时的背景色 */
    }
  </style>
  