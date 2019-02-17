import * as types from '@/vuex/mutations'

const state = {
  isAuth: false
}

const mutations = {
  [types.USER_IS_AUTH] (state) {
    state.isAuth = true
  },
  [types.USER_IS_NOT_AUTH] (state) {
    state.isAuth = false
  }
}

export default {
  state,
  mutations
}
