import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    myMovies: [],
    SearchList: [],
  },
  mutations: {
    ADD_SEARCH_LIST: function(state, data) {
      const newSearchMoive = {
        title: data
      }
      state.SearchList.push(newSearchMoive)
      state.myMovies.push(newSearchMoive)
    }
  },
  actions: {
    onInput: function ({commit}, input_data) {
      commit("ADD_SEARCH_LIST", input_data)
    }
  },
  modules: {
  }
})
