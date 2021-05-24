<template>
  <div>
    <button @click="profile">get</button>
    {{user}}
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'Profile',
  data: function () {
    return {
      user:''
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        }
      }
      console.log(token)
      return config
    },

    profile: function () {
      const config = this.setToken()
      console.log(config)
      axios.get(`${SERVER_URL}/accounts/profile/`,config)
      .then((res) => {
        console.log(res)
        this.user = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created:function (){
    this.profile()
  }
}
</script>

<style scoped>
</style>