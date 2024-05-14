<template>
  <div>
    <h1>로그인 페이지</h1>
    <form @submit.prevent="signIn">
      <div>
        <label for="username">username : </label>
        <input type="text" id="username" v-model="username">
      </div>
      <div>
        <label for="password">password : </label>
        <input type="password" id="password" v-model="password">
      </div>
      <input type="submit" value="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()

const username = ref('')
const password = ref('')

const signIn = function() {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.signIn(payload)
}

</script>

<style scoped>
</style>