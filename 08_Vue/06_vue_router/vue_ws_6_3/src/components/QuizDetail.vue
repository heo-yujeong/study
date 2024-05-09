<template>
  <div class="quiz">
    <h4>{{ quiz.pk }}번 문제. {{ quiz.question }}</h4>
    <p>정답 입력</p>
    <input type="text">
  </div>
</template>

<script setup>
defineProps({
  quiz: Object
})
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