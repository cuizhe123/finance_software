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
            <button class="top-button1">市场行情</button>
            <button class="top-button" @click="getIntrade(username)">模拟交易</button>
            <button class="top-button" @click="getInstrategy(username)">策略</button>
            <button class="top-button" @click="getInfactor(username)">因子回测</button>
            <button class="top-button" @click="switchToLogin">退出账号</button>
        </div>
    </div> 
    <div class="middle-buttons-container">
        <button class="index-button" @click="goToMarketDetail('000001',username)">
            <div class="button-label">上证指数</div>
            <div class="button-info">
                <div class="code">代码:000001</div>
                <div class="price">价格:XXXX</div>
                <div class="percentage">涨跌：+1.2%</div>
            </div>
        </button>
        <button class="index-button" @click="goToMarketDetail('399001',username)">
            <div class="button-label">深证指数</div>
            <div class="button-info">
                <div class="code">代码:399001</div>
                <div class="price">价格:XXXX</div>
                <div class="percentage">涨跌：-0.8%</div>
            </div>
        </button>
        <button class="index-button" @click="goToMarketDetail('399005',username)">
            <div class="button-label">北交指数</div>
            <div class="button-info">
                <div class="code">代码:399005</div>
                <div class="price">价格:XXXX</div>
                <div class="percentage">涨跌：+0.5%</div>
            </div>
        </button>
        <button class="index-button" @click="goToMarketDetail('000300',username)">
            <div class="button-label">沪深300</div>
            <div class="button-info">
                <div class="code">代码:000300</div>
                <div class="price">价格:XXXX</div>
                <div class="percentage">涨跌：-0.3%</div>
            </div>
        </button>
    </div>
    <div class="search-container">
        <form @submit.prevent="handleSubmit" class="form2">
            <input type="number" class="search-container-input" v-model.number="searchQuery" @input="hideNotFoundMsg" @focus="isInputFocused = true" @blur="isInputFocused = false" placeholder="请输入证券代码" required>
            <button type="submit" class="search-container-button">搜索</button>
        </form>
    </div>
    <div v-if="showNotFoundMsg" class="error-message-box2">
        <span class="error-message2">无法找到您要查找的证券代码</span>
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
    emits: ['getInhomepage', 'getIntrade', 'getInstrategy', 'getInfactor', 'switchToLogin', 'goToMarketDetail'],
    data() {
        return {
            
            price001: 0, // 上证指数价格
            price399: 0, // 深证指数价格
            price3995: 0, // 北交指数价格
            price300: 0, // 沪深300价格
            code: 0,
            searchQuery: '', // 搜索框中的内容
            securities: ['000001', '399001', '399005', '000300'], // 证券代号列表
            showNotFoundMsg: false, // 是否显示未找到代码的消息
            isInputFocused: false // 输入框是否聚焦的标志
        };
    },
    
    methods: {
        handleSubmit() {
            // 检查搜索的证券代码是否存在
            if (this.searchQuery !== '' && this.securities.includes(this.searchQuery.toString())) {
                const code = this.searchQuery.toString();
                
                // 调用父组件方法跳转到市场详情页面
                this.goToMarketDetail(code,this.username);
               
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
        goToMarketDetail(code,username) {
            this.$emit('goToMarketDetail', code, username);
        }
        
    }
}
</script>
  
<style>
.middle-buttons-container {
    position: absolute;
    top:30%;
    display: flex;
    justify-content: center; /* 水平居中 */
    transform: translateX(-42%); /* 平移自身宽度的一半 */
}

.index-button {
    flex: 1; /* 自动填充剩余空间 */
    min-width: 120px; /* 设置按钮的最小宽度 */
    margin-right: 100px; /* 或者调整右侧外边距 */
}

.index-button:hover {
    background-color: #0056b3; /* 按钮悬停时的背景色 */
}

.button-label {
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.button-info {
    margin-top: 5px;
}

.search-container {
    position: absolute;
    top:50%;
    width:30%;
    height:50%;
    display: flex;
    justify-content: center; /* 水平居中 */
    transform: translateX(-44%); /* 平移自身宽度的一半 */
}
  
.form2 {
    border: 1px solid #727171;
    background-color: aliceblue;
    border-radius: 5px;
    padding: 30px; /* 减小内边距以缩小表单 */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 100%; /* 设置表单宽度为50%，居中显示 */
    height: 50%;
    margin: 6% auto 0; /* 上边距设置为6%，使用auto水平居中 */
    display: flex; /* 使用Flex布局 */
    flex-direction: column; /* 垂直布局 */
    justify-content: center; /* 在垂直方向上居中 */
    align-items: center; /* 在水平方向上居中 */
}

.search-container-input {
    position: absolute;
    top:70px;
    margin-right: 10px; /* 调整右侧外边距 */
    padding: 8px; /* 添加内边距 */
    border: 1px solid #1e1c1c; /* 添加边框 */
    border-radius: 4px; /* 添加圆角 */
    height:50px !important;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
}
  
.search-container-button {
    position: absolute;
    top:120px;
    width: 130px; 
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
}

.search-container-button:hover {
    background-color: rgb(25, 42, 227);
}
.error-message-box2 {
    position: absolute; /* 设置报错信息框为绝对定位 */
    bottom: 150px; /* 距离浮窗容器底部的距离为0 */
    background-color: red; /* 设置背景为红色 */
    color: white; /* 设置字体为白色 */
    border-radius: 5px; /* 设置边框圆角 */
    padding: 10px; /* 添加内边距 */
    margin-bottom: 10px;
    top:85%;
    height:5%;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
}

.error-message2 {
    font-size: 14px;
    margin: 0; /* 移除默认外边距 */
}
</style>
