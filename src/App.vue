<template>
  <div class="app">
    <div v-if="currentComponent === 'register'">
      <Register @switchToLogin="switchToLogin" />
    </div>
    <div v-else-if="currentComponent === 'login'">
      <Login @switchToRegister="switchToRegister" @getInhomepage="getInhomepage" @getInmarket="getInmarket" @getIntrade="getIntrade" @getInstrategy="getInstrategy" @getInfactor="getInfactor" />
    </div>
    <div v-else-if="currentComponent === 'homepage'" :username="myusername">
      <Homepage :username="myusername" @getInmarket="getInmarket" @getIntrade="getIntrade" @getInstrategy="getInstrategy" @getInfactor="getInfactor" @switchToLogin="switchToLogin" />
    </div>
    <div v-else-if="currentComponent === 'market'" :username="myusername">
      <Market :username="myusername" @getInhomepage="getInhomepage" @getIntrade="getIntrade" @getInstrategy="getInstrategy" @getInfactor="getInfactor" @switchToLogin="switchToLogin" @goToMarketDetail="goToMarketDetail" />
    </div>
    <div v-else-if="currentComponent === 'trade'" :username="myusername">
      <Trade :username="myusername" @getInhomepage="getInhomepage" @getInmarket="getInmarket" @getInstrategy="getInstrategy" @getInfactor="getInfactor" @switchToLogin="switchToLogin" />
    </div>
    <div v-else-if="currentComponent === 'strategy'" :username="myusername">
      <Strategy :username="myusername" @getInhomepage="getInhomepage" @getInmarket="getInmarket" @getIntrade="getIntrade" @getInfactor="getInfactor" @switchToLogin="switchToLogin" @goTostrategy="goTostrategy"/>
    </div>
    <div v-else-if="currentComponent === 'factor'" :username="myusername">
      <Factor :username="myusername" @getInhomepage="getInhomepage" @getInmarket="getInmarket" @getIntrade="getIntrade" @getInstrategy="getInstrategy" @switchToLogin="switchToLogin" @goTofactor="goTofactor"/>
    </div>
    <div v-else-if="currentComponent === 'marketdetail'" :code="selectedCode">
      <MarketDetail  :code="selectedCode" :username="myusername" @getInmarket="getInmarket" />
    </div>
    <div v-else-if="currentComponent === 'strategydetail'" :index="selectedindex">
      <Strategydetail  :index="selectedindex" :username="myusername" @getInstrategy="getInstrategy" />
    </div>
    <div v-else-if="currentComponent === 'factordetail'" :index="selectedindex">
      <Factordetail  :index="selectedindex" :username="myusername" @getInfactor="getInfactor" />
    </div>
  </div>
</template>

<script>

import Register from './components/register.vue';
import Login from './components/login.vue';
import Homepage from './components/homepage.vue';
import Market from './components/market.vue';
import Trade from './components/trade.vue';
import Strategy from './components/strategy.vue';
import Factor from './components/factor.vue';
import MarketDetail from './components/marketdetail.vue';
import Strategydetail from './components/strategydetail.vue';
import Factordetail from './components/factordetail.vue';

export default {
  components: {
    Register,
    Login,
    Homepage,
    Market,
    Trade,
    Strategy,
    Factor,
    MarketDetail,
    Strategydetail,
    Factordetail
  },
  data() {
    return {
      currentComponent: 'homepage', // 初始显示组件
      selectedCode: '', // 用于存储选中的代码
      selectedindex: '',
      myusername:'',//用户名，非常重要，每个页面都通过用户名来找到其他数据
    };
  },
  methods: {
    switchToLogin() {
      this.currentComponent = 'login'; // 切换为登录组件
    },
    switchToRegister() {
      this.currentComponent = 'register'; // 切换为注册组件
    },
    getInhomepage(username) {
      this.currentComponent = 'homepage';// 切换为主页面
      this.myusername = username;
    },
    getInmarket(username) {
      this.currentComponent = 'market';// 切换为市场行情
      this.myusername = username;
    },
    getIntrade(username) {
      this.currentComponent = 'trade';// 切换为模拟交易
      this.myusername = username;
    },
    getInstrategy(username) {
      this.currentComponent = 'strategy';// 切换为策略
      this.myusername = username;
    },
    getInfactor(username) {
      this.currentComponent = 'factor';// 切换为因子
      this.myusername = username;
    },
    goToMarketDetail(code,username) {
      this.currentComponent = 'marketdetail';// 切换为市场详细
      this.selectedCode = code; // 存储选中的代码
      this.myusername = username;
    },
    goTostrategy(index,username) {
      this.currentComponent = 'strategydetail';// 切换为市场详细
      this.selectedindex = index; // 存储选中的策略
      this.myusername = username;
    },
    goTofactor(index,username) {
      this.currentComponent = 'factordetail';// 切换为市场详细
      this.selectedindex = index; // 存储选中的策略
      this.myusername = username;
    }
  }
};
</script>

<style>
.app {
  text-align: center;
  padding: 20px;
}
</style>
