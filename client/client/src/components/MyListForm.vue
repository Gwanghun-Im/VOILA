<template>
  <div>
    <input type="text" @keyup.enter="onInput" v-model = 'input_data' >
    <button @click="onInput">입력</button>
  </div>
</template>

<script>
export default {
  name: 'MySearchForm',
  data: function () {
    return {
      input_data: '',
    }
  },
  methods: {
    onInput: function() {
      console.log(this.input_data)
    }
  }

}
</script>

<style>

</style>