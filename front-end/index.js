const express = require('express');
const app = express();
const sass = require('node-sass');
const path = require('path');

sass.render({
  file: 'public'
}, function(err, result) { 
    console.log(result)
 });

app.use(express.static('public'))
app.set('public', path.join(__dirname,'/public'));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname,'/views'));

app.get('/', (req, res) => {
    res.render('home');
})
app.get('/post', (req, res) => {
   const result = res;
   console.log(result);

})

app.get('/flip', (req, res) => {
    res.render('flip');
})

app.post('/flip', (req,res) => {
    console.log(res);
})

app.listen(3000, () => {
    console.log('App is listening...');
})