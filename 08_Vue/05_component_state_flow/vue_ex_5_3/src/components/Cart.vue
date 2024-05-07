<template>
  <ul>
    <li v-for="(product, index) in cartProducts" :key="product.id">
      {{ product.name }} - {{ product.price }}원
      <button @click="deleteCart(index)">삭제</button>
    </li>
  </ul>
</template>

<script setup>
defineProps({
  cartProducts: Array
})

const emit = defineEmits(['deleteCart'])
const deleteCart = function(index) {
  emit('deleteCart', index)
}
</script>

<style scoped>
</style>