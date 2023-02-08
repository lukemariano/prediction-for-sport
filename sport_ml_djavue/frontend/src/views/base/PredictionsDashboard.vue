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
      <tr v-for="item in desserts" :key="item.name">
        <td>{{ item.name }}</td>
        <td>{{ item.calories }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.calories }}</td>
        <td>{{ item.calories }}</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script>
export default {
  data() {
    return {
      desserts: [
        {
          name: "Frozen Yogurt",
          calories: 159,
        },
        {
          name: "Ice cream sandwich",
          calories: 237,
        },
        {
          name: "Eclair",
          calories: 262,
        },
        {
          name: "Cupcake",
          calories: 305,
        },
        {
          name: "Gingerbread",
          calories: 356,
        },
        {
          name: "Jelly bean",
          calories: 375,
        },
        {
          name: "Lollipop",
          calories: 392,
        },
        {
          name: "Honeycomb",
          calories: 408,
        },
        {
          name: "Donut",
          calories: 452,
        },
        {
          name: "KitKat",
          calories: 518,
        },
      ],
    }
  },
}
</script>
