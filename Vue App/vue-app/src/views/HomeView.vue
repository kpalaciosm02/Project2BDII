<script>
  import SongPreview from '../components/SongPreview.vue';
  import SongInfo from '../components/SongInfo.vue';
  export default{
    name: 'HomeView',
    components: {
    SongPreview,
    SongInfo
},
    data(){
      return {
        songs : [
          { songName: 'Somebody that I used to know', songDuration: '04:03', songAuthor: 'Gotye'},
          { songName: 'Lose Yourself', songDuration: '05:24', songAuthor: 'Eminem'},
          { songName: 'Eye of the Beholder', songDuration: '06:26', songAuthor: 'Metallica'},
          { songName: 'Your Love', songDuration: '04:13', songAuthor: 'The Outfield'}
        ],
        filters: [

        ],
        songData: {
          songName: 'Somebody that I used to know',
          songGenre: 'Pop, Rock',
          songAuthor: 'Gotye',
          songLyrics: "Now and then I think of when we were together \nLike when you said you felt so happy you could die\nTold myself that you were right for me\nBut felt so lonely in your company\nBut that was love, and it's an ache I still remember",
          songDuration: '04:03'
        },
        showSong: false
      }
    },
    methods: {
      agregarFiltro(event){
        const selectedFilter = document.getElementById('filterName').value;
        if (!this.filters.includes(selectedFilter)){
          this.filters.push(selectedFilter);
        }
        else{
          alert("Este filtro ya se encuentra en el sistema.")
        }
      },
      deleteFilter(filter){
        const index = this.filters.indexOf(filter);
        if (index != -1){
          this.filters.splice(index, 1);
        }
        else{
          alert("El filtro a eliminar no existe.");
        }
      },
      toggleShowSong(){
        this.showSong = !this.showSong;
      }
    }
  }
</script>

<template>
  <div class="bigContainer" v-if="!showSong">
    <div class="songsContainer">
      <div v-for="song in songs" class="songContainer">
        <SongPreview :songName="song.songName" :songAuthor="song.songAuthor" :songDuration="song.songDuration" @click="toggleShowSong()"></SongPreview>
      </div>  
    </div>
    
    <div class="filtersContainer">
      <label for="filterName" class="filterName">Seleccione un tipo de filtro</label>
      <select name="filterName" id="filterName" class="filterSelect">
        <option value="Canciones">Número de canciones</option>
        <option value="Artista">Artista</option>
        <!--<option value="lyrics">Lyrics</option>-->
        <option value="Género">Género</option>
        <option value="Lenguaje">Lenguaje</option>
        <option value="Popularidad">Popularidad</option>
      </select>
      <button class="filterButton" @click="agregarFiltro">+ Agregar filtro</button>
      <div v-for="filter in filters" class="filter">
        <div class="filterContainer">
          {{ filter }}
          <input type="text" placeholder="Inserte el dato a buscar con el filtro" class="filterInput">
        </div>
        <div class="deleteButton" @click="deleteFilter(filter)">-</div>
      </div>
      <button class="searchButton">Search</button>
    </div>
  </div>
  <div class="songContainer" v-if="showSong">
    <SongInfo :songName="songData.songName" :songDuration="songData.songDuration" :songAuthor="songData.songAuthor" :songLyrics="songData.songLyrics" :songGenre="songData.songGenre"></SongInfo>
  </div>
</template>
  
<style>
  .bigContainer{
    width: 100%;
    height: auto;
    padding-top: 24px;
    display: flex;
  }

  .songsContainer{
    width: 50%;
    float: left;
  }

  .songContainer{
    height: auto;
    float: left;
    margin-bottom: 4px;
  }

  .filtersContainer{
    width: 50%;
    float: right;
    padding-left: 16px;
    padding-right: 16px;
  }

  .filterName{
    color: #bbe1fa;
    font-size: 16px;
  }

  .filterSelect{
    background-color: #181818;
    border: 1px solid #bbe1fa;
    border-radius: 4px;
    color: #bbe1fa;
    margin-left: 4px;
    cursor: pointer;
  }

  .filterButton{
    border: 1px solid #bbe1fa;
    border-radius: 4px;
    font-size: 14px;
    cursor: pointer;
    background-color: #181818;
    color: #bbe1fa;
    margin-left: 4px;
  }
  
  .filter{
    display: flex;
    width: 100%;
    height: auto;
    margin-left: 50px;
    margin-top: 12px;
  }

  .filterContainer{
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 24px;
    width: 80%;
    border: 1px solid #bbe1fa;
    border-radius: 4px;
    color: #bbe1fa;
    font-size: 16px;
    margin-top: 4px;
    padding-left: 6px;
  }

  .deleteButton{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 24px;
    width: 5%;
    border: 1px solid #bbe1fa;
    border-radius: 4px;
    color: #bbe1fa;
    font-size: 16px;
    margin-left: 40px;
    margin-top: 4px;
    cursor: pointer;
  }

  .filterInput{
    border: 1px solid #bbe1fa;
    border-radius: 4px;
    font-size: 14px;
    background-color: #181818;
    color: #bbe1fa;
    width: 75%;
  }

  .filterInput::placeholder{
    color: #bbe1fa;
  }

  .searchButton{
    width: 200px;
    height: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #bbe1fa;
    background-color: #181818;
    border: 1px solid #bbe1fa;
    border-radius: 4px;
    margin-top: 16px;
    margin-left: 150px;
  }
</style>