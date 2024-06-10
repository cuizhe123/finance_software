<template>
    <div class="answerquestion">
        <button class="exit-button" @click="close">关闭</button>
        <form  class="form1">
            <div class="form-group">问题：{{question}}</div>
            <div class="form-group">
                <label>答案:</label>
                <input type="text" v-model="myanswer" required autocomplete="off">
            </div>
        </form> 
        <button class="info-button1"  @click="is_the_answer_true">确认</button>
        <div v-if="!isanswer_right" class="error-message-box1">
            <span class="error-message1">回答错误</span>
        </div>
        
    </div>  
    <information v-if="informationOpen" :username="username" @close="closeinformation" />
</template>
    
<script>
import axios from 'axios';
import Information from './information.vue';
  export default {
    props: {
      username: {
        type: String,
        required: true
      },
    },
    components: {
        Information
    },
    data() {
      return {
        question: '',//得到了上一个组件传过来的username以此找对应的其他
        answer:'',
        myanswer:'',
        informationOpen: false,
        isanswer_right: true
      };
    },
    mounted() {
        this.getmessage()
    },
   
    methods: {
        close() {
            this.$emit('close');
        },
        openinformation() {
            this.informationOpen = true;
        },
        closeinformation() {
            this.informationOpen = false;
            this.$emit('close');
        },
        async getmessage(){
          try {
              const response = await axios.post('http://127.0.0.1:5000/user/by_name', {
                  'username': this.username
              });
              const data = response.data;
              const user = data.user;
            
              if (data.user != null) {
                  this.question = user.question;
                  this.answer = user.answer;
                  if (this.answer == this.myanswer) {
                    this.isanswer_right = true
                  }
              }
              else
              {
                      // 显示错误消息
                    this.isUsernameValid = false;
              }
          }
          catch (error) {
                  console.error('请求失败:', error);
                  // 显示通用错误消息
                  this.isUsernameValid = false;
              }
        
        },
        is_the_answer_true(){
            //和forget一样，有两个量，分别管报错标签和新窗口
            this.openinformation();
        }
    },
  }
</script>
    
<style>
.answerquestion {
    z-index: 2;
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