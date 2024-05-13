import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useProductStore = defineStore('product', () => {
  const productList = ref([
    {
      name: '상품 1',
      imagePath: 'src/assets/product1.png',
      price: 10000,
      isFavorite: false
    },
    {
      name: '상품 2',
      imagePath: 'src/assets/product2.png',
      price: 20000,
      isFavorite: false
    },
    {
      name: '상품 3',
      imagePath: 'src/assets/product3.png',
      price: 30000,
      isFavorite: false
    },
    {
      name: '상품 4',
      imagePath: 'src/assets/product4.png',
      price: 40000,
      isFavorite: false
    }
  ])

  const updateFavorite = function(productName) {
    productList.value.forEach((product) => {
      if (product.name === productName) {
        product.isFavorite = !product.isFavorite
      }
    })
  }

  const numOfFavorite = computed(() => {
    return productList.value.filter(product => product.isFavorite).length
  })

  return { productList, updateFavorite, numOfFavorite }
}, {persist: true})