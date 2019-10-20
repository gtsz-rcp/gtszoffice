import axios from '@/lib/axios'
import moment from 'moment'

export class Page {
  cosntructor(pageType = 'undefined') {
    this.pageType = pageType
  }

  endpoint(params = []) {
    let type = this.pageType + 's'
    return '/'+([type].concat(params)).join('/')
  }
  
  userDatetime(datetime) {
    return moment(datetime).format('YYYY-MM-DD')
  }
  
  serverDatetime(datetime) {
    return moment(datetime).toDate().toISOString()
  }

  data(page = {}) {
    page = Object.assign({
      id: 0,
      type: this.pageType,
      title: '',
      subtitle: '',
      author: null,
      content: '',
      publishedtime: this.userDatetime(new Date),
      updatetime: null,
      createtime: this.userDatetime(new Date)
    }, page);

    ['createtime', 'publishedtime'].forEach((key) => {
      if(page[key]){
        page[`${key}_str`] = moment(page[key]).format('YYYY-MM-DD')
      }
    })

    return page
  }

  get(params = {}) {
    return axios.get(`/pages/${params.id}`)
  }

  register(page = {}) {
    page.publishedtime = this.serverDatetime(page.publishedtime)
    page.createtime = this.serverDatetime(page.createtime)

    if(page.id) {
      return axios.put(`/pages/${page.id}`, page)
    }
    return axios.post('/pages/', page)
  }

  lists(params = {}) {
    return axios.get(this.endpoint())
  }
}