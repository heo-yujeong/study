<template>
  <header>
    <nav v-if="!store.isLogin">
      <RouterLink :to="{ name: 'ArticleView'}">Articles</RouterLink> | 
      <RouterLink :to="{ name: 'SignUpView'}">회원가입</RouterLink> | 
      <RouterLink :to="{ name: 'LogInView'}">로그인</RouterLink>
    </nav>
    <nav v-else>
      <RouterLink :to="{ name: 'ArticleView'}">Articles</RouterLink> | 
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from './stores/counter'

const store = useCounterStore()
</script>

<style scoped>
</style>
