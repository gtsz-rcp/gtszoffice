import Vue from 'vue'
import Vuex from 'vuex'
import axios from './lib/axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    is_login: false,
    accessToken: null
  },
  getters: {

  },
  mutations: {
    login (state, responseStatus) {
      state.is_login = responseStatus == 200
    },
    logout (state) {
      state.is_login = false
    }
  },
  actions: {
    login ({commit}, {email, password}) {
      return axios.post('/auth/login', {email, password})
        .then(({ data }) => {
          commit('login', data.status)
        })
    },
    logout ({commit}) {
      return axios.post('/auth/logout')
        .then(({ data }) => {
          if(data.status == 200) {
            commit('logout')
          }
        })
    }
  }
})
