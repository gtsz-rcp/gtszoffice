import Vue from 'vue'
import Vuex from 'vuex'
// import * as actions from './actions'
// import * as getters from './getters'

Vue.use(Vuex)

const userStateModule = {
  namespaced: true,
  state: {
    token: false,
    dateJoined: false,
    email: false,
    firstName: false,
    id: false,
    isActive: false,
    isStaff: false,
    isSuperUser: false,
    lastName: false,
    name: false
  },
  mutations: {
    setToken (state, token) {
      console.log()
      state.token = token
    },
    setDateJoined (state, dateJoined) {
      state.dateJoined = dateJoined
    },
    setEmail (state, email) {
      state.email = email
    },
    setFirstName (state, firstName) {
      state.firstName = firstName
    },
    setId (state, id) {
      state.Id = id
    },
    setIsActive (state, isActive) {
      state.isActive = isActive
    },
    setIsStaff (state, isStaff) {
      state.isStaff = isStaff
    },
    setIsSuperUser (state, isSuperUser) {
      state.isSuperUser = isSuperUser
    },
    setLastName (state, lastName) {
      state.lastName = lastName
    },
    setName (state, name) {
      state.name = name
    }
  },
  actions: {
    Login ({commit, dispatch, state}, user) {
      let dispatchSet = [
        {
          key: 'token',
          action: 'setToken'
        },
        {
          key: 'date_joined',
          action: 'setDateJoined'
        },
        {
          key: 'email',
          action: 'setEmail'
        },
        {
          key: 'firstName',
          action: 'setFirstName'
        },
        {
          key: 'id',
          action: 'setId'
        },
        {
          key: 'is_active',
          action: 'setIsActive'
        },
        {
          key: 'is_staff',
          action: 'setIsStaff'
        },
        {
          key: 'is_superuser',
          action: 'setIsSuperUser'
        },
        {
          key: 'last_name',
          action: 'setLastName'
        },
        {
          key: 'name',
          action: 'setName'
        }
      ]

      let _this = this
      dispatchSet.forEach((item) => {
        if (user[item.key] !== undefined) {
          _this.commit(`user/${item.action}`, user[item.key])
        }
      })

      return state.token
    },
    Logout ({commit, dispatch, state}) {
      let _this = this;
      [
        'setToken',
        'setDateJoined',
        'setEmail',
        'setFirstName',
        'setId',
        'setIsActive',
        'setIsStaff',
        'setIsSuperUser',
        'setLastName',
        'setName'
      ].forEach((item) => {
        _this.commit(`user/${item}`, false)
      })
    }
  },
  getters: {
    isAuth (state) {
      return state.token
    }
  }
}

export default new Vuex.Store({
  state: {
    error: false,
    message: false
  },
  mutations: {
    raiseError (state, message) {
      state.error = true
      state.message = message
    }
  },
  actions: {
    raiseError ({ commit }, message) {
      commit('raiseError', message)
    }
  },
  modules: {
    user: userStateModule
  },
  strict: true
})
