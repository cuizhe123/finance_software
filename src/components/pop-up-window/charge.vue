<template>
    <div class="charge">
        <button class="exit-button" @click="close">关闭</button>
        <div class="charge-container">
            <div class="cash-info">
                <span>您现在所持有的现金为：</span>
                <span>{{ cash }}</span>
            </div>
            <div class="input-wrapper">
                <label for="rechargeAmount">您要充值的金额为：</label>
                <input type="number" id="rechargeAmount" v-model.number="rechargeAmount" />
            </div>
            <button class="confirm-button" @click="confirmRecharge">确认充值</button>
        </div>
        
    </div>
</template>
  
<script>
import { errorMessages } from 'vue/compiler-sfc';
import axios from 'axios';
export default {
    props: {
      username: {
        type: String,
        required: true
        },
    },
    data() {
        return {
            cash: 10000, // 初始现金数
            rechargeAmount: 0, // 充值金额
            errorMessages: '',//错误信息
            password:''
        };
    },
    mounted() {
        this.GetMessage(this.username);
    },
    methods: {
        close() {
            this.$emit('close');
        },
        
        confirmRecharge() {
            if (this.rechargeAmount > 0) {
                console.log('进入');
                this.cash += this.rechargeAmount; // 增加现金
                this.rechargeAmount = 0; // 清空充值金额
                this.change_money()
          // 可以在这里触发事件通知父组件充值成功
            } else {
                alert('请输入有效的充值金额');
            }
        },

        async change_money() {
            console.log('进入change')
                try {
                    //将这3个参数传到后端
                    const response = await axios.post('http://127.0.0.1:5000/user/charge', {
                        'username': this.username,
                        'password': this.password,
                        'cash':this.cash
                    });
                    console.log('cash',this.cash)
                    const data = response.data; //data的数据结构，例如：{'result':True\Flase,'message':successful}
                    if (data.result) {
                        alert('充值成功');
                        // 修改成功
                        this.$emit('close');
                    } else {
                        this.errorMessage = data.message;
                    }
                    } catch (error) {
                    console.error('更改失败:', error);
                    this.errorMessage = '更改失败，请稍后再试';
                }
            
        },
        async GetMessage(user_name) {
          try {
            console.log(user_name);
            console.log(111);
                  // 发送异步请求到后端验证用户名和密码
                  const response = await axios.post('http://127.0.0.1:5000/user/by_name', {
                      'username': user_name
                  });
                  // 后端返回验证结果
                //成功的话，返回[user的信息,'successful']，失败的话返回[None,错误信息]
              const data = response.data;
              const user = data.user;
                // console.log(data.user.name)
              if (data.user != null) {
                  this.password = user.password
                  this.cash = user.money
                  //user的结构：{'id':0, 'name':0, 'password':0, 'question':0, 'answer':0, 'money':0}
                  } else {
                      // 显示错误消息
                      this.errorMessage = '用户名错误';
                  }
              } catch (error) {
                  console.error('请求失败:', error);
                  // 显示通用错误消息
                  this.errorMessage = '失败，请稍后重试';
              }
        },
    },
};
</script>
  
<style>
.charge {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgb(234, 232, 232);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 50%;
  max-height: 80vh;
  overflow-y: auto;
  height: 40%;
  padding: 0;
  z-index: 1;
}

.charge-container {
    position: relative;
    top: 30px;
    left: 50%;
    transform: translateX(-50%); /* 平移自身宽度的一半 */
    padding: 20px;
}

.cash-info {
    background-color: #a4a5a4; 
    border-radius: 5px; 
    padding: 20px; 
    margin-bottom: 50px;
    margin-left: 170px;
    width: 400px

}

.input-wrapper {
    background-color: #a4a5a4; 
    border-radius: 5px;
    padding: 20px; 
    margin-bottom: 30px;
    margin-left: 170px;
    width: 400px
}

.confirm-button {
  padding: 10px 20px;
  background-color: #6f7070;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 120px;
  
}

.confirm-button:hover {
  background-color: #292a2a;
}
</style>
