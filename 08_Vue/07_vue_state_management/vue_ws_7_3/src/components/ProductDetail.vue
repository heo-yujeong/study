<template>
  <div class="detail">
    <h4>{{ product.name }}</h4>
    <img :src="product.imagePath" alt="#">
    <p>₩ {{ product.price }}</p>
    <p v-if="!product.isFavorite" @click="store.updateFavorite(product.name)">🤍</p>
    <p v-else @click="store.updateFavorite(product.name)" style="color: red;">❤</p>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'

const store = useProductStore()
defineProps({
  product: Object
})

</script>

<style scoped>
p {
  margin: 10px 0;
}

h4 {
  margin-bottom: 5px;
}
.detail {
  border: 1px solid #eee;
  text-align: center;
  margin: 10px;
  width: 30%;
  padding-top: 10px;
  padding-bottom: 30px;
}

.detail > img {
  width: 85%;
}
</style>