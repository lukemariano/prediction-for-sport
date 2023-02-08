const data = require("../data");

module.exports = {
  find: (req, res) => {
    const response = data.predicts;

    res.send(response);
  },
};
