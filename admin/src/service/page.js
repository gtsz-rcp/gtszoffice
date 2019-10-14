import axios from '@/lib/axios'

export default {
  data(page = {}) {
    return Object.assign(page, {
      id: 0,
      type: 'page',
      title: null,
      subtitle: null,
      author: null,
      content: null,
      publishedtime: null,
      updatetime: null,
      createtime: null
    })
  },
  register(page = {}) {
    if(page.id) {
      return axios.put(`/pages/${page.id}`, page)
    }
    return axios.post('/pages/', page)
  }
}