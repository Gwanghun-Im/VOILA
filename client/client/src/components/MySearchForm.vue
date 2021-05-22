<template>
  <div>
    <input type="text" @keyup.enter="onInput" v-model = 'input_data' class="my-4" >
    <button @click="onInput" type="button" class="btn btn-info mx-1" >Search</button>
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
    }
  },
  methods: {
    onInput: function () {
      axios.get(`${SERVER_URL}/movies/search/${this.input_data}`)
      .then((res) => {
        console.log(res)
        this.$emit('on-input',res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }

}
</script>

<style>

</style>