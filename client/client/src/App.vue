<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container-fluid">
          <router-link :to="{name: 'Home'}"><img src="@/assets/gugu.jpg" alt="?" height='50'></router-link>
          <div class="">
            <div class="row d-flex">
              <div class="col-4"></div>
              <div class="col-4 justify-content-end">
                <div v-if="login">
                  <div class="buttons">
                    <div class="col-5">
                      <router-link :to="{name: 'Profile'}"><input type="submit" class="btn btn-primary" value="profile"></router-link>
                    </div>
                    <div class="col-2"></div>
                    <div class="col-5">
                      <router-link to="#" @click.native="Logout"><input type="submit" class="btn logout" value="logout"></router-link>
                    </div>
                  </div>
                </div>
                <div v-else>
                  <div class="buttons">
                    <div class="col-5">
                      <router-link :to="{ name: 'Login' }"><input type="submit" class="btn login" value="login"></router-link> 
                    </div>
                    <div class="col-2"></div>
                    <div class="col-5">
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
    <router-view @login="Login"/>
  </div>


</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      login: false, //flag
      user:'비둘기'
    }
  },
  methods: {
    Logout: function() {
      console.log('logout 됨')
      // 로그아웃 처리
      this.login = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
      this.user = ''
    },
    Login: function (Username) {
      this.login = true
      this.user = Username.split("@")[0]
      console.log(Username)
    },
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
*{
  font-family: 'Poppins','Nanum Gothic Coding', sans-serif;
}
#app {
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  border-radius: 24px;
  background: #191919;
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
  border-color:  #c0392b;
  color: #c0392b;
}

.logout:hover{
  background: #c0392b;
}

.buttons {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 25px;
}
</style>
