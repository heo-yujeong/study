<template>
  <div class="card">
    <h4>이름 : {{card.name}}</h4>
    <p>직함 : {{card.title}}</p>
  </div>
</template>

<script setup>
defineProps({
  card: Object
})
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