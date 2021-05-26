<template>
  <div id="app">
    <cloud :data="words" :fontSizeMapper="fontSizeMapper" :words="words" :width="500" :rotate="rotate" />
  </div>
</template>
 
<script>
import Cloud from 'vue-d3-cloud'
 
export default {
  name: 'app',
  data() {
    return {
      fontSizeMapper: word => Math.log2(word.value) * 30,
      rotate : word => word.value % 360
    }
  },
  props:{
    words:Array
  },
  components: {
    Cloud,
  }
}
</script>