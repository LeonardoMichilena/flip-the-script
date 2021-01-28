# flip-the-script

## About project
![logoish](https://user-images.githubusercontent.com/60686512/105738115-fc422c80-5f36-11eb-8fd1-ef9b5cd870f9.PNG)

  
## About us
Flip the script is a team Web/App project developed by students from TechLabs Berlin.  
  
## Build Setup
### For the Flask app: 
#### Working with [python3](https://realpython.com/installing-python/)
#### Use package manager [pip](https://pip.pypa.io/en/stable/) to install [Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/)

###### First, cd into the python_app folder to activate your environment.
```bash
python3 -m venv venv
```
###### Next install the packages:
```bash
pip install requests
```
```bash
pip install Flask
```
###### To run the flask server:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### For express app:

Use package manager [npm](https://www.npmjs.com/) to install:
[express](https://expressjs.com/)
[axios](https://github.com/axios/axios)
[ejs](https://ejs.co/)
[method-override](https://www.npmjs.com/package/method-override)

```bash
npm install express axios ejs method-override
```
###### To run the Express server:
```bash
npm node index.js
```
