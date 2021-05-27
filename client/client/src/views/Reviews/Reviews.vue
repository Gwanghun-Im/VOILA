<template>
  <div class="box">
    <div class="heading">
      <h1>{{movie_info.title}} Reviews</h1>
    </div>
    <div class="box-container">
      <div class="post-box">
        <input type="text" v-model="create.title" placeholder="title">
        <textarea v-model="create.content" placeholder="content"></textarea>
        <div class="reviews">
          <div  @mouseenter="star(2)" v-if="create.rank>1">
            <i class="fas fa-2x fa-star"></i>
          </div>
          <div  @mouseenter="star(2)" v-else-if="create.rank<1">
            <i class="far fa-2x fa-star"></i>
          </div>
          <div  @mouseenter="star(4)" v-if="create.rank>3">
            <i class="fas fa-2x fa-star"></i>
          </div>
          <div  @mouseenter="star(4)" v-else-if="create.rank<3">
            <i class="far fa-2x fa-star"></i>
          </div>
          <div  @mouseenter="star(6)" v-if="create.rank>5">
            <i class="fas fa-2x fa-star"></i>
          </div>
          <div  @mouseenter="star(6)" v-else>
            <i class="far fa-2x fa-star"></i>
          </div>
          <div  @mouseenter="star(8)" v-if="create.rank>7">
            <i class="fas fa-2x fa-star"></i>
          </div>
          <div  @mouseenter="star(8)" v-else>
            <i class="far fa-2x fa-star"></i>
          </div>
          <div  @mouseenter="star(10)" v-if="create.rank>9">
            <i class="fas fa-2x fa-star"></i>
          </div>
          <div  @mouseenter="star(10)" v-else>
            <i class="far fa-2x fa-star"></i>
          </div>
        </div>
        <button class="btn btn-primary" @click="post_review">작성</button>
      </div>
    </div>
    <div class="box-container">
      <div class="mb-3" v-if="movie_info.review_set.length === 0">아직 리뷰가 없네요...</div>
      <div v-for="(review,idx) in movie_info.review_set" :key="idx">
        <div class="content-box" @click="gotoComment(review.id)">
          <div class="top">
            <div class="profile">
              <div class="profile-img">
                <span>{{review.like_users.length}}</span>
              </div>
              <div class="name-user">
                <strong>{{review.title}}</strong>
                <span>@{{review.username.split('@')[0]}}</span>
              </div>
            </div>
            <div class="reviews">
              <div v-if="review.rank>=1">
                <i class="fas fa-star"></i>
              </div>
              <div v-else-if="review.rank<1">
                <i class="far fa-star"></i>
              </div>
              <div  v-if="review.rank>=3">
                <i class="fas fa-star"></i>
              </div>
              <div  v-else-if="review.rank<3">
                <i class="far fa-star"></i>
              </div>
              <div  v-if="review.rank>=5">
                <i class="fas fa-star"></i>
              </div>
              <div  v-else>
                <i class="far fa-star"></i>
              </div>
              <div  v-if="review.rank>=7">
                <i class="fas fa-star"></i>
              </div>
              <div  v-else>
                <i class="far fa-star"></i>
              </div>
              <div   v-if="review.rank>=9">
                <i class="fas fa-star"></i>
              </div>
              <div   v-else>
                <i class="far fa-star"></i>
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
        rank:0
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
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/${this.movie_id}/`,config)
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
      .then(res => {
        this.$router.push({name:'Comments',params:{movie_id:this.movie_info.id, review_id:res.data.id}})
        }
      )
    },
    gotoComment: function (pk) {
      this.$router.push({ 
        name: 'Comments', 
        params:{
          movie_id: this.movie_id ,
          review_id: pk
        }
      })
    },
    star: function (num) {
      this.create.rank = num
    }
  },
  
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
.post-box{
  color: #191919;
  width: 80%;
  background-color: #ffffff;
  border-radius: 24px;
  padding: 20px;
  margin: 15px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.box input,textarea{
  font-family: 'Roboto', sans-serif;
  text-align: center;
  border: 2px solid #3498db;
  padding: 14px 10px;
  outline: none;
  border-radius: 24px;
  transition: 0.25s;
}
.content-box {
  color: #191919;
  width: 500px;
  box-shadow: 2px 2px 30px rgba(196, 8, 221, 0.46);
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
.profile-img span {
  width: 100%;
  height: 100%;
  font-size: 2rem;
  color: rgb(161, 41, 87);
  object-position: center;
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
  display: flex;
  justify-content: center;
  
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