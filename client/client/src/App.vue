<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{name:'Home'}">Home</router-link> |
      <span v-if="login">
        <router-link :to="{name: 'MyMovieList'}">MyMovieList</router-link> |
        <router-link :to="{name: 'Profile'}">Profile</router-link> |
        <router-link to="#" @click.native="logout">LOGOUT</router-link> |
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
    </div>
    <router-view @login="login = true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      login: false, //flag
    }
  },
  methods: {
    logout: function() {
      console.log('logout 됨')
      // 로그아웃 처리
      this.login = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    //1. vue instance가 생성된 직후에 jwt를 가져오는 함수 실행하기
    const token = localStorage.getItem('jwt')
    // 2. 토큰이 있따면..
    if (token) {
      this.login = true
    }
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
