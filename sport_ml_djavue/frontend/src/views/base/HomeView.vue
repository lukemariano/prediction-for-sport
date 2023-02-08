<template>
  <div>
    <h1 class="mx-auto my-12 text-center" max-width="500">Predict Inputs</h1>
    <v-card class="mx-auto my-12" max-width="500" elevation="2" shaped>
      <form @submit.prevent="submit">
        <v-text-field v-model="name" label="Name" required></v-text-field>
        <v-text-field v-model="age" label="Age" type="number" required></v-text-field>
        <v-text-field v-model="height" label="Height" type="number" required></v-text-field>
        <v-select :items="items" label="Sex" dense required></v-select>
        <v-btn class="mr-4" type="submit" :disabled="invalid"> Make prediction </v-btn>
        <v-btn @click="clear"> clear fields</v-btn>
      </form>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    name: "",
    age: null,
    height: null,
  }),
  methods: {
    submit() {
      console.log("enviei", this.name)
    },
    clear() {
      this.name = ""
      this.age = null
    },
  },
}
</script>
