const data = require("../data");

module.exports = {
  find: (req, res) => {
    const response = data.predicts;
    res.send(response);
  },

  add: (req, res) => {
    const newPredict = req.body;
    console.log(req);
    data.predicts.push(newPredict);
    res.send(newPredict);
  },
};
