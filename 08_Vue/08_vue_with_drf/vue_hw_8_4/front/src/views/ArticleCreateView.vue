<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title">
      <label for="content">내용 : </label>
      <input type="text" id="content" v-model="content">
      <input type="submit" value="create">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const router = useRouter()

const title = ref('')
const content = ref('')

const createArticle = function() {
  store.createArticle(title.value, content.value)
  router.push({name: 'home'})
}
</script>

<style scoped>
</style>