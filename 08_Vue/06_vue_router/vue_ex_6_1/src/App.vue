<template>
  <header>
    <nav>
      <RouterLink :to="{name: 'home'}">Home</RouterLink>
      <RouterLink :to="{name: 'about'}">About</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'

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
