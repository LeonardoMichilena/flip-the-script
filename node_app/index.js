  
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

//************************
//Counting function for difference
//between user string and python string
//*************************/
function diffWords(aString, bString){
    differentWords = [];
    var compare = aString.localeCompare(bString);
    if(compare === -1 || compare === 1){
        var aStringArray = aString.split(" ");
        var bStringArray = bString.split(" ");
        
        if(aStringArray.length > bStringArray.length){
            var long = aStringArray;
        }
        else{
            var long = bStringArray;
        }
        for(x=0; x<long.length; x++){
            if(bStringArray[x] != aStringArray[x]){
            differentWords.push(aStringArray[x]);
            }
        }
         //console.log("DIFFERENT WORDS: ", differentWords)
        }else{
            console.log("no changes")
            differentWords=["no changes"]
        }
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
/***************************
fem/masc path, send back to user
**************************** */
app.post('/articles', (req, res) => {
    const { article } = req.body; 
    const firstArticle = article;
    axios.post('http://127.0.0.1:5000/mascfem', { article })//////check for post request
    .then(function(response){
        diffWords(response.data,firstArticle);
        console.log(differentWords)
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
        console.log(response.data)
        diffWords(response.data.article, firstArticle)
        res.render("flip", {firstArticle: firstArticle, response: response.data.article, flippedArray: differentWords})//, flippedArray: differentWords})//, flippedArray: differentWords});
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
    const data=[source, topic, sex] 
    //res.render("home")
    axios.post("http://localhost:5000/stats", data)
    .then(function(response){
        res.render("home")
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