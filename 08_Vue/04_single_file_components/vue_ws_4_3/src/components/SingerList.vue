<template>
  <div class="list">
    <h1>가수 목록</h1>
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
</style>