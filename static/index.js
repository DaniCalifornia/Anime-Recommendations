
const tiles = document.getElementById('container')
const list = document.createElement('ul');
const header = document.getElementById('header')
const loader = document.getElementById('loader')
const nav = document.getElementById('nav')

// popular anime (in my opinion)
const popularAnime = ['Naruto', 'One Piece', 'Death Note', 'Sword Art Online', 'Fairy Tale', 'My Hero Academia', 'Haikyuu!!', 'Hunter x Hunter', 'Cowboy Bepop', 'One Punch Man', 'Sailor Moon', 'Dragon Ball', 'Soul Eater', 'Yuri!!! on Ice', 'Bleach']
// array of tile colors
const colors = ['cyan', 'purple', 'pink', 'blue']

// create list of anime tiles
function animeList(arr) {
  arr.forEach((anime, idx) => {
    const li = document.createElement('li')
    li.textContent = anime;
    li.classList = `${colors[idx % 4]} tile`
    list.appendChild(li);
  })
  tiles.appendChild(list)
}


async function getRecs(anime) {
  // activate loading screen
  tiles.style.display = "none";
  nav.style.display = 'none';
  loader.classList = 'loading'
  // request recommendations for selected anime
  const res = await fetch(`/recommendations/${anime}`, {
    method: 'GET',
    headers: {
      'Access-Control-Allow-Origin': '*'
    }
  })
  const recs = await res.json()
  const recsArray = recs.recs
  // deactivate loading screen
  tiles.style.display = "inline";
  nav.style.display = "inline";
  loader.classList = 'loaded'
  header.innerText = `People who watched ${recsArray.shift()} also enjoyed:`
  // remove current anime tiles
  while(list.firstChild) {
    list.removeChild(list.firstChild)
  }
  // replace tiles with recommenation anime tiles
  animeList(recsArray)
}

tiles.addEventListener('click', (event) => {
  const tile = event.target
  if (tile.classList.contains('tile')) {
    getRecs(tile.innerText)
  }
})

list.classList = 'flex'

animeList(popularAnime)
