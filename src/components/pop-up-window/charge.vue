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

export default {
    data() {
        return {
            cash: 10000, // 初始现金数
            rechargeAmount: 0, // 充值金额
            errorMessages:''//错误信息
        };
    },
    methods: {
        close() {
            this.$emit('close');
        },
        
        confirmRecharge() {
            if (this.rechargeAmount > 0) {
                this.cash += this.rechargeAmount; // 增加现金
                this.rechargeAmount = 0; // 清空充值金额
          // 可以在这里触发事件通知父组件充值成功
            } else {
                alert('请输入有效的充值金额');
            }
        },

        async handleSubmit() {
            if (this.isFormValid) {
                // 这里可以提交表单数据到后端保存用户注册信息
                try {
                    //将这四个参数传到后端
                    const response = await axios.post('http://127.0.0.1:5000/user/charge', {
                        'username': this.username,
                        'password': this.password,
                        'cash':this.cash
                    });
                    const data = response.data; //data的数据结构，例如：{'result':True\Flase,'message':successful}
                    if (data.get('result')) {
                        alert('充值成功');
                        // 修改成功

                    
                    } else {
                        this.errorMessage = data.message;
                    }
                    } catch (error) {
                    console.error('更改失败:', error);
                    this.errorMessage = '更改失败，请稍后再试';
                }
                    
                // console.log('用户名:', this.username);
                // console.log('密码:', this.password);
                // 清空表单数据
                // this.password = '';
                // this.confirmPassword = '';
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
    background-color: #7edf7b; 
    border-radius: 5px; 
    padding: 20px; 
    margin-bottom: 50px;
    margin-left: 170px;
    width: 400px

}

.input-wrapper {
    background-color: #7edf7b; 
    border-radius: 5px;
    padding: 20px; 
    margin-bottom: 30px;
    margin-left: 170px;
    width: 400px
}

.confirm-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 120px;
  
}

.confirm-button:hover {
  background-color: #0056b3;
}
</style>
