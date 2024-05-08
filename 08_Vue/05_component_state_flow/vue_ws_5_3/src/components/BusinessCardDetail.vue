<template>
  <div class="card">
    <h4>이름 : {{card.name}}</h4>
    <p>직함 : {{card.title}}</p>
    <button @click="deleteCardFunc(card)">명함 삭제</button>
  </div>
</template>

<script setup>
defineProps({
  card: Object
})

const emit = defineEmits(['deleteCardEvent'])
const deleteCardFunc = function(card) {
  emit('deleteCardEvent', card)
}

</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  background-color: #eee;
  display: inline-block;
  width: 40%;
  margin: 10px;
  padding: 10px;
}
</style>