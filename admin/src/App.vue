<template>
  <div id="app">
    <div id="nav" class="container">
      <ul class="nav">
        <li class="nav-item">
          <router-link to="/" class="nav-link">Home</router-link>
        </li>
        <li class="nav-item dropdown">
          <a href="#" 
            class="nav-link dropdown-toggle" 
            data-toggle="dropdown">Pages</a>
          <div class="dropdown-menu">
            <router-link class="dropdown-item" to="/pages">lists</router-link>
            <router-link class="dropdown-item" to="/pages/write">write</router-link>
          </div>
        </li>
        <li class="nav-item dropdown">
          <a href="#" 
            class="nav-link dropdown-toggle"
            data-toggle="dropdown">Posts</a>
          <div class="dropdown-menu">
            <router-link to="/posts" class="dropdown-item">lists</router-link>
            <router-link to="/posts/write" class="dropdown-item">write</router-link>
          </div>
        </li>
        <li class="nav-item">
          <a v-if="isLogin() == false" 
            v-on:click="showLogin()" 
            href="#" 
            class="nav-link">Login</a>
          <a v-else 
            href="#"
            v-on:click="logout()" 
            class="nav-link">Logout</a>
        </li>
      </ul>
    </div>
    <router-view />
    <Login />
    <div class="primary-alert container">
      <div 
        v-if="message.show" 
        :class="message.cls">{{message.content}}</div>
    </div>
  </div>
</template>

<script>
import Login from '@/components//Login.vue'

export default {
  name: 'app',
  components: {
    Login
  },
  data() {
    return {
    }
  },
  methods: {
    isLogin() {
      return this.$store.state.is_login
    },
    logout() {
      return this.$store.dispatch('logout')
    },
    showLogin() {
      return this.$store.dispatch('loginShow', true)
    }
  },
  computed: {
    message() {
      let message = this.$store.getters.message
      return message
    }
  }
}
</script>

<style>
.primary-alert {margin-top: 30px;}
</style>