<template>
  <div class="detail">
    <h1>가수 이름</h1>
    <div class="detail-img">
      <img src="@/assets/singer.jpg" alt="#" class="detail-img-img">
    </div>
    <p>가수 소개글</p>
  </div>
</template>

<script setup>

</script>

<style scoped>
.detail {
  text-align: center;
  padding: 20px;
  border: 1px solid black;
}

.detail-img {
  margin: 0 auto;
  width: 200px;
  height: 200px;
  border-radius: 70%;
  overflow: hidden;
}

.detail-img-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>





