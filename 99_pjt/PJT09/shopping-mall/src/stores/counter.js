import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCartStore = defineStore('cart', () => {
  const products = ref([])
  const carts = ref([])

  const getProducts = function() {
    axios({
      method: 'get',
      url: 'https://fakestoreapi.com/products'
    })
      .then((response) => {
        products.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const addCart = function(product) {
    carts.value.push(product)
  }

  const deleteCart = function(productId) {
    const idx = carts.value.findIndex(cart => cart.id === productId)
    if (idx !== -1) {
      carts.value.splice(idx, 1)
    }
  }

  return { products, carts, getProducts, addCart, deleteCart }
}, {persist: true})
