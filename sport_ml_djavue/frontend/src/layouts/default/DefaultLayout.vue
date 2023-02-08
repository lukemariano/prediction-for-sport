<template>
  <VLayout>
    <app-error-dialog :show="showErrorMessage" :message="errorMessage" @close="closeErrorDialog" />
    <app-snackbar />
    <VApp :theme="theme">
      <app-nav-bar :theme="theme" @theme-click="onThemeClick"></app-nav-bar>
      <VMain>
        <RouterView />
      </VMain>
      <app-footer :fixed="true" />
    </VApp>
  </VLayout>
</template>

<script setup>
import { ref } from "vue"

const theme = ref("dark")

function onThemeClick() {
  theme.value = theme.value === "light" ? "dark" : "light"
}
</script>

<script>
import { mapState } from "pinia"
import { useAppStore } from "@/stores/appStore"
import AppSnackbar from "@/components/AppSnackbar.vue"
import AppErrorDialog from "@/components/AppErrorDialog.vue"
import AppNavBar from "@/components/AppNavBar.vue"
import AppFooter from "@/components/AppFooter.vue"

export default {
  name: "DefaultLayout",
  components: {
    AppSnackbar,
    AppErrorDialog,
    AppNavBar,
    AppFooter,
  },
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  computed: {
    ...mapState(useAppStore, ["errorMessage", "showErrorMessage"]),
  },
  methods: {
    closeErrorDialog() {
      this.appStore.setShowErrorMessage(null)
    },
  },
}
</script>
