<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'home'}">Home</RouterLink>
      <RouterLink :to="{name: 'products'}">Products</RouterLink>
      <RouterLink :to="{name: 'favorite'}">Favorite</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>

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
</style>
