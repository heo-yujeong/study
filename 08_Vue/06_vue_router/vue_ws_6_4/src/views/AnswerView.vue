<template>
  <div class="answer-check">
    <p class="title">{{ route.params.pk }}번 문제</p>
    <h3>정답 확인</h3>
    <div class="answer-result">
      <p v-if="isAnswerCorrect" class="green"><b>정답입니다!</b></p>
      <p v-else class="red"><b>오답입니다.</b></p>
      <p class="result" :class="{red:!isAnswerCorrect, green:isAnswerCorrect}">나의 제출 답안: {{ userAnswer }}</p>
      <p class="result">정답: {{ route.params.answer }}</p>
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
.red {
  color: red;
}

.green {
  color: green;
}

.title {
  margin: 0;
}

h3 {
  margin-top: 0;
}

.answer-check {
  text-align: center;
  border: 1px solid #ccc;
  border-radius: 10px;
  width: 80%;
  margin: 0 auto;
  padding: 15px 20px;
  background-color: #f5f5f5;
}

.answer-result {
  text-align: left;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
}

.result {
  font-size: 14px;
}
</style>