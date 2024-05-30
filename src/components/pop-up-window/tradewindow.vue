<template>
    <div class="tradewindow">
        <button class="exit-button" @click="close">关闭</button>
        <form @submit.prevent="handleSubmit" class="form1">
            <p>您正在交易的证券代码是: {{ code }}</p>
            <div>{{ code }}</div>
        </form> 
        
    </div>  
</template>
    
<script>
  export default {
    props: {
        code: {
            type: String,
            required: true
        }
    },
    data() {
      return {
       
      };
    },
   
    methods: {
        close() {
            this.$emit('close');
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
    
</style>
    