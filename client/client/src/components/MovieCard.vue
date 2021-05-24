<template>
  <div  @click="selectVideo, moveto" class="col-2 col-md-3 form-check form-check-inline card-container" v-if="movie.overview">
      <div class="card my-3 border-0 ">
        <img :src="'https://image.tmdb.org/t/p/w500'+movie.poster_path" alt="movie_img" >
        <div class="card_body bg-dark">
          <p class="card-title fs-5 fw-bolder py-2 text-light bg-secondary">{{movie.title}}</p>
          <!-- <p class="text-light">{{movie.overview}}</p> -->
        </div>
      </div>
  </div>
</template>

<script>
export default {
  name : 'MovieCard',
  data : function (){
    return { 
      movie_src: `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`,
      movie_title: this.movie.title // 제목을 유튜브 검색을 위해 보내기 
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    selectVideo : function() {
      // console.log(`${this.movie.title}검색했음?`)
      this.$store.dispatch('onSearch', this.movie_title)
    },
    moveto : function() {
      this.$router.push({name:'MovieDetail'})
    }
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
  *{
    color: white;
  }
</style>