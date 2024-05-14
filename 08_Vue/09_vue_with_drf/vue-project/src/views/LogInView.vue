<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <div>
        <label for="username">username : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="password">password : </label>
        <input type="password" v-model.trim="password" id="password">
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref('')
const password = ref('')

const logIn = function() {
  const payLoad = {
    username: username.value,
    password: password.value
  }
  store.logIn(payLoad)
}

</script>

<style>

</style>
