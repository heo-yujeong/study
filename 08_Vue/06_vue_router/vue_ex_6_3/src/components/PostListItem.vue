<template>
  <li v-for="post in posts" :key="post.id">
    <RouterLink :to="{name: 'post-detail', params: {username: username, id: post.id}}">제목: {{ post.title }}</RouterLink>
  </li>
</template>

<script setup>
import {ref} from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const username = ref(route.params.username)

defineProps({
  posts: Array
})
</script>

<style scoped>

</style>