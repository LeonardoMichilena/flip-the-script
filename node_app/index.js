  
const express = require("express");
const app = express();
const path = require("path");
const axios = require("axios");
const methodOverride = require("method-override");


//middleware
app.use(express.urlencoded({extended : true})); //NEED for parsing request body. but only set up to work with form data. 
app.use(express.json());
app.set("views", path.join(__dirname, "/views"));
app.set("view engine", "ejs");
app.use(methodOverride("_method"));

app.use(express.static('public'))
app.set('public', path.join(__dirname,'/public'));


/*******************
 * Find the words that were flipped and isolate them into an array
 * /*******************/
 const convertedWordsArray = (a, b) => {
    const flippedWords = []
    for(let l of a) if(b.indexOf(l) == -1) flippedWords.push(l) 
    return(flippedWords);
}
 
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
    res.render('flip', {response : false});
});

app.get('/statistics', (req, res) => {
    res.render('statistics', {response : false});
});

app.get('/predictor', (req, res) => {
    res.render('predictor', {response : false});
});

app.get('/why-it-matters', (req, res) => {
    res.render('why-it-matters', {response : false});
});

app.get("/about", (req, res) => {
    res.render("aboutUs", {response : false});
});

/***************************
fem/masc path, send back to user
**************************** */
app.post('/articles', (req, res) => {
    const { article } = req.body; 
    const firstArticle = article;
    axios.post('http://127.0.0.1:5000/mascfem', { article })//////check for post request
    .then(function(response){
        differentWords = convertedWordsArray(response.data.split(" "), firstArticle.split(" "))
        res.render("flip", {firstArticle: firstArticle, response: response.data, flippedArray: differentWords}) 
    })
    .catch(function(error){
        console.log(error);
    });
})
/* *****************************
    neutral path, send back to user
******************************** */
  app.post('/neutralarticle', (req, res) => {
    const { article } = req.body; 
    const firstArticle = article;
    axios.post('http://127.0.0.1:5000/neutral', { article })
    .then(function(response){
        differentWords = convertedWordsArray(response.data.split(" "), firstArticle.split(" "))
        res.render("flip", {firstArticle: firstArticle, response: response.data, flippedArray: differentWords})//, flippedArray: differentWords})//, flippedArray: differentWords});
    })
    .catch(function(error){
        console.log(error);
    });   
  })


app.post('/articlecat', (req, res) => {
    console.log(req.body)
    const{source} = req.body;
    const{topic}= req.body;
    const{sex}=req.body; 
    const data=[source, topic, sex];
    axios.post("http://localhost:5000/stats", data)
    .then(function(response){
        console.log(response.data)
        res.render("predictor-result", {response: response.data})
    })
    .catch(function(error){
        console.log(error);
    });
  })
  
 
//*************

app.post('/flip', (req,res) => {
    const { script } = req.body;
    res.send(`Post flip response ${script}`);
});

app.listen(3000, () => {
    console.log('App is listening...');
});

