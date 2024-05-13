<template>
  <div class="main">
    <div class="main-content">
      <h1>유정이의 블로그</h1>
      <p>Welcome to my personal blog!</p>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.main {
  background-color: #f8f8f8;
  width: 100vw;
  height: 100vh;
  text-align: center;
}

.main-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.main-content > h1 {
  margin-bottom: 20px;
}
</style>