<template>
  <div id="login" class="container">
    <form id="frmLogin">
      <input v-model="username" placeholder="username" />
      <input v-model="password" placeholder="password" type="password" />
      <button v-on:click="getAuth">Sign up</button>
    </form>
  </div>
</template>

<script>
import router from '@/router'

export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    getAuth () {
      this.$http({
        method: 'post',
        url: '/user/auth/',
        data: {
          username: this.username,
          password: this.password
        }
      })
        .then((res) => {
          if (res.status === 200) {
            let _this = this
            this.$store.dispatch('user/Login', res.data)
              .then(() => {
                let token = _this.$store.state.user.token
                if (token !== false) {
                  _this.$cookie.set('userToken', token)
                  router.replace('/')
                }
              })
          }
        })
        .catch((error) => {
          if (error === 'Error: "Request failed with status code 401"') {
            alert('Login failed')
          }
        })
    }
  }
}
</script>
