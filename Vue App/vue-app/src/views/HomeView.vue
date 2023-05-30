<script>
  import SongPreview from '../components/SongPreview.vue';
  import SongInfo from '../components/SongInfo.vue';
  import axios from 'axios';


  export default{
    name: 'HomeView',

    components: {
        SongPreview,
        SongInfo
      },
    data(){


      return {
        SongNameA:null,
        SongDurationA:null,
        songAuthorA:null,  
        SongGenreA:null,
        SongLyricsA:null,


        posts: [],

        songs : [
          
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
//----------------------------------------------------------------
//----------------------------------------------------------------
//----------------------------------------------------------------
      agregarFiltro(event){
        const selectedFilter = document.getElementById('filterName').value;
        if (!this.filters.includes(selectedFilter)){
          this.filters.push(selectedFilter);
        }
        else{
          alert("Este filtro ya se encuentra en el sistema.")
        }
      },

//----------------------------------------------------------------
//----------------------------------------------------------------
//----------------------------------------------------------------      
      deleteFilter(filter){
        const index = this.filters.indexOf(filter);
        if (index != -1){
          this.filters.splice(index, 1);
          document.getElementById("filterInput").value = "";
        }
        else{
          alert("El filtro a eliminar no existe.");
        }
      },
      toggleShowSong(song){
        this.songData = song;
        this.showSong = !this.showSong;
      },
//----------------------------------------------------------------
//----------------------------------------------------------------
//----------------------------------------------------------------

      ConstruirListaCancionesConFiltro(){

        this.obtenerConFiltro();
          this.songs = this.posts.map((item) => {
            return {
              songName: item.SName,
              songDuration: "3:46", // Obtener la duración de la canción desde el campo Lyric
              songAuthor: item.Artist,
              songLyrics: item.Lyric,
              songGenre: item.Genre
            };
          });
        
      },
//----------------------------------------------------------------
//----------------------------------------------------------------
//----------------------------------------------------------------

      ConstruirListaCancionesSinFiltro(){

        this.obtenerSinFiltro();
          this.songs = this.posts.map((item) => {
            return {
              songName: item.SName,
              songDuration: "3:46", // Obtener la duración de la canción desde el campo Lyric
              songAuthor: item.Artist,
              songLyrics: item.Lyric,
              songGenre: item.Genre

            };
          });
      },


//----------------------------------------------------------------
//----------------------------------------------------------------
//----------------------------------------------------------------
      obtenerConFiltro() {
        try {
            const inputs = document.querySelectorAll('.filterContainer .filterInput');
            const datos = Array.from(inputs).map(input => input.value);

            const data = {
              paths: this.filters,
              queries: datos,
              limit: 10,
              query_type: "phrase"
            };

            const headers = {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*'
            };

            axios.post('http://main-app.gentleflower-12982389.eastus.azurecontainerapps.io/mongo/search/filters', data, { headers })
            .then(response => {
                this.posts = response.data;
                console.log(response.data);
                console.log("-----------------");
                console.log("lista posts:");
                console.log(this.posts);
              })
              .catch(error => {
                // Manejar el error aquí
                console.error(error);
              });
            

        } catch (error) {
            console.error(error);
        }
      },
//----------------------------------------------------------------
//----------------------------------------------------------------
//----------------------------------------------------------------
       obtenerSinFiltro() {
        try {
            const inputs = document.querySelectorAll('.filterContainer .filterInput');
            const datos = Array.from(inputs).map(input => input.value);
            const data = {
              path: this.filters,
              query: datos,
              limit: 10,
              query_type: "phrase"
            };

            const headers = {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*'
            };

            axios.post('http://main-app.gentleflower-12982389.eastus.azurecontainerapps.io/mongo/search', data, { headers })
            .then(response => {
                this.posts = response.data;
                //this.songs.push({songName: "TestName", songDuration:"04:02", songAuthor:"TestAuthor"});
                console.log(response.data);
                console.log("-----------------");
                console.log("lista posts:");
                console.log(this.posts);

              })
              .catch(error => {
                // Manejar el error aquí
                console.error(error);
              });
            

        } catch (error) {
            console.error(error);
        }
      },
    }
  }
</script>

<template>
  <div class="bigContainer" v-if="!showSong">
    <div class="songsContainer">
      <div v-for="song in songs" class="songContainer">
        <SongPreview :songName="song.songName" :songAuthor="song.songAuthor" :songDuration="song.songDuration" @click="toggleShowSong(song)"></SongPreview>
      </div>  
    </div>
    
    <div class="filtersContainer">
      <label for="filterName" class="filterName">Seleccione un tipo de filtro</label>
      <select name="filterName" id="filterName" class="filterSelect">
        <option value="SName">Nombre de canciones</option>
        <option value="Artist">Artista</option>
        <!--<option value="lyrics">Lyrics</option>-->
        <option value="Genres">Género</option>
        <option value="language">Lenguaje</option>
        <option value="Popularity">Popularidad</option>
        <option value="Lyric">Letra</option>
      </select>
      <button class="filterButton" @click="agregarFiltro">+ Agregar filtro</button>
      <div v-for="filter in filters" class="filter">
        <div class="filterContainer">
          {{ filter }}
          <input type="text" placeholder="Inserte el dato a buscar con el filtro" class="filterInput" id="filterInput">
        </div>
        <div class="deleteButton" @click="deleteFilter(filter)">-</div>
      </div>
      <button type= "button" class="searchButton" @click="ConstruirListaCancionesConFiltro">Search with filter</button>
      <button type= "button" class="searchButton" @click="ConstruirListaCancionesSinFiltro">Search without filter</button>
      
    </div>
  </div>
  <div class="songContainer" v-if="showSong">
    <button class="searchButton2" @click="toggleShowSong(true)">X</button>
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
    cursor: pointer;
  }
  .searchButton2{
    width: 20px;
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
    cursor: pointer;
  }
</style>