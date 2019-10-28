<template>
  <div class="login container" v-if="showLogin">
    <div class="jumbotron">
      <div v-if="is_login">
        <h1>you already logged in</h1>
      </div>
      <div class="login-form" v-else>
        <form @submit.prevent="submit(email, password)">
          <div class="form-group">
            <label>email</label>
            <input class="form-control" 
              type="text" 
              name="email" 
              v-model="email" 
              placeholder="email" />
          </div>
          <div class="form-group">
            <label>password</label>
            <input type="password" 
              class="form-control"  
              name="password" 
              v-model="password" 
              placeholder="password" />
          </div>
          <div class="block">
            <button type="submit" class="btn btn-primary">login</button>
            <button type="button" class="btn btn-danger" v-on:click="hideLogin()">close</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data() {
    return {
      email: 'admin@gtszoffice.com',
      password: 'admin@gtszoffice.com!@#$',
    }
  },
  methods: {
    submit(email, password) {
      let vm = this
      this.$store.dispatch('login', {email, password})
        .then(() => {
          vm.$store.dispatch('showMessage', {
            message: 'logged in',
            type: 'success'
          })
        })
    },
    hideLogin() {
      let vm = this
      this.$store.dispatch('loginShow', false)
    }
  },
  computed: {
    is_login: {
      get() {
        return this.$store.getters.is_login
      },
      set(value) {
        return value;
      }
    },
    showLogin() {
      return this.$store.getters.loginShow
    }
  }
}
</script>

<style scoped>
.login {position: fixed; top: 11em; left: 50%; transform: translateX(-50%); width: 80%; z-index: 999}
</style>
