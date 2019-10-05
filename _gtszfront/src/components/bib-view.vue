<template lang="html">
  <article class="post">
    <carousel :per-page="1" :loop="true" :autoplay="true" v-if="content.images" class="images">
      <slide v-for="(item, index) in content.images.images" :key="index">
        <img v-bind:src="item.image" v-bind:alt="item.name" />
      </slide>
    </carousel>
    <section class="content">
      <header class="postheader">
        <h1>{{content.title}}</h1>
        <h2 v-if="content.subtitle">{{content.subtitle}}</h2>
      </header>
      <section class="meta">
        <dl v-for="(item, index) in meta" :key="index">
            <dt>{{item.label}}</dt>
            <dd>{{item.get_value()}}</dd>
        </dl>
      </section>
      <section v-if="content.summary" class="summary">
        <h2 id="summary">Summary</h2>
        <div class="content" v-html="content.summary"></div>
      </section>
      <section v-if="content.toc">
        <h2 id="table-of-contents">Table of Contents</h2>
        <div class="content" v-html="content.toc"></div>
      </section>
      <section v-if="content.figs" class="figs">
          <h2 id="list-of-figs">List of FIGs</h2>
          <div class="content" v-html="content.figs"></div>
      </section>
      <section v-if="content.distributor" class="distributor">
          <h2>Distributor</h2>
          <ul>
            <li v-for="(item, index) in content.distributor" :key="index"><a v-bind:href="item.website">{{item.name}}</a></li>
          </ul>
      </section>
    </section>
  </article>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel'
import numeral from 'numeral'

export default {
  name: 'BibView',
  components: { Carousel, Slide },
  data () {
    return {
      content: [],
      meta: {
        writer: new DataFactory('Writer', artistImplode),
        designer: new DataFactory('Designer', artistImplode),
        publisher: new DataFactory('Publisher', artistImplode),
        language: new DataFactory('Written in', passThrough),
        publisher_place: new DataFactory('Place of Publication', passThrough),
        medium: new DataFactory('Medium of the Book', passThrough),
        page_amt: new DataFactory('Page Amount', (value) => {
          return `${value} Pages`
        }),
        binding_type: new DataFactory('Binding Type', passThrough),
        colorspace: new DataFactory('Printed in', passThrough),
        price: new DataFactory('Price', (value) => {
          return '￦ ' + numeral(value).format('0,0')
        })
      }
    }
  },
  methods: {
    get_content: function () {
      this.$http.get(`${this.$api_root}/book/${this.$route.params.slug}`)
        .then((result) => {
          if (result.status === 200) {
            this.content = this.set_content(result.data, this.$showdown)
            this.set_meta(result.data)
          }
        })
    },
    set_content: function (data, converter) {
      let content = {}
      let contentKeys = ['title', 'summary', 'toc', 'figs', 'distributor', 'images']
      contentKeys.map((curr) => {
        if (data[curr] === null) return
        if ((typeof data[curr] !== 'string' && data[curr].length < 1)) {
          return
        }
        if (typeof data[curr] === 'string' && curr !== 'title') {
          content[curr] = converter.makeHtml(data[curr])
          return
        }
        content[curr] = data[curr]
      })
      return content
    },
    set_meta: function (data) {
      return Object.keys(this.meta).map((curr) => {
        this.meta[curr].set_value(data[curr])
      })
    }
  },
  metaInfo () {
    return {
      title: this.content.title,
      titleTemplate: '%s-bibliography: gtsz.rcp'
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

function DataFactory (label, valueFactory) {
  this.label = label
  this.valueFactory = valueFactory
}

DataFactory.prototype.set_value = function (value) {
  this.value = value
}

DataFactory.prototype.get_value = function () {
  return this.valueFactory(this.value)
}

function artistImplode (value) {
  if (value !== undefined) {
    return value.map((curr) => {
      return curr.name
    }).join(', ')
  }
}

function passThrough (value) {
  return value
}

</script>

<style lang="css">
</style>
