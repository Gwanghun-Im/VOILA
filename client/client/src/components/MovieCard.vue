<template>
  <div class="col-3 form-check form-check-inline card-container" v-if="movie.overview">
    <a href="http://google.com">
      <div class="card my-3 border-0">
        <img :src="movie_src" alt="movie_img" >
        <div class="card_body bg-dark">
          <p class="card-title fs-5 fw-bolder py-2 text-light bg-secondary">{{movie.title}}</p>
          <!-- <p class="text-light">{{movie.overview}}</p> -->
        </div>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name : 'MovieCard',
  data : function (){
    return {
      movie_src: `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`,
      
    }
  },
  props: {
    movie: Object,
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
</style>