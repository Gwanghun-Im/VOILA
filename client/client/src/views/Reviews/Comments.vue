<template>
  <div class="box">
    <br>
    <h1>{{review.movie}}</h1>
    <div class="box-container">
      <div class="content-box">
        <div class="top">
          <div class="profile">
            <div class="like">
              <div v-if="mode" style="color:red">
                <i class="fas fa-3x fa-heart" @click="likeReview"></i>
              </div>
              <div v-else>
                <i class="far fa-3x fa-heart" @click="likeReview"></i>
              </div>
            </div>
            <div class="name-user">
              <p>{{review.title}}</p>
              <span>@{{username}}</span>
            </div>
          </div>
          <div class="reviews">
            <div class="rating">
              <div v-if="review.rank>1">
                <i class="fas fa-2x fa-star"></i>
              </div>
              <div v-else-if="review.rank<1">
                <i class="far fa-2x fa-star"></i>
              </div>
              <div  v-if="review.rank>3">
                <i class="fas fa-2x fa-star"></i>
              </div>
              <div  v-else-if="review.rank<3">
                <i class="far fa-2x fa-star"></i>
              </div>
              <div  v-if="review.rank>5">
                <i class="fas fa-2x fa-star"></i>
              </div>
              <div  v-else>
                <i class="far fa-2x fa-star"></i>
              </div>
              <div  v-if="review.rank>7">
                <i class="fas fa-2x fa-star"></i>
              </div>
              <div  v-else>
                <i class="far fa-2x fa-star"></i>
              </div>
              <div   v-if="review.rank>9">
                <i class="fas fa-2x fa-star"></i>
              </div>
              <div   v-else>
                <i class="far fa-2x fa-star"></i>
              </div>
            </div>
            <span>{{date}}</span>
          </div>
        </div>
        <div class="context">
          <p>{{review.content}}</p>
        </div>
      </div>
    </div>
    <br>
    <h1>Comment</h1>
    <br>
    <div class="comments">
      <div v-for="(comment,idx) in review.comment_set" :key="idx">
        <div class="comment">
          <span>{{comment.content}}</span>
          <button class="btn btn-danger" @click="deleteComment(comment.id)">X</button>
        </div>
      </div>
    </div>
    <div class="postcomment">
      <input type="text" v-model="content" @keyup.enter="postComment">
      <button class="btn btn-primary" @click="postComment">+</button>
    </div>
    <br>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'comments',
  data: function () {
    return {
      movie_id:this.$route.params.movie_id,
      review_id:this.$route.params.review_id,
      content:'',
      review:'',
      mode:false,
      username:'',
      date:''
    }
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        }
      }
      return config
    },
    postComment: function () {
      const token = localStorage.getItem('jwt')
      const params={
        headers: {
          Authorization: `JWT ${token}`,
        }
      }
      axios({
        url:`${SERVER_URL}/movies/${this.movie_id}/${this.review_id}/`,
        method: 'post',
        headers: params.headers,
        data: {
          content:this.content
        }
      })
      .then(setTimeout(1000))
      .then( this.getReview() )
    },
    getReview: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/${this.movie_id}/${this.review_id}/`, config)
      .then(res => {
        console.log(res.data)
        this.mode = res.data.like_user
        this.review = res.data
        this.username = res.data.username.split('@')[0]
        this.date = res.data.created_at.split('.')[0].split('T')[0]
      })
    },
    deleteComment: function (comment_id){
      axios.delete(`${SERVER_URL}/movies/${this.movie_id}/${this.review_id}/${comment_id}/`)
      .then(setTimeout(100))
      .then(this.getReview())
    },
    likeReview: function (){
      const token = localStorage.getItem('jwt')
      const params={
        headers: {
          Authorization: `JWT ${token}`,
        }
      }
      axios({
        url:`${SERVER_URL}/movies/like/${this.review_id}/`,
        method: 'post',
        headers: params.headers
      })
      .then(res => {
        if (res.data===1){
          this.mode = true
        } else {
          this.mode = false
        }
      })
    }
  },
  created: function (){
    this.getReview()
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
.box-container{
  color: #191919;
  width: 80%;
  background-color: #ffffff;
  border-radius: 24px;
  padding: 20px;
  margin: 15px;
  cursor: pointer;
  transition: 0.3s;
}
.box-container:hover {
  box-shadow: 2px 2px 30px rgba(196, 8, 221, 0.46);
  
}
.profile{
  display: flex;
  align-items: center;
}
.like{
  width: 4rem;
  overflow: hidden;
  margin-right: 10px;
  transition: 0.3s;
}
.like:hover{
  color: red;
  transform: translateY(-5px);
}
.name-user{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.name-user p{
  font-family: 'Nanum Gothic Coding',monospace;
  color: #3d3d3d;
  font-size: 2rem;
  font-weight: 300;
  margin: 0%;
}
.name-user span{
  color: #979797;
  font-size: 0.8rem;
  margin-left: 5%;
}
.reviews{
  color: #f9d71c;
  display: flex;
  flex-direction: column;
}
.reviews span{
  color: #979797;
}
.rating{
  display: flex;
}
.top{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
.context p{
  font-family: 'Nanum Gothic Coding',monospace;
  display: flex;
  font-size: 1rem;
  color: #4b4b4b;
  align-items: flex-start;
}
.comments{
  width: 80%;
  display: flex;
  flex-direction: column;
}
.comment{
  padding: 10px;
  margin: 5px;
  background: white;
  color: #191919;
  display: flex;
  justify-content: space-between;
  border-radius: 24px;
  align-items: center;
}
.comment span{
  font-size: 1.5rem;
}
.postcomment{
  margin: 20px;
  width: 80%;
  display: flex;
  background: white;
  justify-content: space-between;
  border-radius: 24px;
}
.postcomment input{
  border: none;
  width: 100%;
  margin-left: 15px;
  border-radius: 24px;
  outline: none;
  border:none;
}
</style>