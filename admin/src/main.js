// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from '@/App'
import router from '@/router'
import store from '@/vuex/store'
import axios from 'axios'
import VueCookie from 'vue-cookie'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.config.productionTip = false
Vue.use(VueCookie)

Vue.prototype.$http = axios.create({
  baseURL: (process.env.API_ROOT !== undefined ? process.env.API_ROOT : '')
})

/* eslint-disable no-new */
new Vue({
  store,
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  created () {
    let token = this.$cookie.get('userToken')
    if (token === null) {
      return router.replace('/login')
    } else {
      this.$http.defaults.headers.common = {
        'Authorization': `bearer ${token}`
      }
    }
  }
})
