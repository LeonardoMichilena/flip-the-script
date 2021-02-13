# flip-the-script

![logi](https://user-images.githubusercontent.com/60686512/106793744-20e58500-6658-11eb-91a0-866f6c89f1b1.png)

  
## About us
We are Stephanie, Leticia, Leonardo and Luciana, a team of four motivated and engaged participants of TechLabs Berlin. We started Flip The Script because we recognized an issue in the way society sees gender. The way language works in our conscious and subconscious mind is often underestimated, and so is the way it affects how we perceive gender. </br>

Flip The Script is aimed to be used as a tool for change and education about our language use by offering users the option to consciously decide for a fairer language. Furthermore, we want to offer visitors the option to learn more about language use and patters and why it is important. You can find, on the statistics page, our results from collecting and analyzing news articles from various sources across the web. </br>

### What can you expect from our app? </br>
Our app presents itself as a text converter or, perhaps even, a text translator. A user can submit a text, whether  this is a news article you found on the web, a paper you wrote yourself, and anything else that involves text. The text is then returned back to the user in the possibility of two different forms. One, the user can choose to reverse all the pronouns. Two, the user can choose to change all pronouns to gender neutral. </br>

As well as the text conversion, you can explore our statistics page, which includes a deep look into the data we collected from Dec 2020 to Feb 2021. In this data, we explore how gendered language is represented in news articles from various sources across the web.  

## Build Setup
#### This guide requires a BASH shell. If you are using Windows, please visit the documentation for all linked dependencies for Windows commands. 
### For the Flask app: 
#### Working with [python3](https://realpython.com/installing-python/)
#### Use package manager [pip](https://pip.pypa.io/en/stable/) to install [Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/), [numpy](https://numpy.org/), and [Sklearn](https://scikit-learn.org/stable/)

###### First, cd into the python_app folder to activate your environment.
```bash
python3 -m venv venv
```
###### Next install the packages:
```bash
pip install requests
```
```bash
pip install scikit-learn
```
```bash
pip install numpy
```
```bash
pip install Flask
```
### To run the flask server:
###### Make sure you are in the python_app directory. 
Begin by activating your environment:</br>

```bash
source venv/bin/activate
```
Next, run run the Flask server:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### For express app:

Use package manager [npm](https://www.npmjs.com/) to install:</br>
[express](https://expressjs.com/)</br>
[axios](https://github.com/axios/axios)</br>
[ejs](https://ejs.co/)</br>
[method-override](https://www.npmjs.com/package/method-override)</br>

###### First, cd into the node_app folder set up your dependencies.

```bash
npm install express axios ejs method-override
```
### To run the Express server:
###### Make sure you are in the node_app directory.
```bash
npm node index.js
```
## How to use:
The site is hosted locally on your localhost:3000 and localhost:5000 </br>
Open two different consoles to get your servers running. 
##### Refer to [Build setup](#Build-setup)</br>

#### Now that your servers are running, open your browser to http://localhost:3000/


## Usage
Our text translator will convert your text in two ways. </br>
1. Gender binary=> from male to female, female to male. </br>
2. Gender neutral => gender neutral inclusive language. </br>
![textTranslator](https://user-images.githubusercontent.com/60686512/107754203-70474780-6d21-11eb-8525-6b46b2940259.PNG)

## Authors and acknowledgment
1. UX: [Luciana Wills](https://uxfol.io/sernawills)
2. DS: [Leticia Valladares](https://github.com/lavf)
3. WD: [Stephanie Mennear](https://github.com/Ostend)
4. WD: [Leo Michilena](https://github.com/LeonardoMichilena)

## Project status
We would all like to continue working on the project. 
We would like to build our database, extend our language dictionaries, and add features such as a google extension. 
Any help for collecting data and collaboration is welcome!
