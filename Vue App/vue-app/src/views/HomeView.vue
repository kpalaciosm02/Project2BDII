<script>
  import SongPreview from '../components/SongPreview.vue';
  export default{
    name: 'HomeView',
    components: {
      SongPreview
    },
    data(){
      return {
        songs : [
          { songName: 'Somebody that I used to know', songDuration: '04:03', songAuthor: 'Gotye'},
          { songName: 'Lose Yourself', songDuration: '05:24', songAuthor: 'Eminem'},
          { songName: 'Eye of the Beholder', songDuration: '06:26', songAuthor: 'Metallica'},
          { songName: 'Your Love', songDuration: '04:13', songAuthor: 'The Outfield'}
        ]
      }
    }
  }
</script>

<template>
  <div class="bigContainer">
    <div class="songsContainer">
      <div v-for="song in songs" class="songContainer">
        <SongPreview :songName="song.songName" :songAuthor="song.songAuthor" :songDuration="song.songDuration"></SongPreview>
      </div>  
    </div>
    
    <div class="filtersContainer">
      <label for="filterName" class="filterName">Seleccione un tipo de filtro</label>
      <select name="filterName" id="filterName" class="filterSelect">
        <option value="cancion">Canción</option>
        <option value="artista">Artista</option>
        <option value="lyrics">Lyrics</option>
        <option value="genero">Género</option>
        <option value="lenguaje">Lenguaje</option>
        <option value="popularidad">Popularidad</option>
      </select>
      <button class="filterButton">+ Agregar filtro</button>
    </div>
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
</style>