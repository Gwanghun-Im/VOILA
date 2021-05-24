<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-light bg-dark">
        <div class="container-fluid">
          <router-link :to="{name: 'Home'}"><img src="@/assets/gugu.jpg" alt="?" height='50'></router-link>
          <div class="container">
            <div class="row d-flex">
              <div class="col-8"></div>
              <div class="col-4 justify-content-end">
                <div v-if="login">
                  <div class="row">
                    <div class="col-4 text-white">{{user}}</div>
                    <div class="col-4">
                      <router-link to="#" @click.native="logout"><input type="submit" class="btn logout" value="logout"></router-link>
                    </div>
                    <div class="col-4">
                      <router-link :to="{name: 'Profile'}"><input type="submit" class="btn btn-primary" value="profile"></router-link>
                    </div>
                  </div>
                </div>
                <div v-else>
                  <div class="row">
                    <div class="col-4"></div>
                    <div class="col-4">
                      <router-link :to="{ name: 'Login' }"><input type="submit" class="btn login" value="login"></router-link> 
                    </div>
                    <div class="col-4">
                        <router-link :to="{ name: 'Signup' }"><input type="submit" class="btn signup" value="signup"></router-link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </nav>
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

nav {
  padding: 30px;
  border-radius: 24px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.login{
  background: #2ecc71;
  color: white;
}

.signup{
  background: #2980b9;
  color: white;
}

.logout {
  background: #c0392b;
  color: white;
}
</style>
