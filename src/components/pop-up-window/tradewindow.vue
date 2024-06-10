<template>
    <div class="tradewindow">
        <button class="exit-button" @click="close">关闭</button>
        <form @submit.prevent="handleSubmit" class="form1">
            <p>您正在交易的证券名称为: {{ stockname }}</p>
            <p>证券代码为: {{ code }}</p>
            <p>当前价格为: {{ currentPrice }}</p>
            <p>请问您的操作为？</p>
        </form> 
        <div class="trade-button-container">
            <button class="trade-button1" @click="openbuyin">买入</button>
            <buyin v-if="buyin" :stockname="stockname" :code="code":username = "username" :currentPrice="currentPrice" @close="closebuyin" />
            <button class="trade-button2" @click="opensellout">卖出</button>
            <sellout v-if="sellout" :stockname="stockname" :code="code" :username = "username":currentPrice="currentPrice" @close="closesellout" />
        </div>
    </div>  
</template>
    
<script>
import axios from 'axios';
import buyin from './buyin.vue';
import sellout from './sellout.vue';

  export default {
    components: {
        buyin,
        sellout,
    },
    props: {
        code: {
            type: String,
            required: true
        },
        username:{
            type: String,
            required: true
        }
    },
    data() {
      return {
        stockname: '上证指数',  //股票名
        currentPrice: 10,  //价格
        buyin: false,
          sellout: false,
          market:['sh000001','sz399001','bj899050','sh000300']
      };
    },
    mounted() {
        this.Getstock();
    },
   
    methods: {
        close() {
            this.$emit('close');
        },
        openbuyin() {
            this.buyin = true;
            
        },
        closebuyin() {
            this.buyin = false;
        },
        opensellout() {
            this.sellout = true;
        },
        closesellout() {
            this.sellout = false;
        },
        async Getstock() {
          try {
                  const response = await axios.post('http://127.0.0.1:5000/stock/stock_mess', {
                      'code': this.code
                  });
                  
              const data = response.data;
              const stock = data.result;
              console.log(stock)
              if (stock != null) {
                if (this.market.includes(this.code)) {
                    this.stockname = stock.market_name; //股票名
                    this.currentPrice = stock.price;
                  }
                  else {
                    this.stockname = stock.stock_name; //股票名
                    this.currentPrice = stock.price
                  }
              }
              else {
                  // 显示错误消息

                }
          }
          catch (error) {
                  console.error('请求失败:', error);
                  // 显示通用错误消息
              }
        },
    },
  }
</script>
    
<style>
    .tradewindow {
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

      .trade-button-container {
        display: flex;
        justify-content: center; /* 水平居中对齐 */
        gap: 10px; /* 按钮之间的间距 */
    }
    
    .trade-button1 {
        position: absolute;
        background-color: rgb(13, 185, 13);
        color: black;
        font-size: 14px;
        padding: 5px 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100px; /* 或者根据需要调整按钮的宽度 */
        left:30%
    }
    .trade-button1:hover {
        background-color: rgb(8, 121, 8);
    }

    .trade-button2 {
        position: absolute;
        background-color: red;
        color: black;
        font-size: 14px;
        padding: 5px 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100px; /* 或者根据需要调整按钮的宽度 */
        left:58%
    }
    .trade-button2:hover {
        background-color: rgb(160, 14, 14);
    }
</style>
    