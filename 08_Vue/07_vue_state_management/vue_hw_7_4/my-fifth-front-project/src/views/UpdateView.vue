<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <p>이름: {{ balance.name }}</p>
    <p>잔고: {{ balance.balance }}</p>
    <button @click="store.increaseBalance(balance.name)">+</button>
  </div>
</template>

<script setup>
import {useRoute} from 'vue-router'
import {useBalanceStore} from '@/stores/balance'

const store = useBalanceStore()
const route = useRoute()

const balance = store.updateBalance(route.params.name)
</script>

<style scoped>
</style>