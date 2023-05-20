<template>
    <!-- Define que el documento esta bajo el estandar de HTML 5 -->
  
  <!-- Representa la raíz de un documento HTML o XHTML. Todos los demás elementos deben ser descendientes de este elemento. -->
  <html lang="es">
      
      <head>
          
          <meta charset="utf-8">
          
          <title> Filtrado de canciones </title>    
          
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          
          
          
      </head>
      
      <body>
      
          <h1>Filtrado de canciones</h1>
          <form id="loginform">
          
            <button type="button" id="botonBusqueda" @click="obtenerConFiltro"> 
              Get 
            </button>
          </form>
          
          <div>
            <h1>Posts</h1>
              <ul>
                <li v-for="post in posts" :key="post.id">
                    {{ post }}
                </li>
              </ul>
            <p v-if="error">{{ error }}</p>
      </div>

          
          

          
      </body>
  </html>   
  
  
  
  
    </template>
 
  <style>
  .body{
    background-color: #737a7e;
  }
  /* Estilo base para los inputs */
input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* Estilo para los inputs de tipo texto */
input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
}

/* Estilo para los inputs de tipo submit o botón */
input[type="submit"],
input[type="button"] {
  font-family: 'Overpass', sans-serif;
  font-size: 110%;
  color:#cccccc;
  width: 100%;
  height: 40px;
  border: none;
  
  border-radius: 3px 3px 3px 3px;
  -moz-border-radius: 3px 3px 3px 3px;
  -webkit-border-radius: 3px 3px 3px 3px;
  
  background-color: #376381;
  
  margin-top: 10px;
}



/* Cambiar estilo al pasar el mouse sobre los inputs de tipo submit o botón */
input[type="submit"]:hover,
input[type="button"]:hover {
  background-color: #45a049;
}

/* Estilo para los inputs deshabilitados */
input:disabled {
  background-color: #f2f2f2;
  cursor: not-allowed;
}

.mensaje1{
  color: rgb(248, 248, 248);
  
}
  
  </style>
  
  
  <script>
  
  import axios from 'axios';
  
  export default {
    name: 'mainPage',
  data() {
    return {
      posts: [],
      listaParametros: [],

      responseData: null,
      cancion: null,
      Artista: null,
      lyrics: null,
      genero: null,
      lenguaje: null,
      popularidad: null,
      

    };
  },

    
      methods: {
        async obtenerConFiltro() {
          const data = {
              paths: ["SName", "Artist"],
              queries: ["Love Of My Life", "queen"],
              limit: 2,
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
            })
            .catch(error => {
              console.log(error);
            });
        },

      async obtenerSinFiltro() {

        const data = {
              paths: ["SName", "Artist"],
              queries: ["Love Of My Life", "queen"],
              limit: 2,
              query_type: "phrase"
            };

          const headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          };
          axios.post('http://main-app.gentleflower-12982389.eastus.azurecontainerapps.io/mongo/search', data, { headers })
          

        .then(response => {
          this.posts = response.data;
              console.log(response.data);

        })
        .catch(error => {
          // Maneja los errores aquí
          console.error(error);
        });
      },


      async agregarFiltro(param){
        this.listaParametros.push();

      },
      async EliminarFiltro(param){
        this.listaParametros.push();

      }


        }
      }

      
    </script>
