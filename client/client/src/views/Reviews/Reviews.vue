<template>
  <div class="box">
    <div class="heading">
      <h1>{{movie_info.title}} Reviews</h1>
    </div>
    <div class="box-container">
      <div class="post-box">
        <div class="top">
          <div class="profile">
              <div class="profile-img">
                <img src="" alt="">
              </div>
            <input class="name-user" type="text" v-model="create.title" placeholder="title">
          </div>
          <div class="review">
            <input type="number" v-model="create.rank" placeholder="rank">
          </div>
        </div>
        <div class="context">
          <input type="text" v-model="create.content" placeholder="content">
          <button @click="post_review">작성</button>
        </div>
      </div>
    </div>
    <div class="box-container">
      <div v-for="(review,idx) in movie_info.review_set" :key="idx">
        <div class="content-box">
          <div class="top">
            <div class="profile">
              <div class="profile-img">
                <img src="" alt="">
              </div>
              <div class="name-user">
                <strong>{{review.title}}</strong>
                <span>@{{review.user}}</span>
              </div>
            </div>
            <div class="reviews">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="far fa-star"></i>
              {{review.rank}}
            </div>
          </div>
          <div class="context">
            <p>{{review.content}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'reviews',
  data:function () {
    return {
      movie_id:this.$route.params.id,
      movie_info:[],
      create:{
        title: '',
        content:'',
        rank:''
      }
    }
  },
  created: function (){
    this.get_review()
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
    get_review: function (){
      axios.get(`${SERVER_URL}/movies/${this.movie_id}/`)
      .then(res => {
        this.movie_info = res.data
      })
    },
    post_review: function () {
      const token = localStorage.getItem('jwt')
      const params={
        headers: {
          Authorization: `JWT ${token}`,
        },
        data: {
          data: this.create
        }
      }
      axios({
        url:`${SERVER_URL}/movies/${this.movie_id}/`,
        method: 'post',
        headers: params.headers,
        data: this.create
      })
    }
  }
}
</script>

<style scoped>
.box {
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
  align-items: flex-start;
}
</style>