<template>
  <div id="post" class="container">
    <table class="table">
      <thead>
        <th>id</th>
        <th>category</th>
        <th>title</th>
        <th>slug</th>
        <th>is featured</th>
        <th>is list</th>
        <th>published</th>
        <th>createdtime</th>
      </thead>
      <tbody>
        <tr v-for="item in postlist" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.category.name }}</td>
          <td><router-link :to="{name: 'post.write', params: { slug: item.slug }}">{{ item.title }}</router-link></td>
          <td>{{ item.slug }}</td>
          <td>{{ item.is_feature_str}}</td>
          <td>{{ item.is_list_str }}</td>
          <td>{{ item.pub_date }}</td>
          <td>{{ item.createtime_str }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import * as post from '@/lib/post'

export default {
  name: 'Post',
  data () {
    return {
      postlist: []
    }
  },
  methods: {
    fetchListPost () {
      this.$http({
        methods: 'get',
        url: '/post'
      })
        .then((res) => {
          if (res.status === 200) {
            this.postlist = res.data.map((item) => {
              return post.postManipulate(item)
            })
          }
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created () {
    this.fetchListPost()
  }
}
</script>

<style>

</style>
