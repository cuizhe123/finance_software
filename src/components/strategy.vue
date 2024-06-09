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
            <button class="top-button" @click="getIntrade(username)">模拟交易</button>
            <button class="top-button1">策略</button>
            <button class="top-button" @click="getInfactor(username)">因子回测</button>
            <button class="top-button" @click="switchToLogin">退出账号</button>
        </div>
    </div>
    <div class="strategy-container" v-for="index in 5" :key="index">
        <div class="strategy-label">策略 {{ index }}</div>
        <button class="strategy-button" @click="goTostrategy(index,username)">{{strategyArray[index-1]}}</button>
    </div>
  </template>
  
<script>
import axios from 'axios';
export default {
    props: {
        username: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            index:1, //策略编号
            strategyArray: [
            'SVM',
            'RNN',
            'LSTM',
            'GRU',
            '集成策略'
            ],
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
        goTostrategy(index,username) {
            this.$emit('goTostrategy', index, username);
        }
    }
}
</script>
  
<style>
.strategy-container {
    position: relative;
    display: flex;
    align-items: center;
    margin-bottom: 10px; /* 调整标签之间的间距 */
    top: 40px;
    left: 200px;
  }
.strategy-label {
    position: relative;
    background-color: #4cc3e0;
    padding: 14px 15px;
    border-radius: 5px;
    width: 100px; /* 设置一个固定的宽度 */
    height: 50px;
    top:10px
}
.strategy-button {
    position: relative;
    left: 30px;
    width: 300px; /* 设置一个固定的宽度 */
    height: 50px;
    top:5px;
    background-color: #2fb1f2;
    
  } 
  .strategy-button:hover{
    background-color: #2650fb;
  }
</style>
  