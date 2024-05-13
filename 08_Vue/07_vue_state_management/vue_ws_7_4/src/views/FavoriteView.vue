<template>
  <div class="favorite">
    <h1>장바구니 페이지</h1>
    <div class="product-detail">
      <ProductDetail
        v-for="product in store.productList.filter(p => p.isFavorite)"
        :key="product.name"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'
import ProductDetail from '@/components/ProductDetail.vue'

const store = useProductStore()
</script>

<style scoped>
.favorite {
  width: 95%;
  margin: 30px auto;
}

.product-detail {
  display: flex;
  flex-wrap: wrap;
}
</style>