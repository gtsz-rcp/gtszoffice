<template>
  <div id="app">
    <header id="masthead" class="clearfix">
      <h1><router-link :to="{ name: 'Home', params: {} }">금치산자레시피</router-link></h1>
      <nav>
        <ul class="on-lg">
          <li v-for="(value, key) in menu" class="menu-item" :key="key"><router-link :to="value.route">{{value.label}}</router-link></li>
        </ul>
        <ul class="on-sm">
          <li class="show-menu"><a v-on:click="show_menu" href="#">MENU</a></li>
          <li v-for="(value, key) in menu" v-show="smMenuVisible" :key="key" class="menu-item"><router-link :to="value.route">{{value.label}}</router-link></li>
        </ul>
      </nav>
    </header>
    <router-view/>
    <vue-progress-bar></vue-progress-bar>
    <footer></footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      smMenuVisible: false,
      menu: {
        about: {
          route: {name: 'PageView', params: {slug: 'about'}},
          label: 'About'
        },
        posts: {
          route: {name: 'PostList'},
          label: 'Posts'
        },
        bib: {
          route: {name: 'BibList'},
          label: 'Bibliography'
        },
        dist: {
          route: {name: 'DistList'},
          label: 'Distributor'
        }
      }
    }
  },
  methods: {
    show_menu: function () {
      this.smMenuVisible = !this.smMenuVisible
    }
  },
  mounted () {
    this.$Progress.finish()
  },
  created () {
    //  [App.vue specific] When App.vue is first loaded start the progress bar
    this.$Progress.start()
    //  hook the progress bar to start before we move router-view
    this.$router.beforeEach((to, from, next) => {
      //  does the page we want to go to have a meta.progress object
      if (to.meta.progress !== undefined) {
        let meta = to.meta.progress
        // parse meta tags
        this.$Progress.parseMeta(meta)
      }
      //  start the progress bar
      this.$Progress.start()
      //  continue to next page
      next()
    })
    //  hook the progress bar to finish after we've finished moving router-view
    this.$router.afterEach((to, from) => {
      //  finish the progress bar
      this.$Progress.finish()
    })
  }
}
</script>

<style lang="scss">
@import 'assets/scss/_reboot.scss';
@import 'assets/scss/style.scss';
</style>
