<template>
    <div class="container">
        <!-- 欢迎条幅 -->
        <div class="welcome-banner">
            <p>欢迎来到金霸霸量化交易平台</p>
        </div>
        <!-- Logo 和 注册表单 -->
        <div class="header">
            <div class="logo-container">
                <img src="../../public/logo.jpg" alt="logo">
            </div>
            <div class="form-container">
                <h1>登录</h1>
                <form @submit.prevent="handleSubmit" class="form">
                    <div class="form-group">
                        <label for="username">用户名:</label>
                        <input type="text" id="username" v-model="username" required>
                    </div>
                    <div class="form-group">
                        <label for="password">密 码:&nbsp;</label>
                        <input type="password" id="password" v-model="password" required>
                    </div>
                    <button @click="getInhomepage">登录</button>
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
export default {
    data() {
        return {
            username: '',
            password: '',
            errorMessage: ''
        };
    },
    methods: {
        async handleSubmit() {
            try {
                // 发送异步请求到后端验证用户名和密码
                const response = await axios.post('/api/login', {
                    username: this.username,
                    password: this.password
                });

                // 后端返回验证结果
                if (response.data.success) {
                    // 登录成功，进行跳转或其他操作
                    // 例如：this.$router.push('/dashboard');
                } else {
                    // 显示错误消息
                    this.errorMessage = '用户名或密码错误';
                }
            } catch (error) {
                console.error('登录请求失败:', error);
                // 显示通用错误消息
                this.errorMessage = '登录失败，请稍后重试';
            }
        },
        switchToRegister() {
          this.$emit('switchToRegister'); // 触发自定义事件
        },
        getInhomepage() {
          this.$emit('getInhomepage'); // 触发自定义事件
        }
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
  }
  
  .form {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 90px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .form-group {
    margin-bottom: 30px;
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
    margin-top: 20px; /* 添加上边距 */
  }
  </style>
  