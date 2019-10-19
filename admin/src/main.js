import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from './lib/axios'
import VueTheMask from 'vue-the-mask'
import 'jquery'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import '@/assets/css/style.css'

Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.use(VueTheMask)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
