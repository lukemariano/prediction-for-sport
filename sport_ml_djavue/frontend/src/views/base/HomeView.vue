<template>
  <div>
    <div style="text-align: right">
      <v-btn @click="logout"><v-icon>mdi-logout</v-icon> Logout</v-btn>
    </div>
    <h1 class="mx-auto my-12 text-center" max-width="500">Predict Inputs</h1>
    <v-card class="mx-auto my-12" max-width="500" elevation="2" shaped>
      <v-form lazy-validation ref="form" v-model="valid">
        <v-text-field v-model="name" label="Name" required></v-text-field>
        <v-text-field
          v-model="age"
          label="Age"
          type="number"
          :rules="ageRules"
          required></v-text-field>
        <v-text-field
          :rules="heightRules"
          v-model="height"
          label="Height (in centimeters)"
          height
          required></v-text-field>
        <v-select :items="sex" label="Sex" v-model="sexSelected" dense :rules="sexRules"></v-select>
        <v-btn :disabled="!valid" class="mr-4" @click="validate"> Make prediction </v-btn>
        <v-btn @click="clear"> clear fields</v-btn>
      </v-form>
    </v-card>
    <div v-show="isMakePredict">
      {{ isMakePredict != null ? this.appStore.showSnackbar(`New forecast generated! !`) : "" }}
    </div>
  </div>
</template>

<script>
import api from "@/api/predict.api"
import { useAppStore } from "@/stores/appStore"
import AccountsApi from "@/api/accounts.api.js"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  setup() {
    const appStore = useAppStore()
    const accountsStore = useAccountsStore()
    return { appStore, accountsStore }
  },
  data: () => ({
    loading: false,
    name: null,
    age: null,
    height: null,
    sexSelected: null,
    sex: ["Male", "Female"],
    isMakePredict: null,
    valid: true,
    ageRules: [(v) => (v >= 5 && v <= 130) || "Age must be greater than or equal to 5"],
    heightRules: [
      (v) =>
        (v <= 300 && v >= 102) || "The minimum height is 102 cm and the maximum height is 300 cm",
    ],
    sexRules: [(v) => !!v || "Please select your gender"],
  }),
  methods: {
    async validate() {
      this.$refs.form.validate()
      console.log(this.$refs.form.validate())

      const model_inputs = {
        name: this.name,
        age: this.age,
        height: this.height / 100,
        sex: this.sexSelected == "Woman" ? 0 : 1,
      }
      const req = await api.makePredict(model_inputs)
      console.log(req)
      this.isMakePredict = true

      // clear fields
      this.name = ""
      this.age = null
      this.height = null
      this.sexSelected = null

      // redirect
      this.$router.push({ name: "base-predictions" })
    },
    clear() {
      this.$refs.form.resetValidation()
      this.name = ""
      this.age = null
      this.height = null
      this.sexSelected = null
    },

    logout() {
      this.loading = true
      AccountsApi.logout()
        .then(() => {
          this.accountsStore.clearLoggedUser()
          this.appStore.showSnackbar("Sessão encerrada!", "warning")
          this.$router.push({ name: "base-login" })
        })
        .finally(() => {
          this.loading = false
        })
    },
  },
}
</script>
