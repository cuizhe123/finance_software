<template>
  <!-- 欢迎条幅 -->
  <div class="welcome-banner">
    <div class="top-value">欢 迎 来 到 金 霸 霸 量 化 交 易 平 台 !</div>
  </div>
    <div class="container">
        <!-- Logo 和 注册表单 -->
        <div class="header">
            <div class="logo-container">
                <img src="../../public/logo.jpg" alt="logo">
            </div>
            <div class="form-container">
                <h1>登录</h1>
                <form @submit.prevent="handleSubmit" class="form11">
                  <div class="form-group-container1">
                    <div class="form-group">
                      <label for="username">用户名:</label>
                      <input type="text" id="username" v-model="username" required autocomplete="off">
                    </div>
                    <div class="form-group">
                      <label for="password">密 码:&nbsp;</label>
                      <input type="password" id="password" v-model="password" required autocomplete="off">
                    </div>
                    <button @click="getInhomepage(username)" class="">登录</button>
                    <button class="forgot-password-button" @click="openforget">忘记密码？</button>
                    <forget v-if="forgetOpen" @close="closeforget" />
                  </div>
                  
                </form>                          
                <button @click="switchToRegister">切换为注册</button>
            </div>
        </div>

        <div v-if="errorMessage" class="error-message-box">
            <span class="error-message">{{ errorMessage }}</span>
        </div>
    </div>
</template>
  
<script>
import Forget from './pop-up-window/forget.vue';
export default {
    components: {
       Forget
    },
    data() {
        return {
            username: '',
            password: '',
            errorMessage: '',
            forgetOpen: false
        };
    },
    methods: {
        
        switchToRegister() {
          this.$emit('switchToRegister'); // 触发自定义事件
        },
        getInhomepage(username) {
          this.$emit('getInhomepage', username); // 触发自定义事件
        },
        openforget() {
            this.forgetOpen = true;
        },
        closeforget() {
            this.forgetOpen = false;
        },
    }
};
</script>
  
  <style>
  /* 页面容器样式 */
  .container {
    width: 100%; /* 填满整个页面宽度 */
    padding: 5px 150px; /* 垂直方向上填满剩余空间，水平方向上自动调整 */
    display: flex; /* 使用flex布局 */
    flex-direction: column; /* 垂直布局 */
    align-items: center; /* 水平居中 */
  }
  
  /* 欢迎条幅样式 */
  .welcome-banner {
    background-color: #4CAF50; /* 绿色背景 */
    color: white;
    padding: 40px 0;
    text-align: center;
    margin-bottom: 50px;
    width: 100%; /* 横幅宽度填满父容器 */
  }
  
  .header{
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .logo-container img {
    width: 300px; /* 调整logo图片宽度 */
    height: auto;
  }
  
  .form-container {
    margin-left: 250px; /* 增加左侧间距 */
    max-width: 600px; /* 设置最大宽度 */
    width: 100%; /* 宽度填满父容器 */
  }
  
  .form11 {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 90px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 400px;
    height:300px
  }
  
  .form-group-container1{
    position: relative;
    top:-40px;
    height: 100%;
  }
  .form-group {
    margin-bottom: 20px; /* 减少输入框与上下边界的距离 */
    display: flex;
    align-items: center;
  }  
  
  .form-group label {
    flex: 0 0 auto; /* 使标签的宽度根据内容自动调整 */
  }
  
  .form-group input {
    flex: 1;
    padding: 10px;
    box-sizing: border-box;
    margin-left: 10px; /* 添加左边距 */
  }
  
  .forgot-password-button {
    background-color: #ffffff; /* 白色背景 */
    color: #000000; /* 黑色字体 */
    border: none;
    border-bottom: 1px solid #808080; /* 灰色底边线 */
    cursor: pointer;
    margin-top: 20px; /* 调整与上方按钮的间距 */
    width: 150px;
  }

  .forgot-password-button:hover {
    background-color: #d3cbcb; /* 白色背景 */
  }

  button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    cursor: pointer;
    border-radius: 3px;
    display: block;
    margin: 0 auto;
    width: 100%; /* 填满整个页面宽度 */
    margin-top: 10px; /* 添加上边距 */
  }
  button:hover{
    background-color: #0f5eb3;
  }
  </style>
  