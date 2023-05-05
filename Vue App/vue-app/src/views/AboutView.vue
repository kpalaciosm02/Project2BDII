<script lang="ts">
  export default{
    name: 'AboutView'
  }
</script>

<template>
  <div class="about">
    <h1>This is a vue app for music visualization running on a docker container</h1>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100%;
    display: flex;
    align-items: center;
  }
}
</style>
