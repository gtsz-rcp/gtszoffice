import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'
import PostList from '@/components/post-list'
import PostView from '@/components/post-view'
import BibList from '@/components/bib-list'
import BibView from '@/components/bib-view'
import DistList from '@/components/dist-list'

Vue.use(Router)
Vue.use(Meta)

const progressOpt = {
  func: [
    {call: 'color', modifier: 'temp', argument: '#ffb000'},
    {call: 'fail', modifier: 'temp', argument: '#6e0000'},
    {call: 'location', modifier: 'temp', argument: 'top'},
    {call: 'transition', modifier: 'temp', argument: {speed: '1.5s', opacity: '0.6s', termination: 400}}
  ]
}

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: PostList,
      meta: {
        progress: progressOpt
      }
    },
    {
      path: '/page/:slug',
      name: 'PageView',
      component: PostView,
      meta: {
        progress: progressOpt
      }
    },
    {
      path: '/post',
      name: 'PostList',
      component: PostList,
      meta: {
        progress: progressOpt
      }
    },
    {
      path: '/post/:slug',
      name: 'PostView',
      component: PostView,
      meta: {
        progress: progressOpt
      }
    },
    {
      path: '/bib',
      name: 'BibList',
      component: BibList,
      meta: {
        progress: progressOpt
      }
    },
    {
      path: '/bib/:slug',
      name: 'BibView',
      component: BibView,
      meta: {
        progress: progressOpt
      }
    },
    {
      path: '/dist',
      name: 'DistList',
      component: DistList,
      meta: {
        progress: progressOpt
      }
    }
  ]
})
