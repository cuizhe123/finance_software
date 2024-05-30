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
            <button class="top-button" @click="getIntrade">模拟交易</button>
            <button class="top-button1">策略</button>
            <button class="top-button" @click="getInfactor">因子回测</button>
            <button class="top-button" @click="switchToLogin">退出账号</button>
        </div>
    </div>
  </template>
  
<script>
export default {
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
        
    }
}
</script>
  
<style>

</style>
  