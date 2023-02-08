<template>
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
      <tr v-for="input in item" :key="input.name">
        <td>{{ input.name }}</td>
        <td>{{ input.age }}</td>
        <td>{{ input.height }}</td>
        <td>{{ input.sex }}</td>
        <td>{{ input.predict }}</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script>
import { api } from "@/api/predict.api"

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
