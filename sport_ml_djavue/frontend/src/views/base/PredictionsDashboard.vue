<template>
  <div>
    <h1 class="text-center mb-6 mt-6 text-h3 font-weight-bold">Generated Predictions🔮</h1>
    <v-table class="mb-6">
      <thead>
        <tr style="background-color: #fdc200">
          <th class="text-left text-h5 text--color font-weight-bold">Name</th>
          <th class="text-left text-h5 text--color font-weight-bold">Age</th>
          <th class="text-left text-h5 text--color font-weight-bold">Height</th>
          <th class="text-left text-h5 text--color font-weight-bold">Sex</th>
          <th class="text-left text-h5 text--color font-weight-bold">Predict</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="input in item.predicts" :key="input.name">
          <td class="text-h6">{{ input.name }}</td>
          <td class="text-h6">{{ input.age }}</td>
          <td class="text-h6">{{ input.height }}</td>
          <td class="text-h6">{{ input.sex == 0 ? "Female" : "Male" }}</td>
          <td class="text-h6">{{ input.predictions }}</td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script>
import api from "@/api/predict.api"

export default {
  data() {
    return {
      item: [],
    }
  },

  async mounted() {
    this.item = await api.getPredicts()
  },
}
</script>

<style scoped>
.text--color {
  color: black !important;
}
</style>
