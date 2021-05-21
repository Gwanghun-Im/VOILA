<template>
    <div>
    <h1>Login</h1>
    <div>
      <label for="email">사용자 이름: </label>
      <input type="text" id="email" v-model="credentials.email">
    </div>
    <div>
      <label for="password">비번: </label>
      <input type="text" id="password" v-model="credentials.password"
      @keypress.enter="login(credentials)">
    </div>
    <button @click="login(credentials)">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        email: '',
        password: '',
      },
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/login/`, this.credentials)
      .then((res) => {
        console.log(res)
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login')
        this.$router.push({ name: 'Home' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>