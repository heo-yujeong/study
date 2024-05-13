<template>
  <div class="article-list">
    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
.article-list {
  margin-left: 30px;
}
</style>