<template>
  <section class="container page-list">
    <div class="float-right clearfix">
      <div class="btn-group">
        <button class="btn btn-primary">Write</button>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'pagesList',
  data() {
    return {
      lists: []
    }
  },
  methods: {
    getLists() {
      var vm = this
      this.$axios.get('/pages')
        .then(function(result){
          vm.data = result.data
        })
    }
  },
  beforeCreate(){
    },
  created(){
    this.getLists()
  }
}
</script>

<style>

</style>