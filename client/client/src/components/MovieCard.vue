<template>
  <div @click="selectVideo" class="col form-check form-check-inline card-container"
    v-if="movie.overview && movie.poster_path" data-bs-toggle="modal" data-bs-target="#selected_movie">
    <div class="card my-3">
      <img :src="'https://image.tmdb.org/t/p/w500'+movie.poster_path" alt="movie_img" class="card-image" >
      
      <div class="card-text mt-0 ">
        <div class="col pt-2 mb-0">{{movie.release_date.split('-')[0]}}</div>
        <p class="card-title fs-5 fw-bolder mb-0 pt-2" >{{movie.title}}</p>
      </div>

    </div>

  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import axios from 'axios'

export default {
  name : 'MovieCard',
  data : function (){
    return { 
      movieClicked: false,
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    selectVideo : function() {
      axios.get(`${SERVER_URL}/movies/detail/${this.movie.id}`)
      .then(res => {
        console.log(res.data)
        this.$emit('card-click', res.data)
      })
    },
  }
}
</script>

<style scoped>
  .card-container {
    transition: .5s;
  }

  .card-container:hover {
    transform: translate3d(0, -5%, 0);
  }

  /* .modal {
    z-index: 9999;
  } */
  .card {
  grid-template-areas: "image" "text" "info";
  border-radius: 18px;
  background: #191919;
  color: white;
  box-shadow: 5px 5px 15px rgba(0,0,0,0.9);
  font-family: roboto;
  text-align: center;
  }
  .card-image {
  grid-area: image;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  background-size: cover;
  }
  .card-text {
  grid-area: text;
  margin: 12px;
  /* width:94%; */
  }
  .card-info {
  grid-area: info; 
  display: grid;
  grid-template-columns: 1fr 1fr ;
  grid-template-rows: 1fr;
  color: white;
  background: black;
  }
</style>
