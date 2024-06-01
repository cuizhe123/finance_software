<template>
    <div class="background-layer"></div>
    <div class="logo-container1">
        <img src="../../logo.jpg" alt="logo">
    </div>
    <div class="top-label">
        <div class="top-value">欢 迎 来 到 金 霸 霸 量 化 交 易 平 台 ！您 的 最 佳 选 择 !</div>
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
    <div class="trade-info">
        <div>请搜索您所要买卖的股票</div>
    </div>
    <div class="search-container1">
        <form @submit.prevent="handleSubmit" class="form2">
            <input type="number" class="search-container-input" v-model.number="searchQuery" @input="hideNotFoundMsg" @focus="isInputFocused = true" @blur="isInputFocused = false" placeholder="请输入证券代号" required>
            <button type="submit" class="search-container-button">搜索</button>
        </form>
        <tradewindow v-if="tradeOpen1" :code="code" @close="closetrade" />
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
            securities: ['000001', '399001', '399005', '000300'], // 证券代号列表
            showNotFoundMsg: false, // 是否显示未找到代码的消息
            isInputFocused: false,// 输入框是否聚焦的标志
            tradeOpen1: false,
            stocks: [
                { name: '股票A', code: '001', price: 10.5, quantity: 100 },
                { name: '股票B', code: '002', price: 20.3, quantity: 150 },
                { name: '股票C', code: '003', price: 15.8, quantity: 80 },
                { name: '股票D', code: '003', price: 15.8, quantity: 80 },
                { name: '股票E', code: '003', price: 15.8, quantity: 80 },
              
            ]
        };
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
        },
        handleSubmit() {
            // 检查搜索的证券代码是否存在
            if (this.searchQuery !== '' && this.securities.includes(this.searchQuery.toString())) {
                this.code = this.searchQuery.toString();               
                this.opentrade();
                // 重置搜索框和未找到消息
                this.searchQuery = '';
                this.showNotFoundMsg = false;
            } else {
                // 显示未找到消息
                if (!this.isInputFocused) {
                    this.showNotFoundMsg = true;
                }
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
    background-color: #4cc3e0;
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
    background-color: #1670d0;
    color: rgb(10, 9, 9);
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
  