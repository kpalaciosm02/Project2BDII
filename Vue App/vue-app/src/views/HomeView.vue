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
        ],
        filters: [

        ]
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
</style>