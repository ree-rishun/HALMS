import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/payment',
        name: 'Payment',
        component: () => import('../views/Payment.vue')
    },
    {
        path: '/rule',
        name: 'Rule',
        component: () => import('../views/Rule.vue')
    },
    {
        path: '/game',
        name: 'Game',
        component: () => import('../views/GameUI.vue')
    },
    {
        path: '/result',
        name: 'Result',
        component: () => import('../views/Result.vue')
    }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
