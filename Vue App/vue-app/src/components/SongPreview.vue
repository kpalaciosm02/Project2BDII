<script lang="ts">
    interface ItemProps{
        songName: string,
        songDuration: string,
        songAuthor: string
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
            }
        }
    }
</script>

<template>
    <div class="songPreviewContainer">
        <p class="songName">{{ songName }}</p>
        <p class="songAuthor">{{ songAuthor }}</p>
        <p class="songDuration">{{ songDuration }}</p>
    </div>
</template>

<style>

</style>