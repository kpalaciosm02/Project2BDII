<template>
  <main>
    <Signup></Signup>
  </main>

</template>

<script lang="ts">
import Signup from '../components/Signup.vue'
export default {
  name: 'App',
  components: {
    
    Signup
    
  }}
</script>
  
<style>
.Signup{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
