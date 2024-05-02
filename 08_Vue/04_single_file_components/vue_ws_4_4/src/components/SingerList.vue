<template>
  <div class="list">
    <h1 class="list-h1">가수 목록</h1>
    <SingerDetail />
    <SingerDetail />
  </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue'
</script>

<style scoped>
.list {
  text-align: center;
}

.list-h1 {
  color: orangered;
}

.card {
  display: inline-block;
  width: 40%;
  margin: 20px;
}
</style>