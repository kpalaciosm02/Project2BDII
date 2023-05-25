<script lang="ts">
    interface SongProps{
        songName: string,
        songDuration: string,
        songAuthor: string,
        songLyrics: string,
        songGenre: string,
    }
    export default{
        props: {
            songName: {
                type: String,
                required: true
            },
            songDuration: {
                type: String,
                required: true
            },
            songAuthor: {
                type: String,
                required: true
            },
            songLyrics: {
                type: String,
                required: true
            },
            songGenre: {
                type: String,
                required: true
            }
        }
    }
</script>

<template>
    <div class="songInfoContainer">
        <p class="songName">{{ songName }}</p>
        <p class="songGenre">{{ songGenre }}</p>
        <p class="songAuthor">{{ songAuthor }}</p>
        <p class="songLyrics">{{ songLyrics }}</p>
        <p class="songDuration">{{ songDuration }}</p>
    </div>
</template>

<style>
    .songInfoContainer{
        width: 100%;
        height: auto;
        padding: 12px;
    }
    .songInfoContainer p{
        color: #bbe1fa;
    }
</style>