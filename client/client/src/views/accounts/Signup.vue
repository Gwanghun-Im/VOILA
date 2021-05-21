<template>
  <div>
    <h1>Signup</h1>
    <p>{{e}}</p>
    <div>
      <label for="email">사용자 이름: </label>
      <input type="email" id="email" v-model="credentials.email">
    </div>
    <div>
      <label for="password">비번: </label>
      <input type="text" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비번 확인: </label>
      <input type="text" id="passwordConfirmation" v-model="credentials.passwordConfirmation"
      @keypress.enter="signup(credentials)">
    </div>
    <button @click="signup(credentials)">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        email: '',
        password: '',
        passwordConfirmation: '',
      },
      e:''
    }
  },
  methods: {
    signup: function (credentials) {
      axios.post(`${SERVER_URL}/accounts/signup/`, credentials)
      .then(res => {
        console.log(res)
        if (res.data.error) {
          this.e = res.data.error
        }
        else {
          this.$router.push({name:'Login'})
        }
      })
      .catch(e => {
        console.log(e)
      })
    }
  }
}
</script>