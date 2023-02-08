<template>
  <div>
    <h1 class="mx-auto my-12 text-center" max-width="500">Predict Inputs</h1>
    <v-card class="mx-auto my-12" max-width="500" elevation="2" shaped>
      <form @submit.prevent="submit">
        <v-text-field v-model="name" label="Name" required></v-text-field>
        <v-text-field v-model="age" label="Age" type="number" required></v-text-field>
        <v-text-field v-model="height" label="Height" type="number" required></v-text-field>
        <v-select :items="sex" label="Sex" v-model="sexSelected" dense></v-select>
        <v-btn class="mr-4" type="submit"> Make prediction </v-btn>
        <v-btn @click="clear"> clear fields</v-btn>
      </form>
    </v-card>
  </div>
</template>

<script>
import api from "@/api/predict.api"

export default {
  data: () => ({
    name: null,
    age: null,
    height: null,
    sexSelected: null,
    sex: ["Male", "Woman"],
  }),
  methods: {
    async submit() {
      const model_inputs = {
        name: this.name,
        age: this.age,
        height: this.height,
        sex: this.sexSelected,
      }
      const req = await api.makePredict(model_inputs)
    },
    clear() {
      this.name = ""
      this.age = null
      this.height = null
      this.sexSelected = null
    },
  },
}
</script>
