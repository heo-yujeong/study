<template>
  <div>
    <p>이름: {{ balance.name }}</p>
    <p>잔고: {{ balance.balance }}</p>
    <button @click="updateBalance(balance.name)">updateBalance</button>
    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
defineProps({
  balance: Object
})

const updateBalance = function (name) {
  router.push({name: 'update', params: {name: name}})
}
</script>

<style scoped>
button {
  background-color: dodgerblue;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
}
</style>