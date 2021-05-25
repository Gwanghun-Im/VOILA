<template>
  <div id="login">
    <div class="box">
      <h1>Login</h1>
      <div>
        <input type="text" id="email" v-model="credentials.email" placeholder="email" >
        <input type="password" id="password" v-model="credentials.password" @keypress.enter="login(credentials)" placeholder="Password">
      </div>
      <input type="submit" class="login-button" @click="login(credentials)" value="Login">
    </div>
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
      e : '',
      KakaoLogin:`${SERVER_URL}/accounts/login/kakao/`
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/login/`, this.credentials)
      .then((res) => {
        if (res.data.message==='fail'){
          this.e = res.data.message
        } else {
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login',res.data.email)
          this.$router.push({ name: 'Home' })
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style scoped>

.login {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  width: 960px;
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
}

.box {
  width: 500px;
  padding: 40px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background: #191919;
  border-radius: 24px;
  text-align: center;
}

.box h1 {
  color: white;
  text-transform: uppercase;
  font-weight: 500;
}

.box input[type="text"],.box input[type="password"]{
  font-family: 'Roboto', sans-serif;
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #3498db;
  padding: 14px 10px;
  width:  200px;
  outline: none;
  color: #666666;
  background: #e6e6e6;
  border-radius: 24px;
  transition: 0.25s;
}

.box input[type="text"]:focus,.box input[type="password"]:focus{
  width: 280px;
  border: 2px solid #2ecc71;
}

.box input[type="submit"]{
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #2ecc71;
  padding: 14px 40px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
}

.box input[type="submit"]:hover{
  background: #2ecc71;
}

</style>