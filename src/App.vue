<template>
  <div id="app">
    <RPGPortfolio />
  </div>
</template>

<script>
import RPGPortfolio from './views/RPGPortfolio.vue'

export default {
  name: 'App',
  components: {
    RPGPortfolio
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: #0F0F0F;
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
}

body {
  overflow-x: hidden;
  overflow-y: auto;
}

html {
  scroll-behavior: smooth;
}
</style>