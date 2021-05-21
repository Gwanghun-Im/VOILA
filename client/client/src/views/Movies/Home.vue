<template>
  <div>
    <h1>home</h1>
    
    <MySearchForm/>

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
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getMovies:function () {
      axios.get(`${SERVER_URL}/movies`,{headers: this.setToken()})
      .then(res => {
        this.movies = res.data
      })
      .catch(e => {
        console.log(e)
      })
    }
  },
  created: function() {
    this.getMovies()
  }
  
}
</script>

<style>

</style>