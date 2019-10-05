<template lang="html">
  <article class="page">
    <div class="pageheader">
      <h1>{{content.title}}</h1>
    </div>
    <div class="entry" v-html="content.content"></div>
    <div class="date">{{content.pub_date}}</div>
  </article>
</template>

<script>
const moment = require('moment')

export default {
  name: 'PageView',
  data () {
    return {
      content: []
    }
  },
  methods: {
    get_content: function () {
      this.$http.get(`${this.$api_root}/page/${this.$route.params.slug}`)
        .then((result) => {
          if (result.status === 200) {
            this.set_content(result.data)
          }
        })
    },
    set_content: function (data) {
      data.content = this.$showdown.makeHtml(data.content)
      let m = moment(data.pub_date)
      data.pub_date = m.format('ll')
      this.content = data
    }
  },
  beforeRouteEnter (to, from, next) {
    next(vm => vm.get_content())
  },
  beforeRouteUpdate (to, from, next) {
    this.content = []
    this.get_content()
    next()
  }
}
</script>

<style lang="sass">
</style>
