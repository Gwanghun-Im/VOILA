import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'
import Home from '@/views/Movies/Home'
import Reviews from '@/views/Reviews/Reviews'
import Comments from '@/views/Reviews/Comments'

Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path:'/movies/home',
    name:'Home',
    component:Home,
  },
  {
    path: '/reviews/:id',
    name: 'Reviews',
    component: Reviews
  },
  {
    path: '/review/:movie_id/:review_id',
    name: 'Comments',
    component: Comments
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
