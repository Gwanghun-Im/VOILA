<template>
  <div class= "container bg-dark text-white">
    <hr>
    <div class="row">
      <h2 class="fs-3 fw-bolder mb-3" v-if="movie_detail.movie.title">{{movie_detail.movie.title}} <span class="fs-5 fw-light mb-3" v-if="movie_detail.movie.release_date">({{movie_detail.movie.release_date.split('-')[0]}})</span></h2>
      <hr>
      <iframe class="d-flex justify-content-center" :src="`https://www.youtube.com/embed/${movie_detail.youtube.items[0].id.videoId}`"
      style="display:block; width:100vw; height: 40vh" frameborder="0" allow="autoplay"></iframe>
      <hr>
      <div class="col col-bg"> 장르
        <hr>
        <div class="col">
          <span v-for="(genre, idx) in movie_detail.movie.genres" :key='idx'>{{genre.name}}    </span>
        </div>
      </div>
      <div class="col col-bg">평점
        <hr>
        <div class="col">
          <div class="rating">
            <div v-if="movie_detail.movie.vote_average>1">
              <i class="fas fa-2x fa-star"></i>
            </div>
            <div v-else-if="movie_detail.movie.vote_average<1">
              <i class="far fa-2x fa-star"></i>
            </div>
            <div  v-if="movie_detail.movie.vote_average>3">
              <i class="fas fa-2x fa-star"></i>
            </div>
            <div  v-else-if="movie_detail.movie.vote_average<3">
              <i class="far fa-2x fa-star"></i>
            </div>
            <div  v-if="movie_detail.movie.vote_average>5">
              <i class="fas fa-2x fa-star"></i>
            </div>
            <div  v-else>
              <i class="far fa-2x fa-star"></i>
            </div>
            <div  v-if="movie_detail.movie.vote_average>7">
              <i class="fas fa-2x fa-star"></i>
            </div>
            <div  v-else>
              <i class="far fa-2x fa-star"></i>
            </div>
            <div   v-if="movie_detail.movie.vote_average>9">
              <i class="fas fa-2x fa-star"></i>
            </div>
            <div   v-else>
              <i class="far fa-2x fa-star"></i>
            </div>
          </div>
          {{movie_detail.movie.vote_average}}
        </div>
      </div>
      <div> 
        <h5>줄거리</h5> 
        <hr>
        <div class="overview"> 
          {{movie_detail.movie.overview}}
        </div>
      </div>
      <!-- <p>{{movie_detail}}</p> -->
    </div>
      <div class="modal-footer d-flex justify-content-around">
        <button v-if="mode" type="button" class="btn btn-danger" @click="likeMovie">Like this</button>
        <button v-else type="button" class="btn btn-outline-danger" @click="likeMovie">Like this</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="getReview">리뷰보기</button>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'MovieDetail',
  data: function (){
    return {
      mode:false
    }
  },
  props: {
    movie_detail: Object,
  },
  methods: {
    getReview: function () {
      this.$router.push({ name: 'Reviews', params:{id: this.movie_detail.movie.id }})
    },
    likeMovie: function () {
      const token = localStorage.getItem('jwt')
      const params={
        headers: {
          Authorization: `JWT ${token}`,
        }
      }
      axios({
        url:`${SERVER_URL}/movies/likemovie/${this.movie_detail.movie.id}/`,
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
}
</script>

<style>
.rating  {
  color: #f9d71c;
  display: flex;
  justify-content: center;
}
.container{
  border-radius: 24px;
}
.container{
  background: #9053c7;
  background: -webkit-linear-gradient(-135deg, #c850c0, #4158d0);
  background: -o-linear-gradient(-135deg, #c850c0, #4158d0);
  background: -moz-linear-gradient(-135deg, #c850c0, #4158d0);
  background: linear-gradient(-135deg, #c850c0, #4158d0);
  box-shadow: 2px 2px 30px rgb(0, 0, 0);
}
.overview{
  font-family: 'Nanum Gothic Coding',monospace;
}
</style>
