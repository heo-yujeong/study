import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
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
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const signUp = function (payLoad) {
    const { username, password1, password2 } = payLoad

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2
      }
    })
      .then(res => {
        console.log('회원가입 성공')
        const password = password1
        logIn({username, password})
      })
      .catch(error => {
        console.log(error)
      })
  }

  const logIn = function(payLoad) {
    const { username, password } = payLoad

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        // console.log('로그인 성공')
        // console.log(res)
        token.value = res.data.key
        router.push({name: 'ArticleView'})
      })
      .catch(error => {
        console.log(error)
      })
  }

  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })
