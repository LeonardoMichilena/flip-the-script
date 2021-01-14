const express = require("express");
const app = express();
const path = require("path");
const axios = require("axios");
const methodOverride = require("method-override");
//const request = require("request");
//const mongoose = require("mongoose");
//const AppError = require("./AppError");


//middleware
app.use(express.urlencoded({extended : true})); //NEED for parsing request body. but only set up to work with form data. 
app.use(express.json());
app.set("views", path.join(__dirname, "/views"));
app.set("view engine", "ejs");
app.use(methodOverride("_method"));

app.use(express.static('public'))
app.set('public', path.join(__dirname,'/public'));

//*****************
// HOME
//************* */ */
app.get('/', (req, res) => {
    res.render('home');
})

/* ********************************
empty list/form page step I
******************************** */
app.get('/flip', (req, res) => {
    articles = [];
    res.render('flip');
})
    

/***************************
fem/masc path, send back to user
**************************** */
app.get("/articles", (req, res) => {
    res.send({articles});
    console.log({articles}, "I am serving the articles data!!");
}) 

app.post('/articles', (req, res) => {
    console.log(req.body);
    const { article } = req.body;
    articles.push({article});
    console.log({articles}, "Post request!!!");
    axios.get('http://127.0.0.1:5000/mascfem')
    .then(function(response){
        console.log(response, "We got a response from PY!!");
        //res.send(response.data);
        res.render("flip", {response: response.data})
    })
    .catch(function(error){
        console.log("Error in rendering the view!");
    });
  
})
/* *****************************
    neutral path, send back to user
******************************** */
app.get("/neutralarticle", (req, res) => {
    res.send({articles})
    console.log({articles})
}) 

app.post('/neutralarticle', (req, res) => {
    console.log(req.body)
    const { article } = req.body;
    articles.push({article});
    console.log({articles});
    axios.get('http://127.0.0.1:5000/neutral')
    .then(function(response){
        console.log(response);
        //res.send(response.data);
        res.render("flip", {response: response.data});
    })
    .catch(function(error){
        console.log(error);
    });
    
  })
//******************************************************** */
//wrap the data to send to flask
//******************************************************** */
app.get("/show", (req, res) => {
    axios.get("http://localhost:3000/articles")
   .then(function (response) {
       console.log(response.data, "This is the response data!");
       res.send(response.data);
   })
   .catch(function (error) {
       console.log("There has been an error getting the data!");
   })   
})
app.get("/showneutral", (req, res) => {
    axios.get("http://localhost:3000/neutralarticle")
   .then(function (response) {
       console.log(response.data);
       res.send(response.data);
   })
   .catch(function (error) {
       console.log(error);
   })   
})

app.post('/flip', (req,res) => {
    const { script } = req.body;
    res.send(`Post flip response ${script}`);
})

app.listen(3000, () => {
    console.log('App is listening...');
})