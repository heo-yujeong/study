<template>
  <header>
    <div class="container">
      <div class="top">
        <h3>Quiz 퀴즈</h3>
      </div>
      <div class="bottom">
        <p>여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
      </div>
    </div>
    <nav>
      <RouterLink :to="{name: 'home'}">Home</RouterLink>
      <span> | </span>
    </nav>
  </header>
  <main>
    <RouterView />
  </main>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
header {
  margin: 10px auto 30px auto;
  width: 60%;
  text-align: center;
}

main {
  margin: 0 auto;
  width: 80%;
}

h3 {
  margin: 0;
}

nav {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #323232;
  color: white;
  height: 30px;
  font-size: 15px;
}

nav a {
  margin: 0 10px;
  text-decoration: none;
  color: white;
}

.container {
  border: 1px #eee solid;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 20px;
}

.top {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: orange;
  color: white;
  height: 50px;
}

.bottom {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70px;
  font-size: 13px;
}

.bottom > p {
  margin: 0 15px;
}
</style>
