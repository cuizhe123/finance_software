<template>
    <div class="logo-container1">
        <img src="../../public/logo.jpg" alt="logo">
    </div>
    <div class="top-label">
        <div class="top-value">欢 迎 来 到 金 霸 霸 量 化 交 易 平 台 ！您 的 最 佳 选 择 !</div>
        <div class="top-value1">祝您今日愉快！</div>
        <div class="top-value2">用户: {{ username }}</div>
    </div>
    <div class="top-buttons-container">
        <div class="top-buttons">
            <button class="top-button" @click="getInhomepage">首页</button>
            <button class="top-button" @click="getInmarket">市场行情</button>
            <button class="top-button1">模拟交易</button>
            <button class="top-button" @click="getInstrategy">策略</button>
            <button class="top-button" @click="getInfactor">因子回测</button>
            <button class="top-button" @click="switchToLogin">退出账号</button>
        </div>
    </div>
    <div class="trade-info">
        <div>请搜索您所要买卖的股票</div>
    </div>
    <div class="search-container1">
        <form @submit.prevent="handleSubmit" class="form2">
            <input type="number" class="search-container-input" v-model.number="searchQuery" @input="hideNotFoundMsg" @focus="isInputFocused = true" @blur="isInputFocused = false" placeholder="请输入证券代码" required>
            <button type="submit" class="search-container-button">搜索</button>
        </form>
        <tradewindow v-if="tradeOpen1" :code="code" @close="closetrade" />
    </div>
    <div v-if="showNotFoundMsg" class="error-message-box2">
        <span class="error-message2">无法找到您要查找的证券代码</span>
    </div>
        
  </template>
  
<script>
import tradewindow from './pop-up-window/tradewindow.vue';
export default {
    components: {
        tradewindow,
    },
    data() {
        return {
            username: 'John Doe', // 用户名
            code: '',
            searchQuery: '', // 搜索框中的内容
            securities: ['000001', '399001', '399005', '000300'], // 证券代号列表
            showNotFoundMsg: false, // 是否显示未找到代码的消息
            isInputFocused: false,// 输入框是否聚焦的标志
            tradeOpen1: false
        };
    },
    methods: {
        switchToLogin() {
            this.$emit('switchToLogin'); // 触发自定义事件
        },
        getInhomepage() {
            this.$emit('getInhomepage'); // 触发自定义事件
        },
        getInmarket() {
            this.$emit('getInmarket'); // 触发自定义事件
        },
        getIntrade() {
            this.$emit('getIntrade'); // 触发自定义事件
        },
        getInstrategy() {
            this.$emit('getInstrategy'); // 触发自定义事件
        },
        getInfactor() {
            this.$emit('getInfactor'); // 触发自定义事件
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
    left:20%;
    width:30%;
    height:50%
}
.trade-info {
    position: absolute;
    top: 33%;
    left: 26%;
    background-color: #4cc3e0;
    padding: 20px 20px;
    margin: 50px auto;
    border-radius: 5px;
    width: 300px; /* 设置一个固定的宽度 */
  }


</style>
  