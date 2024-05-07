<template>
  <header>
    <h1>명함 관리 페이지</h1>
  </header>
  <main>
    <article>
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </article>
  </main>
  <footer>
    © 2024 My Business Cards
  </footer>
</template>

<script setup>

</script>

<style scoped>
header {
  display: flex;
  width: fit-content;
  padding: 15px;
  margin: 20px auto;
  background-color: dodgerblue;
  color: #fff;
}

main {
  text-align: center
}

footer {
  display: flex;
  width: 100%;
  height: 80px;
  position: absolute;
  bottom: 0;
  align-items: center;
  justify-content: center;
  background-color: #eee;
}
</style>