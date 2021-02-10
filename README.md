# flip-the-script

## About project
![logi](https://user-images.githubusercontent.com/60686512/106793744-20e58500-6658-11eb-91a0-866f6c89f1b1.png)

  
## About us
Flip the script is a team Web/App project developed by students from TechLabs Berlin.  
  
## Build Setup
#build-setup
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
```bash
npm node index.js
```
## How to use:
The site is hosted locally on your localhost:3000 and localhost:5000 </br>
Open two different consoles to get your servers running. 
##### Refer to [Build setup](#Build-setup)</br>

#### Now that your servers are running, open your browser to http://localhost:3000/

## How to run on Windows
#build-setup
### For the Flask app: 
#### Working with [python3](https://realpython.com/installing-python/)
#### Use package manager [pip](https://pip.pypa.io/en/stable/) to install [Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/)

###### First, cd into the python_app folder to activate your environment.
```powershell
virtualenv --python C:\Path\To\Python\python.exe venv
```
###### Next install the packages:
```powershell
pip install requests
```
```powershell
pip install Flask
```
### To run the flask server:
###### Make sure you are in the python_app directory. 
Begin by activating your environment:</br>

```powershell
.\venv\Scripts\activate
```
Next, run run the Flask server:

```powershell
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

### For express app:

Use package manager [npm](https://www.npmjs.com/) to install:</br>
[express](https://expressjs.com/)</br>
[axios](https://github.com/axios/axios)</br>
[ejs](https://ejs.co/)</br>
[method-override](https://www.npmjs.com/package/method-override)</br>

###### First, cd into the node_app folder set up your dependencies.

```powershell
npm install express axios ejs method-override
```
### To run the Express server:
```powershell
node index.js
```
## How to use:
The site is hosted locally on your localhost:3000 and localhost:5000 </br>
Open two different consoles to get your servers running. 
##### Refer to [Build setup](#Build-setup)</br>

#### Now that your servers are running, open your browser to http://localhost:3000/

