<template>
  <nav id="nav">
    <v-btn icon id="github"><v-icon>mdi-github</v-icon></v-btn>
    <router-link to="/">Home</router-link>
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
