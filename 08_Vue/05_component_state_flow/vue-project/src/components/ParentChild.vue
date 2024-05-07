<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild
      :my-msg="myMsg"
      @update-name="updateName"
    />
    <button @click="$emit('someEvent')">버튼1</button>
    <button @click="buttonClick">버튼2</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'
// defineProps(['myMsg'])

const props = defineProps({
  myMsg: {
    type: String,
    required: true
  },
  dynamicProps: String
})

console.log(props)
console.log(props.myMsg)

const emit = defineEmits(['myFocus', 'emitArgs', 'updateName'])
const buttonClick = function() {
  emit('myFocus')
}

const emitArgs = function() {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function() {
  emit('updateName')
}
</script>

<style scoped>
</style>