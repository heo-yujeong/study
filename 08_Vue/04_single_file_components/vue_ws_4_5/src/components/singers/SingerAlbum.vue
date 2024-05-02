<template>
  <div class="album">
    <h3>앨범 제목</h3>
    <p>노래 제목 1</p>
    <p>노래 제목 2</p>
    <p>노래 제목 3</p>
  </div>
</template>

<script setup>

</script>

<style scoped>
.album {
  background-color: #eee;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin: 10px 10px;
  padding: 0 10px;
  box-shadow: 0px 0px 3px #ccc;
}

.album > p {
  color: orangered;
}
</style>