<template>
  <div>
    <MySearchForm @on-input='searchMovie'/>

    <div class='row row-cols-2 row-cols-md-3 row-cols-lg-4 d-inline-block'>
      <MovieCard v-for="(movie, idx) in movies" :key='idx' :movie='movie' @card-click="setMovieDetail"/>
    </div>
    <div class="modal fade" id="selected_movie" tabindex="-1" aria-labelledby="selected_movieLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <MovieDetail :movie_detail="movie_detail" />
        </div>
      </div>
    </div>
      <footer class="fixed-bottom">
        <div class="d-flex justify-content-center text-secondary fs-7">
          <p>by <a href="https://github.com/Gwanghun-Im">Gwanghun</a> and <a href="https://github.com/chanin-shim">Chanin</a> </p>
        </div>
      </footer>
    </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import MySearchForm from '@/components/MySearchForm'
import MovieDetail from '@/components/MovieDetail'
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Home',
  components: {
    MySearchForm,
    MovieCard,
    MovieDetail,
  },
  data:function(){
    return{
      movies:[],
      movie_detail: {},
    }
  },
  methods:{
    getMovies:function () {
      axios.get(`${SERVER_URL}/movies`)
      .then(res => {
        this.movies = res.data
      })
      .catch(e => {
        console.log(e)
      })
    },
    searchMovie: function (res) {
      console.log(res)
      this.movies = res
    },
    setMovieDetail: function (movie) {
      this.movie_detail = movie
    }
  }
}
</script>

<style>
</style>
