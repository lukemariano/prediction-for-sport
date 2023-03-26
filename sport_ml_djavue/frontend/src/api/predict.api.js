import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {
  async getPredicts() {
    const response = await api(`/api/predicts/list`)
    return await response.data
  },

  async makePredict(inputs) {
    const response = await api.post(`/api/predicts/add`, apiHelpers.dataToForm(inputs))
    console.log(response.data)
    return await response.data
  },

  async deletePredict(predict) {
    const response = await api.delete(`/api/predicts/delete`, { data: predict })
    return await response.data
  },
}