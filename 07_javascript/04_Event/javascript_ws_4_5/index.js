const playGame = (player1, player2) => {
  let count1 = 0
  let count2 = 0

  if (player1 === 'scissors') {
    if (player2 === 'rock') {
      count2 += 1
    } else if (player2 === 'paper') {
      count1 += 1
    }
  } else if (player1 === 'rock') {
    if (player2 === 'scissors') {
      count1 += 1
    } else if (player2 === 'paper') {
      count2 += 1
    }
  } else if (player1 === 'paper') {
    if (player2 === 'rock') {
      count1 += 1
    } else if (player2 === 'scissors') {
      count2 += 1
    }
  }

  if (count1 > count2) {
    return 1
  } else if (count1 < count2) {
    return 2
  } else {
    return 0
  }
}

const buttonClickHandler = (choice) => {
  const buttons = document.querySelectorAll('.button-box button')
  buttons.forEach((button) => {
    button.disabled = true
  })
  const player1Img = document.querySelector('#player1-img')
  const player2Img = document.querySelector('#player2-img')
  player1Img.src = `./img/${choice}.png`

  const choices = ['scissors', 'rock', 'paper']

  let randomIndex = Math.floor(Math.random() * 3)
  const player2Choice = choices[randomIndex]

  let intervalId = setInterval(() => {
    player2Img.src = `./img/${choices[randomIndex]}.png`
    randomIndex = (randomIndex + 1) % 3
  }, 100)

  setTimeout(() => {
    clearInterval(intervalId)
    const result = playGame(choice, player2Choice)
    player2Img.src = `./img/${player2Choice}.png`
    const modalContent = document.querySelector('.modal-content')
    if (result === 1) {
      modalContent.textContent = 'Player 1 wins!'
      document.querySelector('.countA').textContent++
    } else if (result === 2) {
      modalContent.textContent = 'Player 2 wins!'
      document.querySelector('.countB').textContent++
    } else {
      modalContent.textContent = 'It\'s a tie!'
    }
    document.querySelector('.modal').style.display = 'flex'

    setTimeout(() => {
      document.querySelector('.modal').style.display = 'none'
      buttons.forEach((button) => {
        button.disabled = false
      });
    }, 3000)
  }, 3000)
}

document.querySelector('#scissors-button').addEventListener('click', () => buttonClickHandler('scissors'))
document.querySelector('#rock-button').addEventListener('click', () => buttonClickHandler('rock'))
document.querySelector('#paper-button').addEventListener('click', () => buttonClickHandler('paper'))