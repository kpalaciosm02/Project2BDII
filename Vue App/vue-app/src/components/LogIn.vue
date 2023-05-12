<script lang="ts">
    export default{
        name: 'LogIn'
    }
</script>

<template>
    <h1>Log in</h1>
    <div class="inputContainer">
        <p class="userText">Username</p>
        <input type="text" class="textInput">
    </div>
    <div class="inputContainer">
        <p class="passwordText">Password</p>
        <input type="text" class="textInput">
    </div>
</template>

<style>
    .inputContainer{
        display: flex
    }
    .textInput{
        width: 400px;
        height: 32px;
        border: 1px solid #000;
        border-radius: 4px;
        padding: 4px;
    }
</style>