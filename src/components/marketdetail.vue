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
    <div class="marketdetail-top-label">
        <div class="marketdetail-container">
            <button class="marketdetail-button" @click="getInmarket(username)">返回</button>
        </div>
        <div class="marketdetail-info-container">
            <div class="marketdetail-info">
                <div class="marketdetail-label">股票名称:</div>
                <div class="marketdetail-value">{{ stockname }}</div>
            </div>
            <div class="marketdetail-info">
                <div class="marketdetail-label">股票代码:</div>
                <div class="marketdetail-value">{{ code }}</div>
            </div>
        </div>
    </div>
    <div class="marketdetail-right-label1">
        <div class="market-index-container1">
            <div class="market-index" >
                当前价格: {{ currentPrice }}
            </div>
        </div>
        <div class="market-index-container1">
            <div class="market-index" :class="{ 'positive': changePercentage > 0, 'negative': changePercentage < 0 }">
                涨跌百分比: {{ changePercentage }}%
            </div>
        </div>      
    </div>
    
    <div class="marketdetail-right-label2">
        <div class="market-index-container2">
            <div class="market-index">
                今开: {{ todayOpen }}
            </div>
        </div>
        <div class="market-index-container2">
            <div class="market-index">
                昨收: {{ yesterdayClose }}
            </div>
        </div>
        <div class="market-index-container2">
            <div class="market-index">
                最高: {{ highest }}
            </div>
        </div>
        <div class="market-index-container2">
            <div class="market-index">
                最低: {{ lowest }}
            </div>
        </div>
        <div class="market-index-container2">
            <div class="market-index">
                总手数: {{ totalVolume }}
            </div>
        </div>
        <div class="market-index-container2">
            <div class="market-index">
                换手数: {{ turnoverRate }}
            </div>
        </div> 
    </div>

     <!-- 绘图区域 -->
     <div class="chart-container">
        <canvas id="stockChart"></canvas>
    </div>
  </template>
  
<script>
import axios from 'axios';
import { onMounted } from 'vue';
import { Chart, registerables } from 'chart.js';

import 'chartjs-adapter-date-fns';
Chart.register(...registerables);
export default {
    data() {
        return {
        stockname: '',  //股票名
        currentPrice: 0,
        changePercentage: 2,
        todayOpen: 0,
        yesterdayClose: 0,
        highest: 0,
        lowest: 0,
        totalVolume: 0,
        turnoverRate: 0,
            market: ['sh000001', 'sz399001', 'bj899050', 'sh000300'],
        history:[]
        };
    },
    props: {
        code: {
            type: String,
            required: true
        },
        username: {
            type: String,
            required: true
        }
    },
    mounted() {
        this.Getstock();
    },
    methods: {

        async Getstock() {
          try {
                  const response = await axios.post('http://127.0.0.1:5000/stock/stock_mess', {
                      'code': this.code
                  });
              const data = response.data;
              const stock = data.result;
              if (stock != null) {
                  //查找成功成功，进行跳转或其他操作
                  if (this.market.includes(this.code)) {
                      this.stockname= stock.market_name;  //股票名
                      this.currentPrice= stock.price;
                      this.changePercentage= stock.price_fluctuation;
                      this.todayOpen= stock.today_open;
                      this.yesterdayClose= stock.yesterday_end;
                      this.highest= stock.high_price;
                      this.lowest= stock.low_price;
                      this.totalVolume= stock.amplitude;
                      this.turnoverRate= 0;
                  }
                  else {
                    this.stockname= stock.stock_name;  //股票名
                      this.currentPrice= stock.price;
                      this.changePercentage= stock.up_down;
                      this.todayOpen= stock.today_open;
                      this.yesterdayClose= stock.yester_price;
                      this.highest= stock.high_price;
                      this.lowest= stock.low_price;
                      this.totalVolume= stock.amplitude;
                      this.turnoverRate= stock.turnover_ratio;
                  }
                  this.Gethistory();   
              }
              else {
                  // 显示错误消息
                  this.errorMessage = 'code错误';
                }
          }
          catch (error) {
                  console.error('请求失败:', error);
                  // 显示通用错误消息
                  this.errorMessage = '失败，请稍后重试';
              }
        },
        getInmarket(username) {
            this.$emit('getInmarket', username);
        },
        async Gethistory() {
          try {
                  const response = await axios.post('http://127.0.0.1:5000/stock/history', {
                      'code': this.code
                  });
              const data = response.data;
              const history = data.result;
              if (stock != null) {
                  //查找成功成功，进行跳转或其他操作
                  this.history = stock;
                  this.drawChart();
              }
              else {
                  // 显示错误消息
                  this.errorMessage = '该股票不存在';
                }
          }
          catch (error) {
                  console.error('请求失败:', error);
                  // 显示通用错误消息
                  this.errorMessage = '失败，请稍后重试';
              }
        },
        drawChart() {
            console.log('开始绘图')
            const ctx = document.getElementById('stockChart').getContext('2d');
            const labels = this.history.map(item => item.time);
            const data = this.history.map(item => item.close_price);

            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: '价格',
                        data: data,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        fill: false,
                        tension: 0.1
                    }]
                },
                options: {
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'day'
                            },
                            title: {
                                display: true,
                                text: '时间'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: '价格'
                            }
                        }
                    }
                }
            });
        }


    }
}
</script>
  
<style>
.marketdetail-top-label {
    position: absolute;
    top: 100px;
    left: 0;
    height: 100px; /* 设置标签的高度 */
    width: 100%; /* 宽度与父容器相同 */
    background-color: #3f9cce; /* 设置标签的背景色 */
}

.marketdetail-container {
    position: absolute; /* 设置相对定位 */
    top:20px;
    left: 0;
    height: 30px; /* 设置标签的高度 */
    width: 5%; /* 宽度与父容器相同 */
}

.marketdetail-button {
    flex: 1;
    border: 1px solid #000; /* 黑色细边框 */
    background-color: #007bff; /* 蓝色背景 */
    color: #ffffff; /* 白色字体 */
    cursor: pointer;
    padding: 10px 10px;
    font-size: 15px; /* 按钮字体大小 */
    outline: none;
    transition: background-color 0.3s ease;
    margin-top: 0; /* 删除按钮的顶部外边距 */
    padding-top: 0; /* 删除按钮的顶部内边距 */
    height: 50px; /* 增加按钮的高度 */
}

.marketdetail-info {
    position: relative;
    top: -30px;
    margin-right: 10px;
    background-color: #4cc3e0;
    padding: 20px 20px;
    margin: 50px auto;
    border-radius: 5px;
    width: 300px; /* 设置一个固定的宽度 */
  }
  
.marketdetail-info-container {
    position: absolute;
    left: 10%;
    display: flex; /* 使用 Flexbox 布局 */
    width: 60%;
}


.marketdetail-label {
    font-weight: bold;
    margin-left: -35px;
    display: inline-block; /* 将 info-label 设置为内联块元素 */
    width: 100px; /* 设置 info-label 的宽度 */
}
  
.marketdetail-value {
    display: inline-block; /* 将 info-value 设置为内联块元素 */
    margin-left: 20px; /* 添加左边距，使其位于 info-label 的右侧 */
    vertical-align: top; /* 垂直对齐方式为顶部对齐 */
}

.marketdetail-right-label1 {
    position: absolute;
    top: 100px;
    right: 0;
    height: 40%; /* 设置标签的高度 */
    width: 15%; /* 宽度与父容器相同 */
    background-color: #2b77ea; /* 设置标签的背景色 */
}

.marketdetail-right-label2 {
    position: absolute;
    top: 40%;
    right: 0;
    height: 100%; /* 设置标签的高度 */
    width: 15%; /* 宽度与父容器相同 */
    background-color: #594ef6; /* 设置标签的背景色 */
}

.market-index-container1 {
    position:relative;
    margin-top:50px;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    background-color: #7edf7b; 
    border-radius: 5px; 
    padding: 20px; 
    width: 80%;
    height: 30px
}

.market-index-container2 {
    position:relative;
    margin-top:35px;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    background-color: #7edf7b; 
    border-radius: 5px; 
    padding: 20px; 
    width: 80%;
    height: 30px
}

.market-index{
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    font-size: 13px; /* 放大字体 */
    font-weight: bold; /* 加粗字体 */
}
.positive {
    color: red; /* 涨幅为正时字体颜色为红色 */
}

.negative {
    color: green; /* 涨幅为负时字体颜色为绿色 */
}
.chart-container {
    position: absolute;
    top: 60%;
    left: 10%;
    width: 80%;
    height: 30%;
    background-color: #ffffff;
    border-radius: 5px;
    padding: 20px;
}
</style>
  