<template>
  <div>
    <ul>
      <div
        v-for="article in store.articles"
        :key="article.pk"
      >
        <h3>{{ article.pk }}번 게시글</h3>
        <p>작성자 : {{ article.user.username }}</p>
        <p>제목 : {{ article.title }}</p>
        <p>내용 : {{ article.content }}</p>
        <hr>
      </div>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style lang="scss" scoped>

</style>