<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="header">
    <nav>
      <!--<RouterLink to="/home" class="header-button">Home</RouterLink>
      <div class="vertical-line"></div>-->
      <RouterLink to="/about" class="header-button">About</RouterLink>
      <div class="vertical-line"></div>
      <RouterLink to="/signup" class="header-button">Sign Up</RouterLink>
      <div class="vertical-line"></div>
      <RouterLink to="/" class="header-button">Login</RouterLink>
    </nav>
  </div>
  <div>
    <RouterView />
  </div>
</template>

<style scoped>
  .header{
    height: 10vh;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #000;
  }
  .header nav{
    display: flex;
  }

  .header-button{
    height: 36px;
    width: auto;
    padding-left: 12px;
    padding-right: 12px;
    display: flex;
    align-items: center;
    border-radius: 4px;
    color: #bbe1fa;
    font-size: 24px;
  }
  div.vertical-line{
    width: 1px;
    background-color: #3282b8;
    height: 36px;
    float: left; 
  }
</style>
