<template>
  <div class= "container">
    <hr>
    <div class="row">
      <h2 v-if="movie_detail.movie.title">{{movie_detail.movie.title}}</h2>
      <hr>
      <iframe class="d-flex justify-content-center" :src="`https://www.youtube.com/embed/${movie_detail.youtube.items[0].id.videoId}`"
      style="display:block; width:100vw; height: 60vh" frameborder="0" allow="autoplay"></iframe>
      <hr>
      <div class="col" style="background-color: #8A2BE2;color: white;"> 장르
        <hr>
        <div class="col">
          <span v-for="(genre, idx) in movie_detail.movie.genres" :key='idx'>{{genre.name}}    </span>
        </div>
      </div>
      <div class="col" style="background-color: #8A2BE2;color: white;">평점
        <hr>
        <div class="col">
          <div class="rating">
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star"></span>
            <span class="fa fa-star"></span>
          </div>
          {{movie_detail.movie.vote_average}}
        </div>
      </div>
      <div> 줄거리
        <hr>
        <div> 
          {{movie_detail.movie.overview}}
        </div>
      </div>
      <!-- <p>{{movie_detail}}</p> -->
    </div>
      <div class="modal-footer d-flex justify-content-around">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="getReview">리뷰보기</button>
      </div>
  </div>

</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'MovieDetail',
  props: {
    movie_detail: Object,
  },
  methods: {
    getReview: function () {
      this.$router.push({ name: 'Reviews', params:{id: this.movie_detail.movie.id }})

    }
  },
  computed: {
    ...mapGetters([
    'videoUrl',
    'isSelected',
    ]),
  },
}
</script>

<style>
  .checked {
    color: orange;
  }
  .rating > span:hover:before {
   content: "\2605";
   position: absolute;
}
</style>
