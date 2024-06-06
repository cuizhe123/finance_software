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
        <h1>注册</h1>
        <form @submit.prevent="handleSubmit" class="form">
          <div class="form-group-container">
            <div class="form-group">
              <label for="username">用户名:</label>
              <input type="text" id="username" v-model="username" required @blur="validateUsername">
            </div>
            <div class="form-group">
              <label for="password"> 密 码 :&nbsp;</label>
              <input type="password" id="password" v-model="password" required @blur="validatePassword">
            </div>
            <div class="form-group">
              <label for="confirmPassword">确认密码:</label>
              <input type="password" id="confirmPassword" v-model="confirmPassword" required @blur="validateConfirmPassword">
            </div>
            <div class="form-group">
              <label for="question">密保问题:</label>
              <input type="question" id="question" v-model="question" required >
            </div> <div class="form-group">
              <label for="answer">密保答案:</label>
              <input type="answer" id="answer" v-model="answer" required >
            </div>
            <button type="submit" :disabled="!isFormValid">注册</button>
          </div>
          
        </form>
        <button @click="switchToLogin">切换为登录</button>
      </div>
    </div>
    
    <div v-if="!isUsernameValid && username && errorPriority === 'username'" class="error-message-box">
      <span class="error-message">用户名不符规则,只能由汉字,字母或数字构成,长度为3到8位</span>
    </div>
    <div v-if="!isPasswordValid && password && errorPriority === 'password'" class="error-message-box">
      <span class="error-message">密码不符规则,必须包含大小写字母和数字,且长度为8位到12位</span>
    </div>
    <div v-if="!isConfirmPasswordValid && confirmPassword && errorPriority === 'confirmPassword'" class="error-message-box">
      <span class="error-message">确认密码与密码不匹配</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: '', 
      question: '',
      answer:'',
      isPasswordValid: true,
      isUsernameValid: true,
      isConfirmPasswordValid: true,
      errorPriority: '' // 用于跟踪错误消息的优先级
    };
  },
  computed: {
    isFormValid() {
      return this.isPasswordValid && this.isUsernameValid && this.isConfirmPasswordValid;
    }
  },
  methods: {
    handleSubmit() {
      if (this.isFormValid) {
        // 这里可以提交表单数据到后端保存用户注册信息
        console.log('用户名:', this.username);
        console.log('密码:', this.password);
        // 清空表单数据
        this.username = '';
        this.password = '';
        this.confirmPassword = '';
        // 清空错误消息
      } 
    },
    validateUsername() {
      const regex = /^[a-zA-Z0-9\u4e00-\u9fa5]{3,8}$/;
      this.isUsernameValid = regex.test(this.username) || this.username === '';
      if (!this.isUsernameValid) {
        this.errorPriority = 'username';
      }else if (!this.isPasswordValid) {
        this.errorPriority = 'password';
      }else if (!this.isConfirmPasswordValid) {
        this.errorPriority = 'confirmPassword';
      }
    },
    validatePassword() {
      const regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z\d]{8,12}$/;
      this.isPasswordValid = regex.test(this.password) || this.password === '';
      if (!this.isPasswordValid) {
        this.errorPriority = 'password';
      }else  if (!this.isUsernameValid) {
        this.errorPriority = 'username';
      }else if (!this.isConfirmPasswordValid) {
        this.errorPriority = 'confirmPassword';
      }
    },
    validateConfirmPassword() {
      this.isConfirmPasswordValid = this.confirmPassword === this.password || this.confirmPassword === '';
      if (!this.isConfirmPasswordValid) {
        this.errorPriority = 'confirmPassword';
      }else if (!this.isPasswordValid) {
        this.errorPriority = 'password';
      }else  if (!this.isUsernameValid) {
        this.errorPriority = 'username';
      }
    }, 
    switchToLogin() {
      this.$emit('switchToLogin'); // 触发自定义事件
    }
  },
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
  position: absolute;
  background-color: #4CAF50; /* 绿色背景 */
  position: absolute;
  top: 0;
  left: 0;
  height: 100px; /* 设置标签的高度 */
  width: 100%; /* 宽度与父容器相同 */
}

.header {
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
  height: 100%;
}

.form {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 90px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 400px;
  height:450px
}

.form-group-container{
  position: relative;
  top:-60px;
  height: 100%;
}
.form-group {
  position: relative;
  margin-bottom: 20px;
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
  margin-top: 10px
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
  margin-top: -30px; /* 添加上边距 */
  margin-bottom: -30px; /* 添加上边距 */
}

.error-message-box {
  position: absolute;
  bottom: 6%;
  background-color: red; /* 设置背景为红色 */
  color: white; /* 设置字体为白色 */
  border-radius: 5px; /* 设置边框圆角 */
  padding: 10px; /* 添加内边距 */
}

.error-message {
  font-size: 14px;
  margin: 0; /* 移除默认外边距 */
}

</style>
