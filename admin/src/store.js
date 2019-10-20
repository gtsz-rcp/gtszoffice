import Vue from 'vue'
import Vuex from 'vuex'
import axios from './lib/axios'

Vue.use(Vuex)

const loginMessage = (code) => {
  let message = {type: 'error'}
  if(code == '401') {
    message.message = 'id and pass does not matched'
    return message
  }
}

const messageCls = (type) => {
  let cls = 'warning'
  if(type == 'error') {
    return cls
  }
  if(type == 'success') {
    cls = 'primary'
    return cls
  }
  return cls
}

export default new Vuex.Store({
  state: {
    is_login: false,
    accessToken: null,
    loginShow: false,
    message: {
      content: '',
      type: 'error',
      show: false,
    },
  },
  getters: {
    message(state) {
      let messageSet = state.message
      messageSet.cls = 'alert alert-'+messageCls(messageSet.type)
      return messageSet 
    },
    is_login(state) {
      return state.is_login
    },
    loginShow(state) {
      return state.loginShow
    }
  },
  mutations: {
    login (state, status) {
      state.is_login = status
    },
    logout (state) {
      state.is_login = false
    },
    message (state, message) {
      state.message.content = message
    },
    messageType (state, type) {
      state.message.type = type
    },
    messageShow (state, showState) {
      state.message.show = showState
    },
    loginShow (state, showState) {
      state.loginShow = showState
    }
  },
  actions: {
    login ({commit}, {email, password}) {
      let store = this
      return axios.post('/auth/login', {email, password})
        .then(({ data }) => {
          commit('login', data.message == 'success')
        })
        .catch((error) => {
          let message = loginMessage(error.response.status)
          store.dispatch('showMessage', message)
        })
    },
    logout ({commit}) {
      let store = this
      return axios.get('/auth/logout')
        .then(({ data }) => {
          if(data.status == 200) {
            commit('logout')
          }
        })
        .catch((error) => {
          store.dispatch('showMessage', {message: error.message})
        })
    },
    showMessage ({commit}, {type, message}) {
      commit('message', message)
      commit('messageType', type)
      commit('messageShow', true)
    },
    loginShow ({commit}, showStatus) {
      commit('loginShow', showStatus)
    }
  }
})
