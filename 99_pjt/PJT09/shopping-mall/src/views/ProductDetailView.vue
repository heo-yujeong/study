<template>
  <div v-if="product.id">
    <h1>상품명 : {{ product.title }}</h1>
    <img :src="product.image" alt="#" width="200">
    <p>가격: {{ product.price }}</p>
    <p>카테고리: {{ product.category }}</p>
    <button @click="cartStore.addCart(product)">장바구니에 추가</button>
  </div>
  <p v-else>Loading 중...</p>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useCartStore } from '@/stores/counter'
import axios from 'axios'

const route = useRoute()
const cartStore = useCartStore()
const productId = route.params.product_id

const product = ref({})
axios({
  method: 'get',
  url: `https://fakestoreapi.com/products/${productId}`
})
  .then((response) => {
    product.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })

</script>

<style scoped>

</style>