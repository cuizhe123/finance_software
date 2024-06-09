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
    <button class="strategydetail-button" @click="getInfactor(username)">返回</button>
    <!-- 第一行：策略标签 -->
    <div class="section1">
      <div class="section-label">因子{{this.index}}:</div>
      <div class="section-content">{{factorArray[this.index-1]}}</div>
    </div>
  
    <!-- 第二行：文字描述 -->
    <div class="section2">
      <div class="section-label">指标说明：</div>
      <div class="section-content">
        <table>
          <thead>
              <tr>
                  <th>IC</th>
                  <th>ICIR</th>
                  <th>多头收益率</th>
                  <th>多头波动率</th>
                  <th>多头IR</th>
                  <th>多头最大回撤</th>
              </tr>
          </thead>
          <tbody>
              <tr>
                  <td>{{dataTable[this.index-1][0]}}</td>
                  <td>{{dataTable[this.index-1][1]}}</td>
                  <td>{{dataTable[this.index-1][2]}}</td>
                  <td>{{dataTable[this.index-1][3]}}</td>
                  <td>{{dataTable[this.index-1][4]}}</td>
                  <td>{{dataTable[this.index-1][5]}}</td>
              </tr>
            </tbody>
          </table>
      </div>
    </div>
  
    <!-- 第三行：历史回测结果 -->
    <div class="section3">
      <div class="section-label">历史回测结果：</div>
    </div>
    <div class="section-content">
      <img v-if="index === 1" src="../../1优加换手率UTR.png" alt="历史回测结果">
      <img v-if="index === 2" src="../../2cpv.png" alt="历史回测结果">
      <img v-if="index === 3" src="../../3PV_corr_std.png" alt="历史回测结果">
      <img v-if="index === 4" src="../../4量价相关性.png" alt="历史回测结果">
      <img v-if="index === 5" src="../../5理想反转因子.png" alt="历史回测结果">
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
          factorArray: [
            '优加换手率',
            '量价波动趋势',
            '量价波动性',
            '量价相关性',
            'ideal_reverse'
            ],
            dataTable: [
              [0.015, -0.265, 0.263, 0.194, 1.356, 28.1],
              [-0.01, -0.159, 0.481, 0.14, 3.433, 8.1],
              [-0.008, -0.094, 0.418, 0.145, 2.879, 9.8],
              [0.01, 0.139, 0.165, 0.193, 0.854, 27.1],
              [-0.007, -0.078, 0.102, 0.228, 0.445, 29.8]
            ]
        };
      },
      methods:{
        getInfactor(username) {
              this.$emit('getInfactor', username);
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
    width: 700px; /* 设置一个固定的宽度 */
    height: 120px;
    top:24%;
    left: 70%;
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
    top:45%;
    left: 12%;
    transform: translate(-50%, -50%);
    display: flex;
    margin-bottom: 20px; /* 调整各部分之间的间距 */
  }
  
  .section-content img {
    position: absolute;
    top: 65%;
    left: 40%;
    transform: translate(-50%, -50%);
    z-index: 1; 
    width: 700px; /* 调整logo图片宽度 */
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
    border: 1px solid #000; /* 设置边框颜色为黑色 */
    background-color: #f2f2f2;
  }

  th {
    padding: 8px;
    border: 1px solid #000; /* 设置边框颜色为黑色 */
    background-color: #57555542;
  }

    </style>