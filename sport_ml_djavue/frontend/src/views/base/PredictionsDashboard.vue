<template>
  <div>
    <h1 class="text-center mb-6 mt-6">Generated Predictions</h1>
    <v-table>
      <thead>
        <tr>
          <th class="text-left">Name</th>
          <th class="text-left">Age</th>
          <th class="text-left">Height</th>
          <th class="text-left">Sex</th>
          <th class="text-left">Predict</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="input in item.predicts" :key="input.name">
          <td>{{ input.name }}</td>
          <td>{{ input.age }}</td>
          <td>{{ input.height }}</td>
          <td>{{ input.sex == 0 ? "Female" : "Male" }}</td>
          <td>{{ input.predictions }}</td>
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
