<template lang="html">
  <article class="page">
    <div class="postheader">
      <h1>Bibliography</h1>
    </div>
    <div class="entry">
      <ul>
        <li v-for="item in lists" :key="item.id" class="citation">
          <span class="writer" v-if="item.writer.length > 0">{{name_implode(item.writer)}}.</span> <span class="editor" v-if="item.editor.length > 0">{{name_implode(item.editor)}}(Eds.),</span> <router-link :to="{name: 'BibView', params: {slug: item.slug}}">{{item.title}}</router-link>. {{name_implode(item.publisher)}}: {{item.publisher_place}}, {{date_format(item.pub_date)}}
        </li>
      </ul>
    </div>
  </article>
</template>

<script>
const moment = require('moment')

export default {
  name: 'BibView',
  data () {
    return {
      lists: []
    }
  },
  methods: {
    get_lists: function () {
      this.$http.get(`${this.$api_root}/book`)
        .then((result) => {
          if (result.status === 200) {
            this.lists = result.data
          }
        })
    },
    date_format: function (dateStr) {
      let m = moment(dateStr)
      return m.format('Y')
    },
    name_implode: function (artistArr) {
      return artistArr.map((curr) => {
        return curr.name
      }).join(', ')
    }
  },
  metaInfo () {
    return {
      title: 'Bibliography: gtsz.rcp'
    }
  },
  beforeRouteEnter (to, from, next) {
    next(vm => vm.get_lists())
  },
  beforeRouteUpdate (to, from, next) {
    this.lists = []
    this.get_lists()
    next()
  }
}
</script>

<style lang="css">
</style>
