<template>
  <NavBar />
  <router-view />
</template>

<script>
//

import NavBar from "@/components/AppNavBar.vue"

export default {
  components: {
    NavBar,
  },
}
</script>
