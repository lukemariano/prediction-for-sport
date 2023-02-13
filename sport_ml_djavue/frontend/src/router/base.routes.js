// Composables
import EmptyLayout from "@/layouts/default/EmptyLayout.vue"
import HomeView from "@/views/base/HomeView.vue"
import LoginView from "@/views/base/LoginView.vue"
import RegisterView from "@/views/base/RegisterView.vue"
import LogoutView from "@/views/base/LoginView.vue"

export default [
  {
    path: "/home",
    component: EmptyLayout,
    children: [
      {
        path: "",
        name: "base-home",
        component: HomeView,
      },
      {
        path: "/",
        name: "base-login",
        component: LoginView,
      },
      {
        path: "/register",
        name: "base-register",
        component: RegisterView,
      },
      {
        path: "/logout",
        name: "base-logout",
        component: LogoutView,
      },
    ],
  },
]
