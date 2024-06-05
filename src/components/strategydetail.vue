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
  <button class="strategydetail-button" @click="getInstrategy(username)">返回</button>
  <!-- 第一行：策略标签 -->
  <div class="section1">
    <div class="section-label">策略{{this.index}}：</div>
    <div class="section-content">策略内容描述...</div>
  </div>

  <!-- 第二行：文字描述 -->
  <div class="section2">
    <div class="section-label">文字描述：</div>
    <div class="section-content">文字描述内容...</div>
  </div>

  <!-- 第三行：历史回测结果 -->
  <div class="section3">
    <div class="section-label">历史回测结果：</div>
  </div>
  <div class="section-content">
    <img src="../../logo.jpg" alt="历史回测结果">
  </div>

  <!-- 第四行：推荐股票表格 -->
  <div class="section4">
    <div class="section-label">推荐股票：</div>
    <div class="section-content">
      <table>
        <thead>
          <tr>
            <th>股票代码</th>
            <th>股票名称</th>
            <th>推荐理由</th>
          </tr>
        </thead>
        <tbody>
          <!-- 这里填充表格内容 -->
          <tr v-for="stock in recommendedStocks" :key="stock.code">
            <td>{{ stock.code }}</td>
            <td>{{ stock.name }}</td>
            <td >{{ stock.reason }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  </template>
  
  <script>
  export default {
    props: {
        index: {
            type: String,
            required: true
        },
        username: {
            type: String,
            required: true
        }
    },
    data() {
      return {
        recommendedStocks: [
          { code: '001', name: '股票一', reason: '理由一' },
          { code: '002', name: '股票二', reason: '理由二' },
          // 其他推荐股票...
        ]
      };
    },
    methods:{
      getInstrategy(username) {
            this.$emit('getInstrategy', username);
        },
    }
  };
  </script>
  
<style>
.strategydetail-button {
  position: absolute;
  top:12.6%;
  left:0;
  width:5%;
  flex: 1;
  border: 1px solid #000; /* 黑色细边框 */
  background-color: #0d8ced; /* 蓝色背景 */
  color: #ffffff; /* 白色字体 */
  cursor: pointer;
  padding: 0px 20px;
  font-size: 15px; /* 按钮字体大小 */
  outline: none;
  transition: background-color 0.3s ease;
  margin-top: 0; /* 删除按钮的顶部外边距 */
  padding-top: 0; /* 删除按钮的顶部内边距 */
  height: 50px; /* 增加按钮的高度 */
}

.strategydetail-button:hover{
  background-color: #0505a6; /* 蓝色背景 */
}

.section1 {
  position: absolute;
  background-color: #4cc3e0;
  padding: 14px 15px;
  border-radius: 5px;
  width: 400px; /* 设置一个固定的宽度 */
  height: 50px;
  top:20%;
  left: 30%;
  transform: translate(-50%, -50%);
  display: flex;
  margin-bottom: 20px; /* 调整各部分之间的间距 */
}

.section2 {
  position: absolute;
  background-color: #4cc3e0;
  padding: 14px 15px;
  border-radius: 5px;
  width: 400px; /* 设置一个固定的宽度 */
  height: 50px;
  top:20%;
  left: 60%;
  transform: translate(-50%, -50%);
  display: flex;
  margin-bottom: 20px; /* 调整各部分之间的间距 */
}

.section3 {
  position: absolute;
  background-color: #4cc3e0;
  padding: 14px 15px;
  border-radius: 5px;
  width: 150px; /* 设置一个固定的宽度 */
  height: 50px;
  top:30%;
  left: 10%;
  transform: translate(-50%, -50%);
  display: flex;
  margin-bottom: 20px; /* 调整各部分之间的间距 */
}

.section-content img {
  position: absolute;
  top: 45%;
  left: 30%;
  transform: translate(-50%, -50%);
  z-index: 1; 
  width: 300px; /* 调整logo图片宽度 */
}

.section4 {
  position: absolute;
  background-color: #4cc3e0;
  padding: 14px 15px;
  border-radius: 5px;
  width: 60%; /* 设置一个固定的宽度 */
  height: 20%;
  top:80%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  margin-bottom: 20px; /* 调整各部分之间的间距 */
}

.section-label {
  width: 150px; /* 设置标签的宽度 */
}

/* 表格样式 */
table {
  width: 100%;
  border-collapse: collapse;
}

td {
  padding: 8px;
  border: 1px solid #9c9a9a9a;
  background-color: #f2f2f2;
}

th {
   padding: 8px;
  border: 1px solid #3b3b3b9a;
  background-color: #57555542;
}
  </style>
  