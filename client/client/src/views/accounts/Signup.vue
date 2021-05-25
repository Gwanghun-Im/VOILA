<template>
  <div>
    <div id="signup">
      <div class="box">
        <h1>Signup</h1>
        <div>
          <input type="text" id="username" v-model="credentials.username" placeholder="username">
          <input type="text" id="email" v-model="credentials.email" placeholder="email">
          <input type="password" id="password" v-model="credentials.password" placeholder="Password">
          <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" @keypress.enter="signup(credentials)" placeholder="passwordConfirmation">
        </div>
        <input type="submit" class="signup-button" @click="signup(credentials)" value="Signup">
      </div>
    </div>
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
        username:''
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


<style scoped>
.signup {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
}

.box {
  width: 500px;
  padding: 40px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background: #191919;
  text-align: center;
  border-radius: 24px;
}

.box h1 {
  color: white;
  text-transform: uppercase;
  font-weight: 500;
}

.box input[type="text"],.box input[type="password"]{
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