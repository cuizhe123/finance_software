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
        <div class="market-index">
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
    </div>
  
    <!-- 绘图区域 -->
    <div ref="chartContainer" class="chart-container"></div>
  </template>
  
  <script>
  import axios from 'axios';
  import Highcharts from 'highcharts/highstock';
  
  export default {
    data() {
      return {
        stockname: '', //股票名
        currentPrice: 0,
        changePercentage: 2,
        todayOpen: 0,
        yesterdayClose: 0,
        highest: 0,
        lowest: 0,
        totalVolume: 0,
        turnoverRate: 0,
        market: ['sh000001', 'sz399001', 'bj899050', 'sh000300'],
        history: []
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
            if (this.market.includes(this.code)) {
              this.stockname = stock.market_name;
              this.currentPrice = stock.price;
              this.changePercentage = stock.price_fluctuation;
              this.todayOpen = stock.today_open;
              this.yesterdayClose = stock.yesterday_end;
              this.highest = stock.high_price;
              this.lowest = stock.low_price;
              this.totalVolume = stock.amplitude;
              this.turnoverRate = 0;
            } else {
              this.stockname = stock.stock_name;
              this.currentPrice = stock.price;
              this.changePercentage = stock.up_down;
              this.todayOpen = stock.today_open;
              this.yesterdayClose = stock.yester_price;
              this.highest = stock.high_price;
              this.lowest = stock.low_price;
              this.totalVolume = stock.amplitude;
              this.turnoverRate = stock.turnover_ratio;
            }
            this.Gethistory();
          } else {
            this.errorMessage = 'code错误';
          }
        } catch (error) {
          console.error('请求失败:', error);
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
          if (history != null) {
            this.history = history;
            this.drawChart();
          } else {
            this.errorMessage = '该股票不存在';
          }
        } catch (error) {
          console.error('请求失败:', error);
          this.errorMessage = '失败，请稍后重试';
        }
      },
      drawChart() {
        const highPriceData = this.history.map(item => [new Date(item.time).getTime(), item.high_price]);
        const closePriceData = this.history.map(item => [new Date(item.time).getTime(), item.close_price]);
        const lowPriceData = this.history.map(item => [new Date(item.time).getTime(), item.low_price]);
  
        Highcharts.stockChart(this.$refs.chartContainer, {
          rangeSelector: {
            selected: 1
          },
          title: {
            text: '股票价格趋势'
          },
          tooltip: {
            split: true
          },
          xAxis: {
            type: 'datetime'
          },
          yAxis: {
            title: {
              text: '价格'
            }
          },
          series: [{
            name: '高价',
            data: highPriceData,
            tooltip: {
              valueDecimals: 2
            }
          }, {
            name: '收盘价',
            data: closePriceData,
            tooltip: {
              valueDecimals: 2
            }
          }, {
            name: '低价',
            data: lowPriceData,
            tooltip: {
              valueDecimals: 2
            }
          }]
        });
      }
    }
  };
  </script>
  
  <style scoped>
  .marketdetail-top-label {
    position: absolute;
    top: 100px;
    left: 0;
    height: 100px;
    width: 100%;
    background-color: #838485;
  }
  
  .marketdetail-container {
    position: absolute;
    top: 20px;
    left: 0;
    height: 30px;
    width: 5%;
  }
  
  .marketdetail-button {
    flex: 1;
    border: 1px solid #000;
    background-color: #5b5c5c;
    color: #ffffff;
    cursor: pointer;
    padding: 10px 10px;
    font-size: 15px;
    outline: none;
    transition: background-color 0.3s ease;
    margin-top: 0;
    padding-top: 0;
    height: 50px;
    top: -100px;
  }
  
  .marketdetail-button:hover {
    background-color: #252525;
  }
  .marketdetail-info {
    position: relative;
    top: -30px;
    margin-right: 10px;
    background-color: #515253;
    padding: 20px 20px;
    margin: 50px auto;
    border-radius: 5px;
    width: 300px;
  }
  
  .marketdetail-info-container {
    position: absolute;
    left: 10%;
    display: flex;
    width: 60%;
  }
  
  .marketdetail-label {
    font-weight: bold;
    margin-left: -35px;
    color: #fafafa;
    display: inline-block;
    width: 100px;
  }
  
  .marketdetail-value {
    display: inline-block;
    margin-left: 20px;
    color: #fafafa;
    vertical-align: top;
  }
  
  .marketdetail-right-label1 {
    position: absolute;
    top: 100px;
    right: 0;
    height: 40%;
    width: 15%;
    background-color: #a4a5a7;
  }
  
  .marketdetail-right-label2 {
    position: absolute;
    top: 40%;
    right: 0;
    height: 100%;
    width: 15%;
    background-color: #787779;
  }
  
  .market-index-container1 {
    position: relative;
    margin-top: 50px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #323332;
    border-radius: 5px;
    padding: 20px;
    width: 80%;
    height: 30px;
  }
  
  .market-index-container2 {
    position: relative;
    margin-top: 65px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #323332;
    border-radius: 5px;
    padding: 20px;
    width: 80%;
    height: 30px;
  }
  
  .market-index {
    position: absolute;
    top: 30%;
    left: 50%;
    color: #fafafa;
    transform: translateX(-50%);
    font-size: 13px;
    font-weight: bold;
    width: 80%;
  }
  .positive {
    color: red;
  }
  
  .negative {
    color: rgb(4, 197, 4);
  }
  .chart-container {
    position: absolute;
    top: 30%;
    left: 10%;
    width: 60%;
    height: 60%;
    background-color: #ffffff;
    border-radius: 5px;
    padding: 20px;
  }
  </style>
  