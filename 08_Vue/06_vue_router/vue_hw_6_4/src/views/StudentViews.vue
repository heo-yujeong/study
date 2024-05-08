<template>
  <div>
    <h1>학생 상세 정보 목록입니다.</h1>
    <p v-for="student in students" :key="student.name">
      <RouterLink :to="{name: 'student-detail', params: {name: student.name}}">
        {{ student.name }} 학생 정보 보기
      </RouterLink>
    </p>
  </div>
</template>

<script setup>
const students = [
  {name: '김하나'},
  {name: '김두리'},
  {name: '김서이'},
]
</script>

<style scoped>
</style>