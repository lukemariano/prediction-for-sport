<template>
  <nav id="nav">
    <div id="github" class="font-weight-bold">
      <v-btn icon href="https://github.com/lukemariano/" target="_blank"
        ><v-icon>mdi-github</v-icon></v-btn
      >By: Lucas Mariano
    </div>
    <router-link to="/home">Home</router-link>
    <router-link to="/predictions">Predictions</router-link>
  </nav>
</template>

<script>
export default {}
</script>

<style scoped>
#nav {
  background-color: #222;
  border-bottom: 4px solid #111;
  padding: 15px 50px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
#nav #github {
  margin: auto;
  margin-left: 0;
}
#logo {
  width: 40px;
  height: 40px;
}
#nav a {
  color: #fcba03;
  text-decoration: none;
  margin: 12px;
  transition: 0.5s;
}
#nav a:hover {
  color: #fff;
}
</style>
