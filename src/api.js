import axios from 'axios'

const api = axios.create({
  baseURL: 'https://api.florencenet.tzkt.io/',
})

export {api}