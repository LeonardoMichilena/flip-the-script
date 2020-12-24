const express = require("express");
const app = express();
const path = require("path");
//const mongoose = require("mongoose");
const axios = require("axios");
//const request = require("request");
//const methodOverride = require("method-override");
//const AppError = require("./AppError");


//middleware
app.use(express.urlencoded({extended : true})); //NEED for parsing request body. but only set up to work with form data. 
app.use(express.json());
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");
//app.use(methodOverride("_method"));


app.get('/home', function(req, res) {
    axios.get('http://127.0.0.1:5000/flask')
    .then(function(response){
        console.log(response);
        res.send(response.data);
    })
    .catch(function(error){
        console.log(error);
    });
});

app.listen(3000, () => {
    console.log("App is listening on port 3000")
})