<template>
  <div v-if="article">
    <h4>{{ article.id }}번 게시글</h4>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <hr>
  </div>
</template>

<script setup>
defineProps({
  article: Object
})
</script>

<style scoped>
</style>