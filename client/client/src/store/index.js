import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default new Vuex.Store({
  state: {
    myMovies: [],
    searchList: [],
    selectedVideo: null,
  },
  mutations: {
    ADD_SEARCH_LIST: function(state, data) {
      const newSearchMoive = {
        title: data
      }
      state.searchList.push(newSearchMoive)
      state.myMovies.push(newSearchMoive)
    },
    SELECT_VIDEO: function(state, movie_info) {
      state.selectedVideo = movie_info
      // axios 제목을 주고, 해장 영화의 정보를 받아옴.
    }
  },
  actions: {
    onInput: function ({commit}, input_data) {
      commit("ADD_SEARCH_LIST", input_data)
    },
    selectVideo: function (context, movie_title) {
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: movie_title
      }

      axios({
        url: API_URL,
        method: 'get',
        params,
      }).then(res => {
        context.commit('SELECT_VIDEO', res.data.item)
      }).catch(err => {
        console.log(err)
      })

    }
  },
  modules: {
  },
  getters: {
    videoUrl: function(state) {
      if(state.selectedVideo) {
        const videoId = state.selectedVideo.id.videoId
        console.log(`${videoId}입니다.`)
      }
      return ''
    },
    isSelected: function(state) {
      return state.selectedVideo !== null
    }
  }
})
