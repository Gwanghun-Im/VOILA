<template>
  <div>
    <h1>MovieList다</h1>
    <ul>
      <h2>Movies List</h2>
      <MyList v-for='(myMovie,idx) in myMovies' :key='idx' :myMovie='myMovie' />
    </ul>
  </div>
</template>

<script>
import MyList from '@/components/MyList'

export default {
  name : 'MyMovieList',
  components : {
    MyList,
  },
  computed: {
    myMovies: function() {
      return this.$store.state.myMovies
    }
  }
}
</script>

<style>

</style>