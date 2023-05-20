<template>
  <!-- Define que el documento esta bajo el estandar de HTML 5 -->

<!-- Representa la raíz de un documento HTML o XHTML. Todos los demás elementos deben ser descendientes de este elemento. -->
<html lang="es">
    
    <head>
        
        <meta charset="utf-8">
        
        <title> Formulario de Acceso </title>    
        
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        
        
    </head>
    
    <body>
        
        <div id="contenedor">
            <div id="central">
                <div id="login">
                    <div class="titulo">
                        Tp2
                    </div>
                    <form id="loginform">
                        <input type="email" name="usuario" placeholder="Usuario"  v-model="email">
                        
                        <input type="password" placeholder="Contraseña" name="password" autocomplete="current-password"  v-model="password">
                        
                        <button type="button" @click="signUp">Sign Up</button>
                    </form>

                   
                </div>
        
            </div>
        </div>
            
    </body>
</html>   




  </template>

<style>

body {
  font-family: 'Overpass', sans-serif;
  font-weight: normal;
  font-size: 100%;
  color: #1b262c;
  
  margin: 0;
  background-color: #0f4c75;
}

#contenedor {
  display: flex;
  align-items: center;
  justify-content: center;
  
  margin: 0;
  padding: 0;
  min-width: 100vw;
  min-height: 100vh;
  width: 100%;
  height: 100%;
}

#central {
  max-width: 320px;
  width: 100%;
}

.titulo {
  font-size: 250%;
  color:#bbe1fa;
  text-align: center;
  margin-bottom: 20px;
}

#login {
  width: 100%;
  padding: 50px 30px;
  background-color: #3282b8;
  
  -webkit-box-shadow: 0px 0px 5px 5px rgba(0,0,0,0.15);
  -moz-box-shadow: 0px 0px 5px 5px rgba(0,0,0,0.15);
  box-shadow: 0px 0px 5px 5px rgba(0,0,0,0.15);
  
  border-radius: 3px 3px 3px 3px;
  -moz-border-radius: 3px 3px 3px 3px;
  -webkit-border-radius: 3px 3px 3px 3px;
  
  box-sizing: border-box;
}

#login input {
  font-family: 'Overpass', sans-serif;
  font-size: 110%;
  color: #1b262c;
  
  display: block;
  width: 100%;
  height: 40px;
  
  margin-bottom: 10px;
  padding: 5px 5px 5px 10px;
  
  box-sizing: border-box;
  
  border: none;
  border-radius: 3px 3px 3px 3px;
  -moz-border-radius: 3px 3px 3px 3px;
  -webkit-border-radius: 3px 3px 3px 3px;
}

#login input::placeholder {
  font-family: 'Overpass', sans-serif;
  color: #E4E4E4;
}

#login button {
  font-family: 'Overpass', sans-serif;
  font-size: 110%;
  color:#1b262c;
  width: 100%;
  height: 40px;
  border: none;
  
  border-radius: 3px 3px 3px 3px;
  -moz-border-radius: 3px 3px 3px 3px;
  -webkit-border-radius: 3px 3px 3px 3px;
  
  background-color: #bbe1fa;
  
  margin-top: 10px;
}

#login button:hover {
  background-color: #0f4c75;
  color:#bbe1fa;
}

.pie-form {
  font-size: 90%;
  text-align: center;    
  margin-top: 15px;
}

.pie-form a {
  display: block;
  text-decoration: none;
  color: #bbe1fa;
  margin-bottom: 3px;
}

.pie-form a:hover {
  color: #0f4c75;
}

.inferior {
  margin-top: 10px;
  font-size: 90%;
  text-align: center;
}

.inferior a {
  display: block;
  text-decoration: none;
  color: #bbe1fa;
  margin-bottom: 3px;
}

.inferior a:hover {
  color: #3282b8;
}

</style>



<script>



import { initializeApp } from 'firebase/app';
import { getAuth, createUserWithEmailAndPassword} from 'firebase/auth';


  const firebaseConfig = {
    apiKey: "AIzaSyDL7BvGvYy_zFiae-U1MKlvc9fbSXdnn8E",
    authDomain: "proyectobd2-1ee28.firebaseapp.com",
    databaseURL: "https://proyectobd2-1ee28-default-rtdb.firebaseio.com",
    projectId: "proyectobd2-1ee28",
    storageBucket: "proyectobd2-1ee28.appspot.com",
    messagingSenderId: "953952352773",
    appId: "1:953952352773:web:93972982c0dc40300b3a6c"
    };

    const app = initializeApp(firebaseConfig);

    // Get auth object
    const auth = getAuth(app);

    
  export default {
    data() {
      return {
        currentUser: null,
        email: '',
        password: '',
      };
    },
    mounted() {
      // Suscribirse a cambios en la autenticación
      auth.onAuthStateChanged(user => {
        this.currentUser = user

        
      })


      
    },
    methods: {



      async signUp() {

        try { 
            
            const {userCredential}  = await createUserWithEmailAndPassword(auth, this.email, this.password)
            alert("Usuario Registrado");
            const user = userCredential.user;
            console.log('User created:', user);
            console.log("Usuario creado: " + user.email);

             
            } 
            catch(error) {
                   console.log(error.message)
                }
      }
  }
}
  </script>