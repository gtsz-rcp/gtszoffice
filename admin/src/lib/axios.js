import axios from 'axios'
import {API_BASE} from '@/lib/config'

const instance = axios.create({
  baseURL: API_BASE
})

export default instance;