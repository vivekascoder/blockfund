import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import FundCause from '../views/FundCause'
import Withdraw from '../views/Withdraw'
import AddCause from '../views/AddCause'
import ListWithdrawCauses from '../views/ListWithdrawCauses'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/add-cause',
    name: 'AddCause',
    component: AddCause
  },
  {
    path: '/withdraw',
    name: 'ListWithdrawCauses',
    component: ListWithdrawCauses
  },
  {
    path: '/fund/:cause_id',
    name: 'FundCause',
    component: FundCause
  },
  {
    path: '/withdraw/:id',
    name: 'Withdraw',
    component: Withdraw
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
