import EmptyLayout from "@/layouts/default/EmptyLayout.vue"
import PredictionsDashboard from "@/views/base/PredictionsDashboard"

export default [
  {
    path: "/predictions",
    component: EmptyLayout,
    children: [
      {
        path: "",
        name: "base-predictions",
        component: PredictionsDashboard,
      },
    ],
  },
]
