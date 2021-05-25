<template>
  <div id="app">
    <cloud :data="words" :fontSizeMapper="fontSizeMapper" :width="width" :height="height" :words="words"/>
  </div>
</template>
 
<script>
import Cloud from 'vue-d3-cloud'
 
export default {
  name: 'app',
  data() {
    return {
      width:500,
      height:500,
      fontSizeMapper: word => Math.log2(word.value) * 4,
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