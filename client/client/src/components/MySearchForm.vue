<template>
  <div>
    <input type="text" @keyup.enter="onInput" v-model = 'input_data' class="my-4" >
    <button @click="onInput" type="button" class="btn btn-primary mx-1" >Search</button>
    <p v-if="msg">{{msg}}</p>
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
      msg : ''
    }
  },
  methods: {
    onInput: function () {
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

</style>