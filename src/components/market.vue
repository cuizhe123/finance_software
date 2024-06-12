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
            <button class="top-button1">市场行情</button>
            <button class="top-button" @click="getIntrade(username)">模拟交易</button>
            <button class="top-button" @click="getInstrategy(username)">策略</button>
            <button class="top-button" @click="getInfactor(username)">因子回测</button>
            <button class="top-button" @click="switchToLogin">退出账号</button>
        </div>
    </div> 
    <div class="middle-buttons-container">
        <button class="index-button" @click="goToMarketDetail('sh000001',username)">
            <div class="button-label">上证指数</div>
            <div class="button-info">
                <div class="code">代码:sh000001</div>
                <div class="price">价格:{{ price001 }}</div>
                <div class="percentage">涨跌：{{change001}}%</div>
            </div>
        </button>
        <button class="index-button" @click="goToMarketDetail('sz399001',username)">
            <div class="button-label">深证成指</div>
            <div class="button-info">
                <div class="code">代码:sz399001</div>
                <div class="price">价格:{{price399}}</div>
                <div class="percentage">涨跌:{{change399}}%</div>
            </div>
        </button>
        <button class="index-button" @click="goToMarketDetail('bj899050',username)">
            <div class="button-label">北证50</div>
            <div class="button-info">
                <div class="code">代码:bj899050</div>
                <div class="price">价格:{{price899}}</div>
                <div class="percentage">涨跌:{{change899}}%</div>
            </div>
        </button>
        <button class="index-button" @click="goToMarketDetail('sh000300',username)">
            <div class="button-label">沪深300</div>
            <div class="button-info">
                <div class="code">代码:sh000300</div>
                <div class="price">价格:{{ price300 }}</div>
                <div class="percentage">涨跌：{{change300}}%</div>
            </div>
        </button>
    </div>
    <div class="search-container">
        <form @submit.prevent="Getstock" class="form2">
            <input type="text" class="search-container-input" v-model="searchQuery" @input="hideNotFoundMsg" @focus="isInputFocused = true" @blur="isInputFocused = false" placeholder="请输入证券代码" required>
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
            price399: 0, // 深证成指价格
            price899: 0, // 北证50价格
            price300: 0, // 沪深300价格
            change001: 0,
            change399: 0,
            change899: 0,
            change300: 0,
            code: 0,
            searchQuery: '', // 搜索框中的内容
            showNotFoundMsg: false, // 是否显示未找到代码的消息
            isInputFocused: false // 输入框是否聚焦的标志
        };
    },
    mounted() {
        this.Getmarketstock('sh000001');
        this.Getmarketstock('sz399001');
        this.Getmarketstock('bj899050');
        this.Getmarketstock('sh000300');
    },
    
    methods: {
        async Getstock() {
          try {
                  // 发送异步请求到后端验证用户名和密码
                  const response = await axios.post('http://127.0.0.1:5000/stock/stock_mess', {
                      'code': this.searchQuery.toString()
                  });
              const data = response.data;
              const stock = data.result;
            //   console.log('data', data);
            //   console.log('user', data.user);
                // console.log(data.user.name)
              if (stock != null) {
                  //查找成功成功，进行跳转或其他操作
                  this.goToMarketDetail(this.searchQuery.toString(), this.username);
                  this.searchQuery = '';
                this.showNotFoundMsg = false;
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
        async Getmarketstock(code) {
          try {
                  // 发送异步请求到后端验证用户名和密码
                  const response = await axios.post('http://127.0.0.1:5000/stock/stock_mess', {
                      'code': code
                  });
              const data = response.data;
              const stock = data.result;
            //   console.log('data', data);
            //   console.log('user', data.user);
                // console.log(data.user.name)
              if (stock != null) {
                  //查找成功成功，进行跳转或其他操作
                  if (code == 'sh000001')
              {
                  this.price001 = stock.price
                this.change001 = stock.price_fluctuation
              }
              if (code == 'sz399001')
              {
                  this.price399 = stock.price
                this.change399 = stock.price_fluctuation
              }
              if (code == 'bj899050')
              {
                  this.price899 = stock.price
                this.change899 = stock.price_fluctuation
              }
              if (code == 'sh000300')
              {
                  this.price300 = stock.price
                this.change300 = stock.price_fluctuation
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
    background-color: #a4a5a5; /* 按钮悬停时的背景色 */
    flex: 1; /* 自动填充剩余空间 */
    min-width: 120px; /* 设置按钮的最小宽度 */
    margin-right: 100px; /* 或者调整右侧外边距 */
}

.index-button:hover {
    background-color: #565757; /* 按钮悬停时的背景色 */
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
    top:150px;
    width: 130px; 
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    background-color: rgb(147, 147, 148);
}

.search-container-button:hover {
    background-color: rgb(78, 78, 79);
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
