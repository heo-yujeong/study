<template>
  <header>
    <div class="wrapper">
      <nav v-if="!store.isLogin">
        <RouterLink to="/">Home</RouterLink> | 
        <RouterLink :to="{name: 'signup'}">SignUp</RouterLink> | 
        <RouterLink :to="{name: 'signin'}">SignIn</RouterLink> | 
      </nav>
      <nav v-else>
        <RouterLink to="/">Home</RouterLink> | 
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
</script>

<style scoped>
</style>
