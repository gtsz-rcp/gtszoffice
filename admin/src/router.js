import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import PagesList from '@/views/pages/list.vue'
import PagesWrite from '@/views/pages/write.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/pages',
      name: 'pagesList',
      component: PagesList,
      alias: '/pages/lists',
      props: {
        type: 'page'
      }
    },
    {
      path: '/pages/write/:id?',
      name: 'pagesWrite',
      component: PagesWrite,
      props: {
        type: 'page'
      }
    },

    {
      path: '/posts',
      name: 'postList',
      component: PagesList,
      alias: '/posts/lists',
      props: {
        type: 'post'
      }
    },
    {
      path: '/posts/write/:id?',
      name: 'postWrite',
      component: PagesWrite,
      props: {
        type: 'post'
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
