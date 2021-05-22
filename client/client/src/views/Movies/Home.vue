<template>
  <div>
    <h1>home</h1>
    
    <MySearchForm @on-input='searchMovie'/>

    <ul>
      <MovieCard v-for="(movie, idx) in movies" :key='idx' :movie='movie'/>
    </ul>

    </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import MySearchForm from '@/components/MySearchForm'
// import Video from '@/components/MySearchForm'
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Home',
  components: {
    MySearchForm,
    MovieCard,
  },
  data:function(){
    return{
      movies:[]
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
    }
  },
  // created: function() {
  //   this.getMovies()
  // }
}
</script>

<style>

</style>