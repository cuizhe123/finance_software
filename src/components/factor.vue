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
            <button class="top-button" @click="getIntrade(username)">模拟交易</button>
            <button class="top-button"@click="getInstrategy(username)">策略</button>
            <button class="top-button1">因子回测</button>
            <button class="top-button" @click="switchToLogin">退出账号</button>
        </div>
    </div>
    <div class="strategy-container" v-for="index in 5" :key="index">
        <div class="strategy-label">因子 {{ index }}</div>
        <button class="strategy-button" @click="goTofactor(index,username)"> {{ factorArray[index-1] }}</button>
    </div>
  </template>
  
<script>
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
            factorArray: [
            '优加换手率',
            '量价波动趋势',
            '量价波动性',
            '量价相关性',
            'ideal_reverse'
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
        goTofactor(index,username) {
            this.$emit('goTofactor', index, username);
        }
    }
}
</script>
  
<style>

</style>
  