<template>
  <div class="box">
    <h1 class="title">초성 맞추기 with 줄거리</h1>
    <br>
    <div class="quiz" v-if="state">
      <div class="top">
        <span class="hide">무야호</span>
        <span>score: {{score}}</span>
        <span>{{time}}</span>
      </div>
      <h3><strong>{{init}}</strong></h3>
      <h5>{{overview}}</h5>
    </div>
    <div class="start" v-else>
      <button class="btn btn-danger" @click="startGame">START</button>
    </div>
    <div class="answer">
      <div class="input-group my-3" v-if="state">
        <input type="text" class="form-control" v-model="myanswer" @keyup.enter="checkAnswer" :placeholder="msg" aria-label="Recipient's username" aria-describedby="basic-addon2">
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button" @click="checkAnswer">Button</button>
        </div>
      </div>
      <div v-if="pass>0 && state">
        남은 패스 기회 : <button class="btn btn-danger" @click="passQuiz">{{pass}}</button> 
      </div>
      <div v-else-if="pass<=0">
        스코어가 감점됩니다 ㅠㅠ <button class="btn btn-danger" @click="passQuiz">pass</button>
      </div>
    </div>
    <br>
    <div class="table" @click="getGame">
      <h3>TOP 10</h3>
      <div class="ranks" v-if="table">
        <div v-for="(ranking,idx) in rankings" :key="idx">
          <div class="rank" :style="[ranking.is_me ? {color:'#3498db'}:{color:'grey'}]">
            <div class="medal">
              <i v-if="idx===0" class="fas fa-trophy" style="color:#f1c40f"></i>
              <i v-else-if="idx===1" class="fas fa-medal" style="color:#bdc3c7"></i>
              <i v-else-if="idx===2" class="fas fa-medal" style="color:#cd7f32"></i>
              <div v-else>{{idx+1}}</div>
            </div>
            <div class="info">
              <div>{{ranking.username}}</div>
              <div>{{ranking.score}}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <br>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'loadsh'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'Game',
  data: function () {
    return {
      state:false,
      score:0,
      pass:5,
      init:'',
      answer:'',
      overview:'',
      myanswer:'',
      msg:'',
      rankings:[],
      time:120,
      table:false
    }
  },
  methods:{
    countDown: function (){
      if (this.time>0){
        setTimeout(()=>{
          this.time -= 1
          this.countDown()
        },1000)
      } else {
        alert('게임이 종료되었습니다.')
        this.time = 120
        this.postGame()
        this.state = false
      }
    },
    startGame:function(){
      axios.get(`https://api.themoviedb.org/3/movie/popular?api_key=3a5a5d5bd9ebc60efe15703f924c7578&language=ko-kr&page=${_.random(1,40)}&region=KR`)
      .then(res => {
        const movie = res.data.results[_.random(1,19)]
        this.answer = movie.title
        this.init = this.getInitSound(movie.title)
        this.overview = movie.overview
        console.log(movie.title)
        this.countDown()
      })
      this.state = true
    },
    getRandomMovie: function () {
      axios.get(`https://api.themoviedb.org/3/movie/popular?api_key=3a5a5d5bd9ebc60efe15703f924c7578&language=ko-kr&page=${_.random(1,40)}&region=KR`)
      .then(res => {
        const movie = res.data.results[_.random(1,19)]
        this.answer = movie.title
        this.init = this.getInitSound(movie.title)
        this.overview = movie.overview
        console.log(movie.title)
      })
      },
    getKorean: function(word){
      return word.replace(/[^\uAC00-\uD7AF\u1100-\u11FF\u3130-\u318F]/gi,"")
    },
    getInitSound:function (src) {
      var init = [ 'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'];
      var iSound = '';
      for(var i=0; i<src.length; i++) {
        var index = Math.floor(((src.charCodeAt(i) - 44032) /28) / 21);
        if(index >= 0) {
          iSound += init[index];
        } 
      }
      return iSound;
    },
    checkAnswer: function (){
      console.log(this.answer)
      console.log(this.myanswer)
      if (this.getKorean(this.answer) === this.getKorean(this.myanswer)){
        this.score += 1
        this.myanswer = ''
        this.msg = ''
        this.getRandomMovie()
      } else {
        this.myanswer = ''
        this.msg = '땡입니다. 다시 입력하세요'
      }
    },
    passQuiz: function () {
      if (this.pass>0){
        this.pass -= 1
        alert(this.answer)
      } else {
        this.score -= 1
        alert(this.answer)
      }
      this.myanswer = ''
      this.msg = ''
      this.getRandomMovie()
    },
    postGame: function (){
      const token = localStorage.getItem('jwt')
      axios({
        url:`${SERVER_URL}/movies/game/`,
        method:'post',
        headers: {Authorization: `JWT ${token}`},
        data:{
          score:this.score
        }
      })
      .then(res => {
        this.rankings = res.data
        this.table=true
      })
    },
    getGame:function(){
      if (this.table){
        this.table = false
      } else {
        const token = localStorage.getItem('jwt')
        axios({
          url:`${SERVER_URL}/movies/game/`,
          method:'get',
          headers: {Authorization: `JWT ${token}`},
        })
        .then(res => {
          console.log(res.data)
          this.rankings = res.data
        })
        this.table = true
      }
    }
  }
}
</script>

<style scoped>
*:not(i){
  font-family: 'Do Hyeon',"Font Awesome 5 Free";
}
.box {
  letter-spacing: 1.5px;
  margin-top: 1%;
  padding: 1% 0 0 0 ;
  width: 100%;
  background: #191919;
  border-radius: 24px;
  color: rgba(255, 255, 255, 0.686);
  flex-wrap: wrap;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.quiz{
  width: 90%;
}
.table{
  width: 80%;
  padding: 10px;
  margin: 5px;
  background: white;
  color: #191919;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border-radius: 24px;
  align-items: center;
  cursor: pointer;
}
.top{
  display: flex;
  justify-content: space-around;
}
.ranks{
  width: 100%;
  display: flex;
  flex-direction: column;
}
.rank{
  width: 100%;
  padding: 0 1rem;
  display: flex;
  justify-content: space-around;
  /* flex-direction: row; */
}
.rank div{
  font-size: 1.5rem;
}
.medal{
  font-size: 1.0em;
}
.hide {
  color: #191919;
}
.hide:hover{
  color: white;
}
.info{
  width: 50%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

</style>