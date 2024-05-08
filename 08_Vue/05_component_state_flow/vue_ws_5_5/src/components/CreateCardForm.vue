<template>
  <div>
    <form @submit.prevent="createCardFunc">
      <label for="name">이름</label>
      <input type="text" id="name" v-model="name">
      <label for="title">직함</label>
      <input type="text" id="title" v-model="title">

      <input type="submit" value="명함 추가">
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'

const name = ref('')
const title = ref('')

const emit = defineEmits(['createCardEvent'])
const createCardFunc = function() {
  if (name.value.trim() !== '' && title.value.trim() !== '') {
    const cardInfo = {
      name: name.value,
      title: title.value
    }
    name.value = ''
    title.value = ''
    emit('createCardEvent', cardInfo)
  }
}
</script>

<style scoped>
input {
  box-sizing: border-box;
  background-color: white;
  height: 30px;
  border: dodgerblue 1px solid;
  border-radius: 5px;
  margin-left: 10px;
}
input[type='submit'] {
  color: dodgerblue;
}

#name {
  margin-right: 15px;
}
</style>