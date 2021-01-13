const express = require("express");
const app = express();
const path = require("path");
const axios = require("axios");
const methodOverride = require("express-method-override");
//const AppError = require("./AppError");


//middleware
app.use(express.urlencoded({extended : true})); //NEED for parsing request body. but only set up to work with form data. 
app.use(express.json()); //parses the data in the post form!!
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");
app.use(methodOverride("_method"));




/* ********************************
empty list/form page step I
******************************** */
 app.get("/home", (req, res) => {
    res.render('home')
    articles = [

    ]
})

//******************************************************** */
//after python has reversed it, call the python http port
//******************************************************** */

app.get('/reversed', function(req, res) {
    axios.get('http://127.0.0.1:5000/mascfem')
    .then(function(response){
        console.log(response);
        //res.send(response.data);
        res.render("new", {reversed: response.data})
    })
    .catch(function(error){
        console.log(error);
    });
    
});  

app.get('/neutral', function(req, res) {
    axios.get('http://127.0.0.1:5000/neutral')
    .then(function(response){
        console.log(response);
        //res.send(response.data);
        res.render("new", {reversed: response.data})
    })
    .catch(function(error){
        console.log(error);
    });
    
});  

/***************************
fem/masc path, send back to user
**************************** */
app.get("/articles", (req, res) => {
       res.send({articles})
    console.log({articles})
}) 

app.post('/articles', (req, res) => {
    console.log(req.body)
    const { article } = req.body;
    articles.push({article})
    console.log({articles})
    res.redirect("/reversed")
  
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
    articles.push({article})
    console.log({articles})
    res.redirect("/neutral")
  })
//******************************************************** */
//wrap the data to send to flask
//******************************************************** */
app.get("/show", (req, res) => {
    axios.get("http://localhost:3000/articles")
   .then(function (response) {
       console.log(response.data);
       res.send(response.data);
   })
   .catch(function (error) {
       console.log(error);
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

app.listen(3000, () => {
    console.log("App is listening on port 3000")
})