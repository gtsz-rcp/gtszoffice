<template>
  <section class="container page-list">
    <table class="table">
      <thead>
        <tr>
          <th>id</th>
          <th>title</th>
          <th>author</th>
          <th>publishedtime</th>
          <th>createtime</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in lists" class="item" v-bind:key="item.id">
          <td>{{item.id}}</td>
          <td>
            <router-link :to="writeUrl(item.id)">
              {{item.title}} <span class="subtitle" v-if=item.subtitle>-- {{item.subtitle}}</span>
            </router-link>
          </td>
          <td>{{item.author_data.name}}</td>
          <td>{{item.publishedtime_str}}</td>
          <td>{{item.createtime_str}}</td>
        </tr>
      </tbody>
    </table>
    <div class="float-right clearfix">
      <div class="btn-group">
        <router-link :to="writeUrl()" class="btn btn-primary">Write</router-link>
      </div>
    </div>
  </section>
</template>

<script>
import {Page} from '@/service/page'
const pageIO = new Page()

export default {
  name: 'pagesList',
  props: ['type'],
  data() {
    return {
      lists: [],
    }
  },
  methods: {
    getLists() {
      let vm = this
      return pageIO.lists()
        .then((result) => {
          vm.lists = result.data.map((item) => {
            return pageIO.data(item)
          })
        })
    },
    writeUrl(id = '') {
      return `/${this.type}s/${id}`
    }
  },
  beforeCreate(){
  },
  created(){
    pageIO.pageType = this.type
    this.getLists()
  }
}
</script>

<style>

</style>