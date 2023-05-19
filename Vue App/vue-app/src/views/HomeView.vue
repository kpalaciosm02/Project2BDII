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
          { songName: 'TestName', songDuration: '03:00', songAuthor: 'TestAuthor'}
        ]
      }
    }
  }
</script>

<template>
  <SongPreview songName="Shape of you" songAuthor="Ed Sheeran" songDuration="03:45"></SongPreview>
</template>
  
<style>

</style>