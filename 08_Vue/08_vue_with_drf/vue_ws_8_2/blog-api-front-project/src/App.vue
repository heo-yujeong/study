<template>
  <div>
    <nav class="nav">
      <RouterLink :to="{name: ''}">Home</RouterLink>
    </nav>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.nav {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #292929;
  height: 35px;
}

.nav > a {
  color: #ffffff;
  text-decoration: none;
}
</style>
