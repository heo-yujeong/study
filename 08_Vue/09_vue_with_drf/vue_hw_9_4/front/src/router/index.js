import { createRouter, createWebHistory } from 'vue-router'
import { useArticleStore } from '@/stores/articles'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import SignInView from '@/views/SignInView.vue'

const checkLogin = (to, from, next) => {
  const store = useArticleStore()
  if (store.isLogin) {
    window.alert('이미 로그인 되어 있습니다.')
    next({neme: 'home'})
  } else {
    next()
  }
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
      beforeEnter: checkLogin
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignInView,
      beforeEnter: checkLogin
    }
  ]
})

router.beforeEach((to, from) => {
  const store = useArticleStore()
  if (!store.isLogin && (to.name === 'home' || to.name === 'create')) {
    window.alert('로그인이 필요합니다.')
    return { name: 'signin' }
  }
})

export default router
