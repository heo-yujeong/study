<template>
  <div>
    <h3>보유 명함 목록</h3>
    <p v-if="numOfCard > 0">
      현재 보유중인 명함 수 : {{ numOfCard }}
    </p>
    <p v-else>
      명함이 없습니다. 새로운 명함을 추가해 주세요.
    </p>
    <BusinessCardDetail
      v-for="card in businessCards"
      :key="card.name"
      :card="card"
      @delete-card-event="DeleteCardEvent"
    />
  </div>
</template>

<script setup>
import {ref, computed} from 'vue'
import BusinessCardDetail from '@/components/BusinessCardDetail.vue'

const businessCards = ref([
  {name: '일론 머스크', title: '테슬라 테크노킹'},
  {name: '래리 엘리슨', title: '오라클 창업주'},
  {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
  {name: '래리 페이지', title: '구글 공동창업주'},
  {name: '세르게이 브린', title: '구글 공동창업주'},
])

const DeleteCardEvent = function(card) {
  businessCards.value = businessCards.value.filter((c) => c !== card)
}

const numOfCard = computed(() => {
  return businessCards.value.length
})
</script>

<style scoped>

</style>