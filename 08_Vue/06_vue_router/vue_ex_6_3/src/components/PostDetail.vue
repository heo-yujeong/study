<template>
  <div>
    <p>번호 : {{ post[0].id }}</p>
    <p>제목 : {{ post[0].title }}</p>
    <p>내용 : {{ post[0].content }}</p>
  </div>
</template>

<script setup>
import {ref, computed} from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const username = ref(route.params.username)
const postId = ref(route.params.id)

const posts = ref([
  {id: 1, title: 'Post 1', content: 'Content 1'},
  {id: 2, title: 'Post 2', content: 'Content 2'},
  {id: 3, title: 'Post 3', content: 'Content 3'},
])

const post = computed(() => {
  return posts.value.filter((p) => p.id == postId.value)
})

onBeforeRouteUpdate((to, from) => {
  if (to.params.id !== from.params.id) {
    postId.value = to.params.id
  }
})

</script>

<style scoped>

</style>