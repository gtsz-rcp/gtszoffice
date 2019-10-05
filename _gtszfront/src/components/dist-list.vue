<template lang="html">
  <article class="page">
  <div class="postheader">
    <h1>Distributor</h1>
  </div>
  <div class="entry">
    <table class="distributor">
      <thead>
        <tr>
          <th>Shop Name</th>
          <th>Region</th>
          <th>Country</th>
          <th>Address</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in lists" :key="item.id">
          <td>
            <a v-bind:href="item.website">{{item.name}}</a>
          </td>
          <td>{{item.Region}}</td>
          <td>{{item.country}}</td>
          <td><a v-bind:href="item.address_map">{{item.address}}</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</article>
</template>

<script>
export default {
  name: 'DistList',
  data () {
    return {
      lists: []
    }
  },
  methods: {
    get_lists: function () {
      this.$http.get(`${this.$api_root}/dist`)
        .then((result) => {
          if (result.status === 200) {
            this.lists = result.data.map(function (curr) {
              curr.address_map = `https://www.google.co.kr/maps/place/${curr.address}`
              return curr
            })
          }
        })
    }
  },
  metaInfo () {
    return {
      title: 'distributors: gtsz.rcp'
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
