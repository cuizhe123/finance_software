<template>
  <div class="mydetail">
    <div class="page">
      <button class="exit-button" @click="close">关闭</button>
      <div class="info-message">以下为您仓中所持有股票</div>
      <table class="stock-table">
        <thead>
          <tr>
            <th>名称</th>
            <th>代号</th>
            <th>价格</th>
            <th>持仓数量</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(stock, index) in stocks" :key="index">
            <td>{{ stock.name }}</td>
            <td>{{ stock.code }}</td>
            <td>{{ stock.price }}</td>
            <td>{{ stock.quantity }}</td>
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
      stocks: [
        { 'name': '无', 'code': '000', 'price': 0, 'quantity': 0 },
      ]
    };
  },
  mounted()
  {
    this.getmystock(this.username)
  },
  methods: {
    async getmystock(user_name) {
      // 这里可以提交表单数据到后端保存用户注册信息
                try {
                    //将这四个参数传到后端
                    const response = await axios.post('http://127.0.0.1:5000/user/mystock', {
                        'username': user_name,
                    });
                  const data = response.data; //data的数据结构，[{'name': ,'code': ,'price': ,'quantity': },{...},{...}]
                  const my_stock = data.result
                    this.stocks = my_stock;
                }
                catch (error) {
                  console.error('查看持仓失败:', error);
                    this.errorMessage = '查看持仓失败，请稍后再试';
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
    z-index: 1;
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
    background-color: #2b2b2b;
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
