<template>
    <div class="background-layer"></div>
    <div class="logo-container1">
        <img src="../../logo.jpg" alt="logo">
    </div>
    <div class="top-label">
        <div class="top-value">TradePulse —— 一站式A股量化交易平台</div>
        <div class="top-value1">祝您今日愉快！</div>
        <div class="top-value2">用户: {{ username }}</div>
    </div>
    <div class="top-buttons-container">
        <div class="top-buttons">
            <button class="top-button" @click="getInhomepage(username)">首页</button>
            <button class="top-button" @click="getInmarket(username)">市场行情</button>
            <button class="top-button1">模拟交易</button>
            <button class="top-button" @click="getInstrategy(username)">策略</button>
            <button class="top-button" @click="getInfactor(username)">因子回测</button>
            <button class="top-button" @click="switchToLogin">退出账号</button>
        </div>
    </div>
    <div class="trade-info">请搜索您所要买卖的股票</div>
    <div class="search-container1">
        <form @submit.prevent="Getstock" class="form2">
            <input type="text" class="search-container-input" v-model="searchQuery" @input="hideNotFoundMsg" @focus="isInputFocused = true" @blur="isInputFocused = false" placeholder="请输入证券代号" required>
            <button type="submit" class="search-container-button">搜索</button>
        </form>
        <tradewindow v-if="tradeOpen1" :code="code":username = "username" @close="closetrade" />
    </div>
    <div v-if="showNotFoundMsg" class="error-message-box2">
        <span class="error-message2">无法找到您要查找的证券代号</span>
    </div>
    <div class="mystock-container">
        <div class="mystock-message">以下为您仓中所持有股票</div>
        <table class="mystock-table">
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
    
  </template>
  
<script>
import tradewindow from './pop-up-window/tradewindow.vue';
import axios from 'axios';
export default {
    props: {
        username: {
            type: String,
            required: true
        }
    },
    components: {
        tradewindow,
    },
    data() {
        return {
            code: '',
            searchQuery: '', // 搜索框中的内容
            market: ['sh000001','sz399001','bj899050','sh000300'], // 证券代号列表
            showNotFoundMsg: false, // 是否显示未找到代码的消息
            isInputFocused: false,// 输入框是否聚焦的标志
            tradeOpen1: false,
            stocks: []
        };
    },
    mounted()
    {
        this.getmystock();
    },
    methods: {
        switchToLogin() {
            this.$emit('switchToLogin'); 
        },
        getInhomepage(username) {
            this.$emit('getInhomepage', username); 
        },
        getInmarket(username) {
            this.$emit('getInmarket', username);
        },
        getIntrade(username) {
            this.$emit('getIntrade', username);
        },
        getInstrategy(username) {
            this.$emit('getInstrategy', username);
        },
        getInfactor(username) {
            this.$emit('getInfactor', username);
        },
        opentrade() {
            this.tradeOpen1 = true;
        },
        closetrade() {
            this.tradeOpen1 = false;
            this.getmystock();
        },
        async getmystock() {
            // 这里可以提交表单数据到后端保存用户注册信息
                try {
                    //将这四个参数传到后端
                    const response = await axios.post('http://127.0.0.1:5000/user/mystock', {
                        'username': this.username,
                    });
                  const data = response.data; //data的数据结构，[{'name': ,'code': ,'price': ,'quantity': },{...},{...}]
                  const my_stock = data.result
                  console.log('我的持仓', data)
                    this.stocks = my_stock;
                    console.log(my_stock)
                }
                catch (error) {
                  console.error('查看持仓失败:', error);
                    this.errorMessage = '查看持仓失败，请稍后再试';
                }
        },

        async Getstock() {
          try {
                  // 发送异步请求到后端验证用户名和密码
                  const response = await axios.post('http://127.0.0.1:5000/stock/stock_mess', {
                      'code': this.searchQuery.toString()
                  });
              const data = response.data;
              const stock = data.result;
              this.code = this.searchQuery;
              if (stock != null) {
                  
                if (this.market.includes(this.code)) {
                this.showNotFoundMsg = true;
                  }
                else {
                    this.searchQuery = '';
                    this.opentrade();
                this.showNotFoundMsg = false;
                }
                 
                      //user的结构：{'id':0, 'name':0, 'password':0, 'question':0, 'answer':0, 'money':0}
              }
              else {
                  // 显示错误消息
                  this.errorMessage = 'code错误';
                  this.showNotFoundMsg = true;
              }
          }
          catch (error) {
                  console.error('请求失败:', error);
                  // 显示通用错误消息
                  this.errorMessage = '失败，请稍后重试';
              }
        },
       
        hideNotFoundMsg() {
            // 用户输入时隐藏未找到消息
            this.showNotFoundMsg = false;
        },
        
    }
}
</script>
  
<style>
.search-container1 {
    position: absolute;
    top:50%;
    display: flex;
    left:15%;
    width:30%;
    height:50%
}
.trade-info {
    position: absolute;
    top: 33%;
    left: 21%;
    background-color: #727374;
    color: #fdfdfe;
    padding: 20px 20px;
    margin: 50px auto;
    border-radius: 5px;
    width: 300px; /* 设置一个固定的宽度 */
  }

.mystock-container {
    position: absolute;
    top:30%;
    display: flex;
    left:55%;
    width:30%;
    height:50%
}

.mystock-message {
    position: absolute;
    top:0;
    width:100%;
    height:15%;
    background-color: #464748;
    color: rgb(245, 244, 244);
    padding: 15px;
    text-align: center;
}

.mystock-table {
    position: absolute;
    top: 15%;
    width: 100%;
    height: 85%;
    border-collapse: collapse;
    margin: 0; /* 确保表格的外边距为0 */
  }
  
.mystock-table th,
.mystock-table td {
    width:25%;
    height:3%;
    border: 1px solid #0c0c0c;
    padding: 8px 40px;
    text-align: left;
    font-size: 15px; /* 放大字体 */
    background-color: aliceblue;
}
  
  .mystock-table th {
    background-color: #b0adad;
  }
  
  
</style>
  