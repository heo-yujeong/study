<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList
      :products="products"
      @add-to-cart="addToCart"
    />

    <p>총 가격: {{totalPrice}}원</p>
    <h1>장바구니</h1>
    <Cart
      :cartProducts="cartProducts"
      @delete-cart="deleteCart"
    />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from '@/components/Cart.vue'

let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const cartProducts = ref([])

const addToCart = function(product) {
  cartProducts.value.push(product)
}

const deleteCart = function(index) {
  cartProducts.value.splice(index, 1)
}

const totalPrice = computed(() => {
  return cartProducts.value.reduce((acc, product) => acc+product.price, 0)
})
</script>
