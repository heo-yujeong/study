<template>
  <div>
    <li>{{ product.name }} - {{ product.price }}원</li>
  </div>
</template>

<script setup>
const props = defineProps({
  product: Object
})
</script>

<style scoped>
</style>