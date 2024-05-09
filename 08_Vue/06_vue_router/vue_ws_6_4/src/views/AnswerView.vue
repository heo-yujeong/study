<template>
  <div>
    <p>{{ route.params.pk }}번 문제</p>
    <h3>정답 확인</h3>
    <div>
      <p v-if="isAnswerCorrect">정답입니다!</p>
      <p v-else>오답입니다.</p>
      <p>나의 제출 답안: {{ userAnswer }}</p>
      <p>정답: {{ route.params.answer }}</p>
    </div>
  </div>
</template>

<script setup>
import {useRoute} from 'vue-router'
import {ref, computed} from 'vue'

const route = useRoute()
const userAnswer = ref(route.query.inputAnswer)

const isAnswerCorrect = computed(() => {
  return userAnswer.value.trim() === route.params.answer.trim()
})
</script>

<style scoped>

</style>