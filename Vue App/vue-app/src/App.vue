<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="header">
    <nav>
      <RouterLink to="/">Login</RouterLink>
      <RouterLink to="/signup">SignUp</RouterLink>
      <RouterLink to="/main">Search</RouterLink>
    </nav>
  </div>

  <div>
    <RouterView> </RouterView>
  </div>
</template>

<style scoped>
  .header{
    height: 5vh;
    display: flex;
    border-bottom: 1px solid #000;
  }
  .header nav{
    display: flex;
  }
  RouterView{
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
