
const tiles = document.getElementById('container')
const list = document.createElement('ul');

// popular anime (in my opinion)
const popularAnime = ['Naruto', 'One Piece', 'Death Note']
// array of tile colors
const colors = ['cyan', 'purple', 'pink', 'blue']

// create list of anime tiles
function animeList(arr) {
  arr.forEach(anime => {
    const li = document.createElement('li')
    li.textContent = anime;
    li.classList = `${colors[Math.floor(Math.random() * 4)]} tile`
    list.appendChild(li);
  })
  tiles.appendChild(list)
}


async function getRecs(anime) {
  console.log('selected', anime)
  const res = await fetch(`/recommendations/${anime}`, {
    method: 'GET',
    headers: {
      'Access-Control-Allow-Origin': '*'
    }
  })
  console.log('request sent', res)
  const recs = await res.json()
  console.log('recs', recs.recs)

  while(list.firstChild) {
    list.removeChild(list.firstChild)
  }
  animeList(recs.recs)
}

tiles.addEventListener('click', (event) => {
  const tile = event.target
  if (tile.classList.contains('tile')) {
    console.log('innertext', tile.innerText)
    getRecs(tile.innerText)
  }
})

animeList(popularAnime)
