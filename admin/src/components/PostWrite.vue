<template>
  <section id="postWrite" class="section">
    <h1 class="title">Post Write</h1>
    <form id="frmPostWrite">
      <input type="hidden" v-model="post.id" />
      <div class="field">
        <label class="checkbox">
          <input
            type="checkbox"
            v-model="post.is_featured" /> is featured
        </label>
      </div>
      <div class="field">
        <label class="checkbox">
          <input
            type="checkbox"
            v-model="post.is_list" /> is listed
        </label>
      </div>
      <div class="field">
        <label class="label">title</label>
        <div class="control">
          <input
            type="text"
            class="input"
            v-model="post.title" />
        </div>
      </div>
      <div class="field">
        <label class="label">content</label>
        <div class="columns">
          <div class="column">
            <textarea
              class="textarea"
              v-model="post.content"></textarea>
          </div>
          <div class="column">

          </div>
        </div>
      </div>
      <div class="field">
        <label class="label">slug</label>
        <div class="control">
          <input
            type="text"
            class="input"
            v-model="post.slug" />
        </div>
      </div>
      <div class="buttons">
        <button class="button is-danger">Cancel</button>
        <button class="button is-success">Save</button>
      </div>
    </form>
  </section>
</template>

<script>
export default {
  name: 'PostWrite',
  data () {
    return {
      post: {
        id: null,
        pub_date: new Date(),
        is_featured: false,
        is_list: false,
        content: '',
        title: '',
        slug: ''
      }
    }
  },
  methods: {
    getPost (slug) {
      this.$http({
        methods: 'get',
        url: `/post/${slug}`
      })
        .then((res) => {
          if (res.status === 200) {
            this.post = Object.assign(this.post, res.data)
          }
        })
    },
    dateFormatter (date) {
      date = new Date()
      return date.toLocaleDateString()
    }
  },
  created () {
    if (this.$route.params.slug !== undefined) {
      this.getPost(this.$route.params.slug)
    }
  }
}
</script>

<style>

</style>
