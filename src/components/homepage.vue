<template>
    <div class="background-layer"></div>
    <div class="logo-container1">
        <img src="../../logo.jpg" alt="logo">
    </div>
    <div class="logo-container2">
        <img src="../../xdd.jpg" alt="logo">
    </div>
    <div class="logo-container3">
        <img src="../../bbx.jpg" alt="logo">
    </div>
    <div class="top-label">
        <div class="top-value">欢 迎 来 到 金 霸 霸 量 化 交 易 平 台 ！您 的 最 佳 选 择 !</div>
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
        <information v-if="accountOpen" @close="closeaccount" />
    </div>
    <!-- 现金标签 -->
    <div class="user-info">
        <div class="info-label">金额:</div>
        <div class="info-value">{{ cash }}</div>
        <button class="info-button" @click="opencharge">充值金额</button>
        <charge v-if="chargeOpen" @close="closecharge" />
    </div>
    <!-- 持仓量标签 -->
    <div class="user-info">
        <div class="info-label">持仓量:</div>
        <div class="info-value">{{ holdings }}</div>
        <button class="info-button" @click="openmydetail">持仓详情</button>
        <mydetail v-if="mydetailOpen" @close="closemydetail" />
    </div>
    <div class="user-info">
        <div class="info-label1">交易历史</div>
        <button class="info-button" @click="openmyhistory">历史详情</button>
        <myhistory v-if="myhistoryOpen" @close="closemyhistory" />
    </div>
</template>

<script>
import Myhistory from './pop-up-window/myhistory.vue';
import Mydetail from './pop-up-window/mydetail.vue';
import Charge from './pop-up-window/charge.vue';
import Information from './pop-up-window/information.vue';
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
    methods: {
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
        },
        opencharge() {
            this.chargeOpen = true;
        },
        closecharge() {
            this.chargeOpen = false;
        },
        openaccount() {
            this.accountOpen = true;
        },
        closeaccount() {
            this.accountOpen = false;
        },
        openmyhistory() {
            this.myhistoryOpen = true;
        },
        closemyhistory() {
            this.myhistoryOpen = false;
        },
    },
    data() {
        return {
            
            cash: 10000, // 现金
            holdings: 10, // 持仓量

            mydetailOpen: false,
            chargeOpen: false,
            accountOpen: false,
            myhistoryOpen: false
        };
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
    background-color: #42b0eb; /* 设置标签的背景色 */
}

.top-value {
    position: absolute;
    top: 30px;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    font-size: 28px; /* 放大字体 */
    font-weight: bold; /* 加粗字体 */
}

.top-value1 {
    position: absolute;
    top: 10px;
    left: 92%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    font-size: 18px; /* 放大字体 */
    font-weight: bold; /* 加粗字体 */
}

.top-value2 {
    position: absolute;
    top: 50px;
    left: 92%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    font-size: 18px; /* 放大字体 */
    font-weight: bold; /* 加粗字体 */
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
    background-color: #007bff; /* 蓝色背景 */
}

.top-button {
    flex: 1;
    border: 1px solid #000; /* 黑色细边框 */
    background-color: #007bff; /* 蓝色背景 */
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
    background-color: #224a78; /* 蓝色背景 */
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
    background-color: #0056b3; /* 按钮悬停时的背景色 */
}

.user-info {
    position: relative;
    top: 80px;
    left: 50%;
    background-color: #4cc3e0;
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
    background-color: #0c97c2; 
    color: #fff;
    border: none;
    width: 120px;
    border-radius: 5px;
    cursor: pointer;
}
.info-button:hover {
    background-color: #0056b3; /* 按钮悬停时的背景色 */
}
</style>
  