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
        <div class="left">
           <p class="songName">{{ songName }}</p>
        <p class="songAuthor">{{ songAuthor }}</p> 
        </div>
        <div class="right">
            <p class="songDuration">{{ songDuration }}</p>
        </div>
    </div>
</template>

<style>
    .songPreviewContainer{
        display: flex;
        border: 1px solid #bbe1fa;
        border-radius: 4px;
        padding: 8px 16px;
        height: auto;
        width: 480px;
    }
    .songName{
        font-family: 'Helvetica';
        font-size: 20px;
        line-height: 20px;
        color: #bbe1fa;
        margin-bottom: 4px;
    }
    .songAuthor{
        font-family: 'Helvetica';
        font-size: 16px;
        line-height: 16px;
        color: #bbe1fa
    }
    .songDuration{
        font-family: 'Helvetica';
        color: #bbe1fa;
        font-size: 12px;
        line-height: 12px;
        float: right;
    }
    .left{
        display: grid;
        width: 80%;
        justify-content: left;
        text-align: left;
    }
    .right{
        width: 20%;
        float: right;
        display: flex;
        align-items: center;
        text-align: right;
        justify-content: right;
    }
</style>