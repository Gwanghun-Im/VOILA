<template>
  <div class= "container bg-primary" v-if = "isSelected">
    <h1>MovieDetail</h1>
    <iframe src="videoUrl" frameborder="0"></iframe>
    <div class="row">
      <p class="col-4">정보</p>
      <p class="col-4">평점</p>
    </div>
    <p>추천</p>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'MovieDetail',
  computed: {
    ...mapGetters([
    'videoUrl',
    'isSelected',
    ]),
  }
}
</script>

<style>

</style>