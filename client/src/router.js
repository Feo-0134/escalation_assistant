import Vue from 'vue'
import Router from 'vue-router'

import DashBoard from './components/DashBoard'
import Comment from './components/Comment'
import Login from './components/Login'
import Application from './components/Application'


Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/dsh',
            name: 'DashBoard',
            component: DashBoard
        },
        {
            path: '/apply',
            name: 'Application',
            component: Application
        },
        {
            path: '/',
            name: 'Login',
            component: Login
        },
        {
            path: '/:id/cmt',
            name: 'Comment',
            component: Comment
        },
    ]
})