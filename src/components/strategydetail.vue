<template>
  <div class="background-layer"></div>
  <div class="logo-container1">
    <img src="../../logo.jpg" alt="logo">
  </div>
  <div class="top-label">
    <div class="top-value">TradePulse —— 一站式A股量化交易平台</div>
    <div class="top-value1">祝您今日愉快！</div>
    <div class="top-value2">用户: {{ username }}</div>
  </div>
  <button class="strategydetail-button" @click="getInstrategy(username)">返回</button>
  <!-- 第一行：策略标签 -->
  <div class="section11">
    <div class="section-label">策略{{this.index}}：</div>
    <div class="section-content">{{strategyArray[this.index-1]}}</div>
  </div>
  <div class="section12">
    <div class="section-label">介绍{{this.index}}：</div>
    <div class="section-content">{{strategyArray1[this.index-1]}}</div>
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
  <div class="section31">
    <div class="section-label">历史回测结果：</div>
  </div>
  <div class="section-content1">
    <img v-if="index === 1" src="../../策略1SVM.png" alt="历史回测结果">
    <img v-if="index === 2" src="../../策略2RNN.png" alt="历史回测结果">
    <img v-if="index === 3" src="../../策略3LSTM.png" alt="历史回测结果">
    <img v-if="index === 4" src="../../策略4GRU.png" alt="历史回测结果">
    <img v-if="index === 5" src="../../meiyou.jpg" alt="历史回测结果">
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
            <th>股票代码</th>
            <th>股票名称</th>
          </tr>
        </thead>
        <tbody>
          <!-- 这里填充表格内容 -->
          <tr v-if="index === 1" v-for="stock in recommendedStocks1" :key="stock.code">
            <td>{{ stock.code1 }}</td>
            <td>{{ stock.name1 }}</td>
            <td>{{ stock.code2 }}</td>
            <td>{{ stock.name2 }}</td>
          </tr>
          <tr v-if="index === 2" v-for="stock in recommendedStocks2" :key="stock.code">
            <td>{{ stock.code1 }}</td>
            <td>{{ stock.name1 }}</td>
            <td>{{ stock.code2 }}</td>
            <td>{{ stock.name2 }}</td>
          </tr>
          <tr v-if="index === 3" v-for="stock in recommendedStocks3" :key="stock.code">
            <td>{{ stock.code1 }}</td>
            <td>{{ stock.name1 }}</td>
            <td>{{ stock.code2 }}</td>
            <td>{{ stock.name2 }}</td>
          </tr>
          <tr v-if="index === 4" v-for="stock in recommendedStocks4" :key="stock.code">
            <td>{{ stock.code1 }}</td>
            <td>{{ stock.name1 }}</td>
            <td>{{ stock.code2 }}</td>
            <td>{{ stock.name2 }}</td>
          </tr>
          <tr v-if="index === 5" v-for="stock in recommendedStocks5" :key="stock.code">
            <td>{{ stock.code1 }}</td>
            <td>{{ stock.name1 }}</td>
            <td>{{ stock.code2 }}</td>
            <td>{{ stock.name2 }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  </template>
  
  <script>
  import axios from 'axios';
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
            strategyArray: [
            '基于SVM的沪深300截面策略',
            '基于RNN的中低频收益率预测',
            '基于LSTM的中低频收益率预测',
            '基于GRU的中低频收益率预测',
            '集成xgb、catboost与贝叶斯回归的中低频收益率预测'
            ],
            strategyArray1: [
            '该模型选取2010-2022的月频数据,以沪深300作为股票池,通过支持向量机模型拟合基本面月频因子,对收益率进行预测并推荐当前预测收益率最高的10只股票',
            '该模型利用2017-2022年的数据,通过循环神经网络对基础行情因子进行拟合,对收益率进行预测并推荐当前预测收益率最高的10只股票',
            '该模型利用2017-2022年的数据,通过LSTM对基础行情因子进行拟合,对收益率进行预测并推荐当前预测收益率最高的10只股票',
            '该模型利用2017-2022年的数据,通过GRU对基础行情因子进行拟合,对收益率进行预测并推荐当前预测收益率最高的10只股票',
            '该模型利用2020-2022年的日频数据,通过对XGBoost,CatBoost和贝叶斯回归三种模型进行集成学习得到的模型,对20个日频因子进行拟合,对收益率进行预测并推荐当前预测收益率最高的10只股票。'
            ],
            dataTable: [
              [-0.028,-0.224,0.002,0.246,2.1,18.6],
              [-0.047,-0.381,0.003,0.211,3.499, 14.5],
              [-0.042,-0.364,0.002,0.236,2.635,17.1],
              [-0.055,-0.469,0.003,0.224,3.62,12.6],
              [0.058,-0.498,0.004,0.193,3.88,10.2]
            ],
            recommendedStocks1: [ 
              { code1: '600011', name1: '华能国际', code2: '601800', name2: '中国交建',},
              { code1: '600885', name1: '宏发股份', code2: '601872', name2: '招商轮船',},
              { code1: '600895', name1: '张江高科', code2: '600831', name2: '广电网络',},
              { code1: '688035', name1: '德邦科技', code2: '600031', name2: '三一重工',},
              { code1: '600016', name1: '民生银行', code2: '600216', name2: '浙江医药',},
            ],
            recommendedStocks2: [ 
              { code1: '000157', name1: '中联重科', code2: '600133', name2: '东湖高新',},
              { code1: '600032', name1: '浙江新能', code2: '601766', name2: '中国中车',},
              { code1: '601169', name1: '北京银行', code2: '002560', name2: '通达股份',},
              { code1: '601166', name1: '兴业银行', code2: '603099', name2: '长白山',},
              { code1: '603107', name1: '上海汽配', code2: '000972', name2: '中基健康',},
            ],
            recommendedStocks3: [
              { code1: '600133', name1: '东湖高新', code2: '603099', name2: '长白山',},
              { code1: '300488', name1: '恒锋工具', code2: '300222', name2: '科大智能',},
              { code1: '000157', name1: '中联重科', code2: '002283', name2: '天润工业',},
              { code1: '001219', name1: '青岛食品', code2: '603004', name2: '鼎龙科技',},
              { code1: '600032', name1: '浙江新能', code2: '600941', name2: '中国移动',},
            ],
            recommendedStocks4: [ 
              { code1: '300194', name1: '福安药业', code2: '002587', name2: '奥拓电子',},
              { code1: '600028', name1: '中国石化', code2: '002831', name2: '裕同科技',},
              { code1: '603087', name1: '甘李药业', code2: '603099', name2: '长白山',},
              { code1: '002059', name1: '云南旅游', code2: '000972', name2: '中基健康',},
              { code1: '301419', name1: '阿莱德', code2: '600872', name2: '中炬高新',},
            ],
            recommendedStocks5: [	
              { code1: '600011', name1: '博深股份', code2: '000651', name2: '格力电器',},
              { code1: '600719', name1: '大连热电', code2: '688128', name2: '中国电研',},
              { code1: '002642', name1: '荣联科技', code2: '002758', name2: '浙农股份',},
              { code1: '603031', name1: '安孚科技', code2: '300906', name2: '日月明',},
              { code1: '600329', name1: '	达仁堂', code2: '300122', name2: '智飞生物',},
            ],
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
  background-color: #7d7d7e; /* 蓝色背景 */
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
  background-color: #3c3c3c; /* 蓝色背景 */
}

.section11 {
  position: absolute;
  background-color: #626363;
  padding: 14px 15px;
  border-radius: 5px;
  width: 500px; /* 设置一个固定的宽度 */
  height: 80px;
  top:19%;
  left: 30%;
  transform: translate(-50%, -50%);
  display: flex;
  margin-bottom: 20px; /* 调整各部分之间的间距 */
  color: #f6f9f9;
}

.section12 {
  z-index:1 ;
  position: absolute;
  background-color: #878989;
  color: #f6f9f9;
  padding: 14px 15px;
  border-radius: 5px;
  width: 500px; /* 设置一个固定的宽度 */
  height: 130px;
  top:31%;
  left: 30%;
  transform: translate(-50%, -50%);
  display: flex;
  margin-bottom: 20px; /* 调整各部分之间的间距 */
}

.section2 {
  position: absolute;
  background-color: #808181;
  color: #050505;
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

.section31 {
  position: absolute;
  background-color: #8e8f90;
  color: #050505;
  padding: 14px 15px;
  border-radius: 5px;
  width: 150px; /* 设置一个固定的宽度 */
  height: 50px;
  top:48%;
  left: 8%;
  transform: translate(-50%, -50%);
  display: flex;
  margin-bottom: 20px; /* 调整各部分之间的间距 */
}

.section-content1 img {
  position: absolute;
  top: 70%;
  left: 35%;
  transform: translate(-50%, -50%);
  z-index: 1; 
  width: 700px; /* 调整logo图片宽度 */
}

.section4 {
  position: absolute;
  background-color: #a6a8a8;
  color: #050505;
  padding: 14px 15px;
  border-radius: 5px;
  width: 33%; /* 设置一个固定的宽度 */
  height: 40%;
  top:60%;
  left: 80%;
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
  