import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    myMovies: [],
    searchList: [],
  },
  mutations: {
    ADD_SEARCH_LIST: function(state, data) {
      const newSearchMoive = {
        title: data
      }
      state.searchList.push(newSearchMoive)
      state.myMovies.push(newSearchMoive)
    },
  },
  actions: {
    onInput: function ({commit}, input_data) {
      commit("ADD_SEARCH_LIST", input_data)
    },

  },
  modules: {
  },
  getters: {
    videoUrl: function(state) {
      if (state.selectedVideo) {
        const videoId = state.selectedVideo.id.videoId
        console.log(`${videoId}입니다.`)
        return `https://www.youtube.com/embed/${videoId}`
      }
      return ''
    },
    isSelected: function(state) {
      return state.selectedVideo !== null
    },
  }
})
