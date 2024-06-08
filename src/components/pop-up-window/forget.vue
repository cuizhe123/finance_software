<template>
    <div class="forget">
        <button class="exit-button" @click="close">关闭</button>
        <form  class="form1">
            <div class="form-group">
                <label for="username">您的用户名:</label>
                <input type="text" id="username" v-model="username" required autocomplete="off">
            </div>
        </form> 
        <button class="info-button1"  @click="findusername">确认</button>
        <div v-if="!isUsernameValid" class="error-message-box1">
            <span class="error-message1">找不到该用户名</span>
        </div>
        
    </div>  
    <answerquestion v-if="answerquestionOpen" :username="username" @close="closeanswerquestion" />
</template>
    
<script>
  import Answerquestion from './answerquestion.vue';
  export default {
    components: {
        Answerquestion
    },
    data() {
      return {
        username: '',
        isUsernameValid: true,
        answerquestionOpen: false
      };
    },
    methods: {
        close() {
            this.$emit('close');
        },
        openanswerquestion() {
            this.answerquestionOpen = true;
        },
        closeanswerquestion() {
            this.answerquestionOpen = false;
        },
        findusername(){
            //找有没有对应的用户名，有对应的返回answerquestionOpen是true,isUsernameValid为true,没有则都为false
            //之所以设置两个变量，因为平时isUsernameValid为true才没有错误标签，平时answerquestionOpen为false
            //true则跳转
            this.openanswerquestion();
        }
    },
  }
</script>
    
<style>
    .forget {
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
    