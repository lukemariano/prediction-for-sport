const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const multer = require("multer");
const cookieParser = require("cookie-parser");

const base = require("./controllers/base");
const predicts = require("./controllers/predicts");

const YELLOW = "\x1b[33m%s\x1b[0m";
const WHITE = "\x1b[37m";

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(multer().array());
app.use(cookieParser());

//CONFIG
const PORT = process.env.APIMOCK_PORT || 8000;
const ORIGIN_URL = process.env.ORIGIN_URL || "http://localhost:3000";

app.use(cors({ credentials: true, origin: ORIGIN_URL }));

// BASE
app.get("dapau", base.dapau);

app.get("/api/predicts/list", predicts.find);

app.listen(PORT, () => {
  console.log(
    YELLOW,
    "🆙 API MOCK using express is running on port: " + PORT,
    WHITE
  );
});
