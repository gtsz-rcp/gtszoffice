import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Login from '@/components/Login'
import Post from '@/components/Post'
import PostWrite from '@/components/PostWrite'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/post',
      name: 'Post',
      component: Post
    },
    {
      path: '/post/write/:slug',
      name: 'post.write',
      component: PostWrite
    }
  ]
})
