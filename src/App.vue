<template>
  <div class="app">
    <div v-if="currentComponent === 'register'">
      <Register @switchToLogin="switchToLogin" />
    </div>
    <div v-else-if="currentComponent === 'login'">
      <Login @switchToRegister="switchToRegister" @getInhomepage="getInhomepage" @getInmarket="getInmarket" @getIntrade="getIntrade" @getInstrategy="getInstrategy" @getInfactor="getInfactor" />
    </div>
    <div v-else-if="currentComponent === 'homepage'">
      <Homepage @getInmarket="getInmarket" @getIntrade="getIntrade" @getInstrategy="getInstrategy" @getInfactor="getInfactor" @switchToLogin="switchToLogin" />
    </div>
    <div v-else-if="currentComponent === 'market'">
      <Market @getInhomepage="getInhomepage" @getIntrade="getIntrade" @getInstrategy="getInstrategy" @getInfactor="getInfactor" @switchToLogin="switchToLogin" @goToMarketDetail="goToMarketDetail" />
    </div>
    <div v-else-if="currentComponent === 'trade'">
      <Trade @getInhomepage="getInhomepage" @getInmarket="getInmarket" @getInstrategy="getInstrategy" @getInfactor="getInfactor" @switchToLogin="switchToLogin" />
    </div>
    <div v-else-if="currentComponent === 'strategy'">
      <Strategy @getInhomepage="getInhomepage" @getInmarket="getInmarket" @getIntrade="getIntrade" @getInfactor="getInfactor" @switchToLogin="switchToLogin" />
    </div>
    <div v-else-if="currentComponent === 'factor'">
      <Factor @getInhomepage="getInhomepage" @getInmarket="getInmarket" @getIntrade="getIntrade" @getInstrategy="getInstrategy" @switchToLogin="switchToLogin" />
    </div>
    <div v-else-if="currentComponent === 'marketdetail'" :code="selectedCode">
      <MarketDetail  :code="selectedCode" @getInmarket="getInmarket" />
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

export default {
  components: {
    Register,
    Login,
    Homepage,
    Market,
    Trade,
    Strategy,
    Factor,
    MarketDetail
  },
  data() {
    return {
      currentComponent: 'homepage', // 初始显示组件
      selectedCode: '' // 用于存储选中的代码
    };
  },
  methods: {
    switchToLogin() {
      this.currentComponent = 'login'; // 切换为登录组件
    },
    switchToRegister() {
      this.currentComponent = 'register'; // 切换为注册组件
    },
    getInhomepage() {
      this.currentComponent = 'homepage';// 切换为主页面
    },
    getInmarket() {
      this.currentComponent = 'market';// 切换为市场行情
    },
    getIntrade() {
      this.currentComponent = 'trade';// 切换为模拟交易
    },
    getInstrategy() {
      this.currentComponent = 'strategy';// 切换为策略
    },
    getInfactor() {
      this.currentComponent = 'factor';// 切换为因子
    },
    goToMarketDetail(code) {
      this.currentComponent = 'marketdetail';// 切换为市场详细
      this.selectedCode = code; // 存储选中的代码
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
