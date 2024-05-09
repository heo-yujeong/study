<template>
  <div class="quiz-create">
    <h3>퀴즈 생성</h3>
    <form @submit.prevent="createQuiz">
      <label for="question">문제</label>
      <input type="text" id="question" v-model="questionText">
      <label for="answer">답안</label>
      <input type="text" id="answer" v-model="answerText">
      <input type="submit" value="퀴즈 생성">
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import {onBeforeRouteLeave} from 'vue-router'

const questionText = ref('')
const answerText = ref('')
const isWriting = ref(false)

const emit = defineEmits(['create-quiz'])
const createQuiz = function() {
  if (questionText.value.trim() !== '' && answerText.value.trim() !== ''){
    const newQuiz = {
      question: questionText.value,
      answer: answerText.value
    }
    questionText.value = ''
    answerText.value = ''
    emit('create-quiz', newQuiz)
  }
}

onBeforeRouteLeave((to, from, next) => {
  if (questionText.value.trim() !== '' | answerText.value.trim() !== '') {
    isWriting.value = true
  }
  if (isWriting.value) {
    const check = window.confirm('작성중이던 문제가 있습니다. 다른 경로로 이동시 작성중이던 내용은 소멸됩니다. 이동하시겠습니까?')
    if (check) {
      next()
    } else {
      next(false)
    }
  } else {
    next()
  }
})

</script>

<style scoped>
.quiz-create {
  border-radius: 10px;
  width: 80%;
  margin: 0 auto;
  padding: 15px 20px;
  background-color: #f5f5f5;
}

label {
  font-size: 14px;
}

input {
  border: solid 1px #ccc;
  border-radius: 5px;
  width: 100%;
  height: 25px;
  margin-top: 5px;
  margin-bottom: 10px;

}

#question {
  height: 70px;
}

input[type='submit'] {
  background-color: dodgerblue;
  color: white;
  border: none;
  height: 30px;
}
</style>