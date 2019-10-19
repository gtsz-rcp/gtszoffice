import axios from '@/lib/axios'
import moment from 'moment'

export class Artists {
  list(params = {}) {
    return axios.get('/artists')
  }
}