import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {


  async deletePredict(inputs) {
    const response = await api.post(`/api/predicts/delete`, inputs)
    console.log(response.data)
    console.log(inputs)
    return await response.data
  },
}
