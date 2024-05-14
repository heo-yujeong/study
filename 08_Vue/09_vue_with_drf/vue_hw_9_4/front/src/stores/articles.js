import axios from 'axios'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const token = ref(null)
  const router = useRouter()

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then(res => articles.value = res.data)
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => console.log(res))
  }

  const signUp = function(payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: {
        username, password1, password2
      }
    })
      .then(res => {
        // console.log('회원가입 성공')
        const password = password1
        signIn({username, password})
      })
      .catch(error => {
        console.log(error)
      })
  }

  const signIn = function(payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username, password
      }
    })
      .then(res => {
        // console.log('로그인!')
        token.value = res.data.key
        router.push({name: 'home'})
      })
      .catch(error => {
        console.log(error)
      })
  }

  return { articles, getArticles, createArticle, signUp, signIn, isLogin, token }
})
