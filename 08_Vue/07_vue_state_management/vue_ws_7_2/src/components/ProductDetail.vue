<template>
  <div class="detail">
    <h4>{{ product.name }}</h4>
    <img :src="product.imagePath" alt="#">
    <p>₩ {{ product.price }}</p>
    <p v-if="!product.isFavorite">🤍</p>
    <p v-else>❤</p>
  </div>
</template>

<script setup>
const props = defineProps({
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