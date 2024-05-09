<template>
  <div class="quiz">
    <h4>{{ quiz.pk }}번 문제. {{ quiz.question }}</h4>
    <p>정답 입력</p>
    <input type="text" v-model="inputAnswer" @keyup.enter="submitAnswer(quiz.pk, quiz.answer)">
  </div>
</template>

<script setup>
import {ref} from 'vue'
import {useRouter} from 'vue-router';
defineProps({
  quiz: Object
})

const router = useRouter();
const inputAnswer = ref('')

const submitAnswer = function(quizPk, quizAnswer) {
  router.push({
    name: 'answer',
    params: {
      pk: quizPk,
      answer: quizAnswer
    },
    query: {
      inputAnswer: inputAnswer.value
    }
  })
}

</script>

<style scoped>
h4 {
  margin: 0 0 10px 0;
}

p {
  margin: 5px 0;
  font-size: 13px;
}
.quiz {
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 1px 1px 5px #eee;
  background-color: #fcfcfc;
  margin: 20px auto;
  padding: 20px;
  width: 90%;
}

input[type='text'] {
  width: 100%;
  height: 30px;
  border: solid 1px #ccc;
  border-radius: 5px;
}
</style>