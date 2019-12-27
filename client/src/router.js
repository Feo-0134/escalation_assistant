import Vue from 'vue'
import Router from 'vue-router'

import DashBoard from './components/DashBoard'
import Comment from './components/Comment'
import Login from './components/Login'
import Application from './components/Application'
import CmtPool from './components/CmtPool'

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
            path: '/cmtpl',
            name: 'CmtPool',
            component: CmtPool
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