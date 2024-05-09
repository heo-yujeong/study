<template>
  <div class="child">
    <h3>자식 페이지</h3>
    {{ child.name }}
  </div>
</template>

<script setup>
defineProps({
  child: Object
})
</script>

<style scoped>
.child {
  margin: 10px auto;
  padding-bottom: 20px;
  border: 1px solid #eee;
  background-color: #fff;
}
</style>