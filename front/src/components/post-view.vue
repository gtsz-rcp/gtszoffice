<template lang="html">
  <article class="post">
    <carousel :per-page="1" :loop="true" :autoplay="true" v-if="content.images" class="images">
      <slide v-for="(item, index) in content.images.images" :key="index">
        <img v-bind:src="item.image" v-bind:alt="item.name" />
      </slide>
    </carousel>
    <section class="content">
      <div class="postheader">
        <h1>{{content.title}}</h1>
      </div>
      <div class="entry" v-html="content.content"></div>
      <div class="date">{{content.pub_date}}</div>
    </section>
  </article>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel'
import moment from 'moment'

export default {
  name: 'PostView',
  components: { Carousel, Slide },
  data () {
    return {
      content: {
        title: 'loading'
      }
    }
  },
  methods: {
    get_content: function () {
      this.$http.get(this.api_url())
        .then((result) => {
          if (result.status === 200) {
            this.set_content(result.data)
          }
        })
    },
    api_url: function () {
      let cat = this.$route.name === 'PageView' ? 'page' : 'post'
      return [this.$api_root, cat, this.$route.params.slug].join('/')
    },
    set_content: function (data) {
      data.content = this.$showdown.makeHtml(data.content)
      data.pub_date = moment(data.pub_date).format('ll')
      this.content = data
    }
  },
  metaInfo () {
    return {
      title: this.content.title,
      titleTemplate: '%s-Posts: gtsz.rcp'
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
