import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {
  async getPredicts() {
    const response = await api(`/api/predicts/list`)
    return await response.data
  },

  async makePredict(inputs) {
    console.log(inputs)
    const response = await api.post(`/api/predicts/add`, apiHelpers.dataToForm(inputs))
    console.log(response.data)
    return await response.data
  },
}
