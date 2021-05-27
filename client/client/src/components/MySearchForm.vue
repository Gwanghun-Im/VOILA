<template>
  <div class="box">
    <div class="search-box mt-4">
      <input type="text" @keyup.enter="onInput" v-model = 'input_data' class="search-txt" placeholder = "search" >
      <i class="search-btn fas fa-search" @click="onInput"></i>
      <p class="text-white mt-5" v-if="msg">{{msg}}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MyListForm',
  data: function () {
    return {
      input_data: '',
      msg : '"초성게임"을 입력해 보세요.'
    }
  },
  methods: {
    onInput: function () {
      if (this.input_data === '초성게임'){
        this.$router.push({name:"Game"})
      } else if (this.input_data === '프로필'){
        this.$router.push({name:"Profile"})
      }
      axios.get(`${SERVER_URL}/movies/search/${this.input_data}`)
      .then((res) => {
        console.log(res.data)
        if (res.data.length === 0){
          console.log(`error`)
          this.msg = `${this.input_data}에 대한 검색결과가 존재하지 않습니다.`
          this.$emit('on-input',res.data)
          } else {
          this.$emit('on-input',res.data)
          this.msg = ''
        }
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }

}
</script>

<style scoped>
.box {
  display: flex;
  justify-content: center;
  margin-bottom: 3%;
}

.search-box{
  background: white;
  height: 40px;
  border-radius: 40px;
  padding : 10px;
  width: 500PX;
}

.search-btn{
  color: #e84118;
  float: right;
  /* top: 15%; */
  width: 40px;
  height: 20px;
  border-radius: 50%;
  background: white;
  display: flex;
  justify-content: center;
  align-items: center;  
}

.search-txt{
  border:none;
  background: none;
  outline: none;
  float: left;
  padding: 0;
  color: black;
  font-size: 16px;
  transition: 0.4s;
  line-height: 20px;
  width:300px;
}

</style>