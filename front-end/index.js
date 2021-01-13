const express = require('express');
const app = express();
const path = require('path');

app.use(express.urlencoded({extended : true})); 

app.use(express.static('public'))
app.set('public', path.join(__dirname,'/public'));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname,'/views'));

app.get('/', (req, res) => {
    res.render('home');
})

app.get('/flip', (req, res) => {
    res.render('flip');
})

app.post('/flip', (req,res) => {
    const { script } = req.body;
    res.send(`Post flip response ${script}`);
})

app.listen(3000, () => {
    console.log('App is listening...');
})