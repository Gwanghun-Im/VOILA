<template>
  <div>
    <input type="text" @keyup.enter="onInput" v-model = 'input_data' class="my-4" >
    <button @click="onInput" type="button" class="btn btn-info mx-1" >Search</button>
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  data: function () {
    return {
      input_data: '',
    }
  },
  methods: {
    onInput: function() {
      this.$store.dispatch('onInput', this.input_data)
    }
  }

}
</script>

<style>

</style>