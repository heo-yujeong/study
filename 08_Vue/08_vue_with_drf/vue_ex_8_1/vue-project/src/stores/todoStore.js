import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useTodoStore = defineStore('todo', () => {
  const BASE_URL = 'http://127.0.0.1:8000'
  const todos = ref([])

  const getTodos = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/api/v1/todos/`
    })
      .then(res => todos.value = res.data)
      .catch(error => console.log(error))
  }

  return { BASE_URL, todos, getTodos }
}, { persist: true })
