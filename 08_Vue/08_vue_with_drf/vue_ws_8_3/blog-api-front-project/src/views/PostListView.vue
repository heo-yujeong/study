<template>
  <div class="post-list">
    <h1>게시물 목록 페이지</h1>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted } from 'vue'

onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/posts/'
  })
    .then(response => console.log(response))
    .catch(error => console.log(error))
})
</script>

<style scoped>
.post-list {
  margin: 30px 20px;
}
</style>