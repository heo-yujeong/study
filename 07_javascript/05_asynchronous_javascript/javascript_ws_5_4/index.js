/* 
  아래에 코드를 작성해주세요.
*/
const API_URL = 'https://ws.audioscrobbler.com/2.0/'
const API_KEY = ''

const keyword = document.querySelector('.search-box__input')
const searchBtn = document.querySelector('.search-box__button')
const searchDiv = document.querySelector('.search-result')
const fetchAlbums = (page=1, limit=10) => {

  axios({
    method: 'get',
    url: API_URL,
    params: {
      method: 'album.search',
      album: keyword.value,
      api_key: API_KEY,
      format: 'json',
      page,
      limit
    }
  })
    .then((response) => {
      searchDiv.textContent = null
      const albums = response.data.results.albummatches.album
      return albums
    })
    .then((albums) => {
      albums.forEach(album => {
        const divCard = document.createElement('div')
        divCard.classList.add('search-result__card')
        
        const imgTag = document.createElement('img')
        imgTag.src = album.image[1]['#text']
        const divText = document.createElement('div')
        divText.classList.add('search-result__text')
        
        const h2Tag = document.createElement('h2')
        h2Tag.textContent = album.artist
        const pTag = document.createElement('p')
        pTag.textContent = album.name
        
        divText.appendChild(h2Tag)
        divText.appendChild(pTag)
        
        divCard.appendChild(imgTag)
        divCard.appendChild(divText)
        
        
        searchDiv.appendChild(divCard)
      })
    })
    .catch(() => {
      window.alert('잠시 후 다시 시도해주세요')
    })
}

searchBtn.addEventListener('click', fetchAlbums)