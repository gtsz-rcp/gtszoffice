<template>
  <section class="page-write container">
    <h1>Write Page</h1>
    <form @submit.prevent="putPage()">
      <div class="form-group">
        <label for="pageTitle">title</label>
        <input type="text" id="pageTitle" class="form-control" v-model="page.title" required />
      </div>
      <div class="form-group">
        <label for="pageSubtitle">subtitle</label>
        <input type="text" id="pageSubtitle" class="form-control" v-model="page.subtitle" required />
      </div>
      <div class="form-group">
        <label for="pageContent">content</label>
        <textarea id="pageContent" class="form-control" rows="3" v-model="page.content" required></textarea>
      </div>
      <artistsSelector v-model="page.author" :value="page.author" label="author" />
      <div class="form-group">
        <label>publishedtime</label>
        <the-mask mask="####-##-##" v-model="page.publishedtime" :masked="true" class="form-control"></the-mask>
      </div>
      <div class="form-group clearfix">
        <div class="btn-group">
          <router-link to="/pages" class="btn btn-secondary">Lists</router-link>
          <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </form>
  </section>
</template> 

<script>
import {Page} from '@/service/page'
import artistsSelector from '@/views/artists/selector.vue'

const pageIO = new Page('page')

export default {
  name: 'PagesWrite',
  components: { artistsSelector },
  data() {
    return {
      page: pageIO.data()
    }
  },
  methods: {
    getPage(id) {
      let vm = this
      pageIO.get({id})
        .then((result) => {
          vm.page = result.data
        })
    },
    putPage() {
      pageIO.register(this.page)
        .then((result) => {
          if(result.status == 200) {
            alert('success')
          }
        })
    }
  },
  created() {
    if(this.$route.params.id !== undefined) {
      this.getPage(this.$route.params.id)
    }
  }
}
// id = db.Column(db.Integer(), primary_key=True)
// type = db.Column(db.Enum(PagesType), nullable=False, default='post')
// slug = db.Column(db.String(64), nullable=True, unique=True)
// title = db.Column(db.String(255), nullable=False)
// subtitle = db.Column(db.String(255), nullable=True, default=None)
// author = db.Column(db.Integer(), default=1)
// content = db.Column(db.UnicodeText)
// publishedtime = db.Column(db.DateTime, default=datetime.now())
// deletetime = db.Column(db.DateTime, nullable=True, default=None)
// updatetime = db.Column(db.DateTime, nullable=True, default=None, onupdate=datetime.utcnow())
// createtime = db.Column(db.DateTime, default=datetime.now())
</script>

<style>

</style>