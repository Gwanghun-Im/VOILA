import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'
import Home from '@/views/Movies/Home'
import MyMovieList from '@/views/Movies/MyMovieList'
import MovieDetail from '@/views/Movies/MovieDetail'

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
    path: '/movies/MyMovieList',
    name: 'MyMovieList',
    component: MyMovieList
  },
  { path: '/movies/MovieDetail',
    name: 'MovieDetail',
    component: MovieDetail
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
