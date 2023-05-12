<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="header">
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </div>
  <div>
    <RouterView />
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
</style>
