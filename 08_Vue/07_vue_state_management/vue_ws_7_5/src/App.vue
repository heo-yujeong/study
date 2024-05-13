<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'home'}">Home</RouterLink>
      <RouterLink :to="{name: 'products'}">Products</RouterLink>
      <RouterLink :to="{name: 'favorite'}">
        Favorite 
        <div v-if="store.numOfFavorite > 0" class="circle-number">{{ store.numOfFavorite }}</div>
      </RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'

const store = useProductStore()
</script>

<style scoped>
nav {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
  background-color: rgb(61, 61, 61);
}

nav > a {
  color: white;
  text-decoration: none;
  margin: 10px;
}

.circle-number {
  display: inline-block;
  text-align: center;
  background-color: red;
  width: 18px;
  height: 18px;
  font-size: 13px;
  border-radius: 50%;
}
</style>
