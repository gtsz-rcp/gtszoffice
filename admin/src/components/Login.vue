<template>
  <div class="login container">
    <div class="login-form" v-if="is_login()">
      <form @submit.prevent="submit(email, password)">
        <div class="block">
          <input type="text" name="email" v-model="email" placeholder="email" />
        </div>
        <div class="block">
          <input type="password" name="password" v-model="password" placeholder="password" />
        </div>
        <div class="block">
          <p v-if="message != ''">{{message}}</p>
        </div>
        <div class="block">
          <button type="submit">login</button>
        </div>
      </form>
    </div>
    <div v-else>
      <h1>you already logged in</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data() {
    return {
      message: '',
      email: '',
      password: '',
    }
  },
  methods: {
    submit(email, password) {
      this.$store.dispatch('login', {email, password})
        .then(() => {
          alert('logged in')
        })
        .catch(({message}) => {
          this.message = message
        })
    },
    is_login() {
      return this.$store.state.is_login
    }
  }
}
</script>
