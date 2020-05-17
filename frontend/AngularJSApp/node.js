var express = require("express");
const path = require('path');

var app = express();

app.use(express.static(__dirname + '/public/'));

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", '*'); //<-- you can change this with a specific url like http://localhost:4200
    res.header("Access-Control-Allow-Credentials", true);
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
    res.header("Access-Control-Allow-Headers", 'Origin,X-Requested-With,Content-Type,Accept,content-type,application/json,*');
    next();
});

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/public/html/index.html');
});
app.listen(80);