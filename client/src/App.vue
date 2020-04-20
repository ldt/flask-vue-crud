<template>
  <div id="app">
    <nav-bar />
    <router-view />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";

export default {
  components: {
    NavBar
  }
};
</script>

<style>
#app {
  /* margin-top: 60px; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
