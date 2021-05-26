<template>
  <div>
    <div class="box justify-content-md-center">
      <div class="profile_img col-12 col-lg-6" >
        <h3>당신의 영화 클라우드</h3>
        <div v-if="words">
          <cloud :words='words' />
        </div>
        <div v-else>
          <h3>아직 좋아한 영화가 없네요</h3>
        </div>
      </div>
      <div class="user_info col-12 col-lg-6">
        <h3>{{user.email}}</h3>
        <input type="text" :placeholder="user.username">
        <input type="date" :placeholder="user.date_of_birth">
        <input type="text" :placeholder="user.address">
        <input type="text" :placeholder="user.phone">
        end
      </div>
    </div>

    <div class="box-container">
      <div class="review_box">
        <h3>당신의 리뷰</h3>
        <div class="box-container">
          <div v-for="(review,idx) in reviews" :key="idx">
            <div class="content-box" @click="gotoComment(review.fields.movie,review.pk)">
              <div class="top">
                <div class="profile">
                  <div class="name-user">
                    <strong>{{review.fields.title}}</strong>
                  </div>
                </div>
                <div class="reviews">
                  <i class="fas fa-star"></i>
                  <i class="fas fa-star"></i>
                  <i class="fas fa-star"></i>
                  <i class="fas fa-star"></i>
                  <i class="far fa-star"></i>
                  {{review.fields.rank}}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import cloud from '@/components/cloud'
import Cloud from '../../components/cloud.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'Profile',
  data: function () {
    return {
      user:'',
      profile_img:'',
      words:[],
      reviews:''
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
      return config
    },

    profile: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/accounts/profile/`,config)
      .then((res) => {
        this.user = res.data.user
        console.log(res.data)
        if (res.data.review) {
          this.reviews = JSON.parse(res.data.review)
        } else {
          this.reviews = 'not yet'
        }
        this.profile_img = res.data.profile_image
        this.$emit('profile',this.user.username)
      })
      .then( () =>{
        this.getWords()
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getWords: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/word/${this.user.id}`,config)
      .then(res => {
        this.words = res.data
      })
    },
    gotoComment:function (m,pk) {
      this.$router.push({ 
        name: 'Comments', 
        params:{
          movie_id: m ,
          review_id: pk
        }
      })
    }
  },
  created:function (){
    this.profile()
  },
  components:{
    cloud,
    Cloud
  }
}
</script>

<style scoped>

h3{
  font-weight: 500;
  margin-bottom: 50px;
}

.review_box{
  margin-top: 1%;
  padding: 1% 0 0 0 ;
  width: 100%;
  background: #191919;
  border-radius: 24px;
  color: white;
  flex-wrap: wrap;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.box {
  margin-top: 1%;
  padding: 5% 0 0 0 ;
  width: 100%;
  background: #191919;
  border-radius: 24px;
  color: white;
  flex-wrap: wrap;
  display: flex;
  align-items: center;
  justify-content: center;
  /* flex-direction: row; */
}

.profile_img {
  height: 800px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  margin: 0;
  padding: 0;
}

.user_info {
  height: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

input{
  font-family: 'Roboto', sans-serif;
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #3498db;
  padding: 10px;
  width:  260px;
  outline: none;
  color: #666666;
  background: #e6e6e6;
  border-radius: 24px;
  transition: 0.25s;
}

input[type="text"]:focus{
  width: 280px;
  border: 2px solid #2ecc71;
}

a {
  text-decoration: none;
}

.heading span{
  font-size: 1.3rem;
  color: white;
  margin-bottom: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
}
.box-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  width: 100%;
}
.content-box,.post-box {
  color: #191919;
  width: 500px;
  box-shadow: 2px 2px 30px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  border-radius: 24px;
  padding: 20px;
  margin: 15px;
  cursor: pointer;
  transition: 0.3s;
}
.content-box:hover {
  transform: translateY(-10px);
  
}
.profile-img{
  width: 50px;
  height: 50px;
  border-radius: 50%;
  overflow: hidden;
  margin-right: 10px;
}
.profile-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  background-color: grey;
}
.profile{
  display: flex;
  align-items: center;
}
.name-user{
  display: flex;
  flex-direction: column;
}
.name-user strong{
  color: #3d3d3d;
  font-size: 1.1rem;
  letter-spacing: 0.5px;
}
.name-user span{
  color: #979797;
  font-size: 0.8rem;
}
.reviews{
  color: #f9d71c;
}
.top{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
.context p{
  display: flex;
  font-size: 0.9rem;
  color: #4b4b4b;
}
</style>