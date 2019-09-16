import Vue from 'vue'
import App from './App'
import router from './router'
import instance from './axios-config'
import showdown from 'showdown'
import VueProgressBar from 'vue-progressbar'

Vue.config.productionTip = false

Vue.prototype.$http = instance
Vue.prototype.$api_root = (process.env.API_ROOT !== undefined ? process.env.API_ROOT : '')
Vue.prototype.$showdown = new showdown.Converter({
  headerLevelStart: 2
})

Vue.use(VueProgressBar, {
  color: '#bffaf3',
  failedColor: '#874b4b',
  thickness: '5px',
  transition: {
    speed: '0.2s',
    opacity: '0.6s',
    termination: 300
  },
  autoRevert: true,
  location: 'left',
  inverse: false
})

export default new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  metaInfo: {
    title: 'gtsz.rcp HOME'
  }
}).$mount('#app')
