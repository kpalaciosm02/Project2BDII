<script lang="ts">
  import LogIn from '../components/LogIn.vue'
  export default {
  name: 'App',
  components: {
    
    LogIn
    
  }}
</script>
  
<template>
  <main>
    <!--Agregar aca el componente a mostrar en el home (log in)-->
    <LogIn></LogIn>
  </main>
</template>

<style>
.LogIn{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
