export const api = {
  async getPredicts() {
    const response = await fetch(`http://localhost/api/predicts/list`)
    return await response.json()
  },
}
