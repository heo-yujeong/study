import { ref } from 'vue'
import { defineStore } from "pinia"

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      }
  ])

  const updateBalance = function(name) {
    const balance = balances.value.find((b) => b.name === name)
    return balance
  }

  const increaseBalance = function(name) {
    balances.value = balances.value.map((balance) => {
      if (balance.name === name) {
        balance.balance += 1000
      }
      return balance
    })
  }

  return { balances, updateBalance, increaseBalance }
})