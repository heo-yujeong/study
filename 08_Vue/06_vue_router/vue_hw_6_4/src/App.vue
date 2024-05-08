<template>
  <header>
    <div class="wrapper">
      <MainPage />
      <nav>
        <RouterLink :to="{name:'some'}">Some</RouterLink>
        <RouterLink :to="{name:'other'}">Other</RouterLink>
        <RouterLink :to="{name:'students'}">Students</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainPage from '@/components/MainPage.vue'

</script>

<style scoped>
nav a {
  display: inline-block;
  padding: 0 10px;
  border-left: 1px solid black;
}

nav a:first-of-type {
  border: 0;
}
</style>
