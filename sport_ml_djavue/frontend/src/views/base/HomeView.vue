<template>
  <div>
    <h1 class="mx-auto my-12 text-center" max-width="500">Predict Inputs</h1>
    <v-card class="mx-auto my-12" max-width="500" elevation="2" shaped>
      <form @submit.prevent="submit">
        <v-text-field v-model="name" label="Name" required></v-text-field>
        <v-text-field v-model="age" label="Age" type="number" required></v-text-field>
        <v-text-field
          v-model="height"
          label="Height (in centimeters)"
          height
          required></v-text-field>
        <v-select :items="sex" label="Sex" v-model="sexSelected" dense></v-select>
        <v-btn class="mr-4" type="submit"> Make prediction </v-btn>
        <v-btn @click="clear"> clear fields</v-btn>
      </form>
    </v-card>
    <div v-show="isMakePredict">
      {{ isMakePredict != null ? this.appStore.showSnackbar(`Novo predict gerado !`) : "" }}
    </div>
  </div>
</template>

<script>
import api from "@/api/predict.api"
import { useAppStore } from "@/stores/appStore"

export default {
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data: () => ({
    name: null,
    age: null,
    height: null,
    sexSelected: null,
    sex: ["Male", "Woman"],
    isMakePredict: null,
  }),
  methods: {
    async submit() {
      const model_inputs = {
        name: this.name,
        age: this.age,
        height: this.height / 100,
        sex: this.sexSelected == "Woman" ? 0 : 1,
      }
      const req = await api.makePredict(model_inputs)
      console.log(req)
      this.isMakePredict = true
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
