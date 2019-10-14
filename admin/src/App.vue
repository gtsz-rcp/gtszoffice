<template>
  <div id="app">
    <div id="nav" class="container">
      <ul class="nav">
        <li class="nav-item">
          <router-link to="/" class="nav-link">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/pages" class="nav-link">Pages</router-link>
        </li>
        <li class="nav-item">
          <a href="#" v-on:click@prevent="showLogin" class="nav-link">Login</a>
        </li>
      </ul>
    </div>
    <router-view />
    <Login />
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
      showLogin: false
    }
  }
}
</script>