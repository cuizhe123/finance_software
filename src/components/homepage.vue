<template>
    <div class="background-layer"></div>
    <div class="logo-container1">
        <img src="../../logo.jpg" alt="logo">
    </div>
    
    <div class="top-label">
        <div class="top-value">TradePulse —— 一站式A股量化交易平台</div>
        <div class="top-value1">祝您今日愉快！</div>
        <div class="top-value2">用户: {{ this.username }}</div>
    </div>
    <div class="top-buttons-container">
        <div class="top-buttons">
            <button class="top-button1">首页</button>
            <button class="top-button" @click="getInmarket(username)">市场行情</button>
            <button class="top-button" @click="getIntrade(username)">模拟交易</button>
            <button class="top-button" @click="getInstrategy(username)">策略</button>
            <button class="top-button" @click="getInfactor(username)">因子回测</button>
            <button class="top-button" @click="switchToLogin">退出账号</button>
        </div>
    </div>
    
    <div class="user-info">
        <div class="info-label">用户名:</div>
        <div class="info-value">{{ username }}</div>
        <button class="info-button" @click="openaccount">账户设置</button>
        <information v-if="accountOpen" :username="username" @close="closeaccount" />
    </div>
    <!-- 现金标签 -->
    <div class="user-info">
        <div class="info-label">金额:</div>
        <div class="info-value">{{ cash }}</div>
        <button class="info-button" @click="opencharge">充值金额</button>
        <charge v-if="chargeOpen" :username="username" @close="closecharge" />
    </div>
    <!-- 持仓量标签 -->
    <div class="user-info">
        <div class="info-label">持仓量</div>
        <div class="info-value">{{ stock_value }}</div>
        <button class="info-button" @click="openmydetail">持仓详情</button>
        <mydetail v-if="mydetailOpen" :username="username" @close="closemydetail" />
    </div>
    <div class="user-info">
        <div class="info-label1">交易历史</div>
        <button class="info-button" @click="openmyhistory">历史详情</button>
        <myhistory v-if="myhistoryOpen" :username="username" @close="closemyhistory" />
    </div>
</template>

<script>
import Myhistory from './pop-up-window/myhistory.vue';
import Mydetail from './pop-up-window/mydetail.vue';
import Charge from './pop-up-window/charge.vue';
import Information from './pop-up-window/information.vue';
import axios from 'axios';
export default {
    props: {
        username: {
            type: String,
            required: true
        }
    },
    components: {
        Myhistory,
        Mydetail,
        Charge,
        Information
    },
    emits: ['getInhomepage', 'getInmarket', 'getIntrade', 'getInstrategy', 'getInfactor', 'switchToLogin'],
    methods: {
        async GetMessage(user_name) {
          try {
                  // 发送异步请求到后端验证用户名和密码
                  const response = await axios.post('http://127.0.0.1:5000/user/by_name', {
                      'username': user_name
                  });
                  // 后端返回验证结果
                //成功的话，返回[user的信息,'successful']，失败的话返回[None,错误信息]
              const data = response.data;
              const user = data.user;
            //   console.log('data', data);
            //   console.log('user', data.user);
                // console.log(data.user.name)
              if (data.user != null) {
                  this.cash = user.money;
                    //登录成功，进行跳转或其他操作
                      //user的结构：{'id':0, 'name':0, 'password':0, 'question':0, 'answer':0, 'money':0}
                  } else {
                      // 显示错误消息
                      this.errorMessage = '用户名或密码错误';
                  }
              } catch (error) {
                  console.error('请求失败:', error);
                  // 显示通用错误消息
                  this.errorMessage = '失败，请稍后重试';
              }
        },
        async getmystockvalue(user_name) {
            // 这里可以提交表单数据到后端保存用户注册信息
                try {
                    //将这四个参数传到后端
                    const response = await axios.post('http://127.0.0.1:5000/user/mystock', {
                        'username': user_name,
                    });
                    const data = response.data; //data的数据结构，[{'name': ,'code': ,'price': ,'quantity': },{...},{...}]
                    const my_stock = data.result;//[{'name': ,'code': ,'price': ,'quantity': },{...},{...}]
                    if(my_stock != null) {
                        for (let i = 0; i < my_stock.length; i++)
                        {
                            let stock = my_stock[i];
                            try {
                                //将这四个参数传到后端
                                const response2 = await axios.post('http://127.0.0.1:5000/stock/stock_mess', {
                                    'code': stock.code
                                });
                                const stock_now = response2.data.result;
                                this.stock_value += stock.quantity * stock_now.price;
                                console.log(this.stock_value)
                            }
                            catch (error) {
                                console.error('查看股票信息失败:', error);
                                this.errorMessage = '查看股票信息失败，请稍后再试';
                            }
                        }
                    }
                    else {
                        this.stock_value = 0;
                    }
                }
                catch (error) {
                  console.error('查看持仓失败:', error);
                    this.errorMessage = '查看持仓失败，请稍后再试';
                }
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
        openmydetail() {
            this.mydetailOpen = true;
        },
        closemydetail() {
            this.mydetailOpen = false;
            this.GetMessage(this.username);
        },
        opencharge() {
            this.chargeOpen = true;
        },
        closecharge() {
            this.chargeOpen = false;
            this.GetMessage(this.username);
        },
        openaccount() {
            this.accountOpen = true;
        },
        closeaccount() {
            this.accountOpen = false;
            this.GetMessage(this.username);
        },
        openmyhistory() {
            this.myhistoryOpen = true;
        },
        closemyhistory() {
            this.myhistoryOpen = false;
            this.GetMessage(this.username);
        },
    },
    data() {
        return {
            cash: 0, // 现金
            holdings: 10, // 持仓量
            mydetailOpen: false,
            chargeOpen: false,
            accountOpen: false,
            myhistoryOpen: false,
            stock_value: 0,
        };
    },
    mounted() {
        this.GetMessage(this.username);
        this.getmystockvalue(this.username);
    }
}
</script>
  
<style>
.background-layer::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('../../public/background.jpg'); /* 相对于 CSS 文件的路径 */
    background-size: cover;
    z-index: -1;
  }      

.logo-container1 img {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1; 
    width: 99px; /* 调整logo图片宽度 */
   
  }
  .logo-container2 img {
    position: absolute;
    top: 170px;
    left: 0;
    width: 355px; /* 调整logo图片宽度 */
   
  }
  .logo-container3 img {
    position: absolute;
    top: 170px;
    right: 0;
    width: 355px; /* 调整logo图片宽度 */
   
  }
.top-label {
    position: absolute;
    top: 0;
    left: 0;
    height: 100px; /* 设置标签的高度 */
    width: 100%; /* 宽度与父容器相同 */
    background-color: #000a0f; /* 设置标签的背景色 */
}

.top-value {
    position: absolute;
    top: 30px;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    font-size: 28px; /* 放大字体 */
    font-weight: bold; /* 加粗字体 */
    color: #ffffff; /* 白色字体 */
}

.top-value1 {
    position: absolute;
    top: 10px;
    left: 92%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    font-size: 18px; /* 放大字体 */
    font-weight: bold; /* 加粗字体 */
    color: #ffffff; /* 白色字体 */
}

.top-value2 {
    position: absolute;
    top: 50px;
    left: 92%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    font-size: 18px; /* 放大字体 */
    font-weight: bold; /* 加粗字体 */
    color: #ffffff; /* 白色字体 */
}

.top-buttons-container {
    position: absolute; /* 设置相对定位 */
    top:100px;
    left: 0;
    height: 100px; /* 设置标签的高度 */
    width: 100%; /* 宽度与父容器相同 */
}

.top-buttons {
    position: absolute; 
    width: 100%;
    display: flex;
    background-color: #999a9b; /* 灰色背景 */
}

.top-button {
    flex: 1;
    border: 1px solid #000; /* 黑色细边框 */
    background-color: #979798; /* 蓝色背景 */
    color: #ffffff; /* 白色字体 */
    cursor: pointer;
    padding: 10px 10px;
    font-size: 18px; /* 按钮字体大小 */
    outline: none;
    transition: background-color 0.3s ease;
    margin-top: 0; /* 删除按钮的顶部外边距 */
    padding-top: 0; /* 删除按钮的顶部内边距 */
    height: 70px; /* 增加按钮的高度 */
}

.top-button1 {
    flex: 1;
    border: 1px solid #000; /* 黑色细边框 */
    background-color: #404142; 
    color: #ffffff; /* 白色字体 */
    cursor: pointer;
    padding: 10px 10px;
    font-size: 18px; /* 按钮字体大小 */
    outline: none;
    transition: background-color 0.3s ease;
    margin-top: 0; /* 删除按钮的顶部外边距 */
    padding-top: 0; /* 删除按钮的顶部内边距 */
    height: 70px; /* 增加按钮的高度 */
}

.top-button:hover {
    background-color: #333434; /* 按钮悬停时的背景色 */
}
.top-button1:hover {
    background-color: #404142; 
}
.user-info {
    position: relative;
    top: 80px;
    left: 50%;
    background-color: #858586;
    padding: 20px 20px;
    margin: 50px auto;
    border-radius: 5px;
    width: 300px; /* 设置一个固定的宽度 */
  }
  
.info-label {
    font-weight: bold;
    margin-left: -35px;
    display: inline-block; /* 将 info-label 设置为内联块元素 */
    width: 100px; /* 设置 info-label 的宽度 */
}
  
.info-label1 {
    font-weight: bold;
    margin-left: 0px;
    display: inline-block; /* 将 info-label 设置为内联块元素 */
    width: 100px; /* 设置 info-label 的宽度 */
}
.info-value {
    display: inline-block; /* 将 info-value 设置为内联块元素 */
    margin-left: 20px; /* 添加左边距，使其位于 info-label 的右侧 */
    vertical-align: top; /* 垂直对齐方式为顶部对齐 */
}

.info-button {
    margin-left: 70px;
    padding: 5px 10px;
    background-color: #a8aaaa; 
    color: #fff;
    border: none;
    width: 120px;
    border-radius: 5px;
    cursor: pointer;
}
.info-button:hover {
    background-color: #383839; /* 按钮悬停时的背景色 */
}
</style>
  