<template>
    <div class="information">
        <button class="exit-button" @click="close">关闭</button>
        <form @submit.prevent="handleSubmit" class="form1">
            <div class="new-password">
                <label for="password"> 新密码 :</label>
                <input type="password" id="password" v-model="password" required @blur="validatePassword">
            </div>
            <div class="new-password">
                <label for="confirmPassword">确认密码:</label>
                <input type="password" id="confirmPassword" v-model="confirmPassword" required @blur="validateConfirmPassword">
            </div>
            
        </form> 
        <button class="info-button1" type="submit" :disabled="!isFormValid">更改密码</button>
        <div v-if="!isPasswordValid && password && errorPriority === 'password'" class="error-message-box1">
            <span class="error-message1">密码不符规则,必须包含大小写字母和数字,且长度为8位到12位</span>
        </div>
        <div v-if="!isConfirmPasswordValid && confirmPassword && errorPriority === 'confirmPassword'" class="error-message-box1">
            <span class="error-message1">确认密码与密码不匹配</span>
        </div>
    </div>  
</template>
    
<script>
  export default {
    data() {
      return {
        password: '',
        confirmPassword: '', 
        isPasswordValid: true,
        isConfirmPasswordValid: true,
        errorPriority: '' // 用于跟踪错误消息的优先级
      };
    },
    computed: {
        isFormValid() {
            return this.isPasswordValid && this.isConfirmPasswordValid;
    }
    },
    methods: {
        close() {
            this.$emit('close');
        },
        handleSubmit() {
            if (this.isFormValid) {
                // 这里可以提交表单数据到后端保存用户注册信息
                console.log('用户名:', this.username);
                console.log('密码:', this.password);
                // 清空表单数据
                this.password = '';
                this.confirmPassword = '';
            } 
        },
        validatePassword() {
            const regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z\d]{8,12}$/;
            this.isPasswordValid = regex.test(this.password) || this.password === '';
            if (!this.isPasswordValid) {
                this.errorPriority = 'password';
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
            }
        }, 
    },
  }
</script>
    
<style>
    .information {
        z-index: 1;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgb(244, 235, 235);
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 50%;
        max-height: 80vh;
        overflow-y: auto;
        height: 40%;
        padding: 0;
      }
    
      .form1 {
        border: 1px solid #727171;
        border-radius: 5px;
        padding: 30px; /* 减小内边距以缩小表单 */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        width: 50%; /* 设置表单宽度为50%，居中显示 */
        height: 50%;
        margin: 6% auto 0; /* 上边距设置为6%，使用auto水平居中 */
        display: flex; /* 使用Flex布局 */
        flex-direction: column; /* 垂直布局 */
        justify-content: center; /* 在垂直方向上居中 */
        align-items: center; /* 在水平方向上居中 */
    }

    .new-password {
        display: flex;
        align-items: center;
        margin-bottom: 20px; /* 增大行与行之间的间距 */
    }
    
    .new-password label {
        flex: 0 0 auto;
        margin-right: 10px;
    }
    
    .info-button1 {
        position: absolute;
        padding: 5px 10px;
        background-color: #0c97c2; 
        color: #fff;
        border: none;
        width: 120px;
        border-radius: 5px;
        cursor: pointer;
        left: 50%;
        transform: translateX(-50%); /* 平移自身宽度的一半 */
    }
    .info-button1:hover {
        background-color: #0056b3; /* 按钮悬停时的背景色 */
    }

    .error-message-box1 {
        position: absolute; /* 设置报错信息框为绝对定位 */
        bottom: 0; /* 距离浮窗容器底部的距离为0 */
        background-color: red; /* 设置背景为红色 */
        color: white; /* 设置字体为白色 */
        border-radius: 5px; /* 设置边框圆角 */
        padding: 10px; /* 添加内边距 */
        margin-bottom: 10px;
        left: 50%;
        transform: translateX(-50%); /* 平移自身宽度的一半 */
    }
    
    .error-message1 {
        font-size: 14px;
        margin: 0; /* 移除默认外边距 */
    }
    
</style>
    