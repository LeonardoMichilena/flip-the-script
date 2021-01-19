from flask import Flask, request, render_template
import requests
import json
from neutral import neutral_converter
from gender import flip_the_script

app = Flask(__name__)



@app.route("/mascfem", methods=["POST"])
def jsInfo(): 
    data = json.loads(request.data)
    textData = data['article']
    text=flip_the_script(textData)
    return(text)

  


@app.route("/neutral", methods=["POST"])
def neutral():
    data = json.loads(request.data)
    textData = data['article']
    text=neutral_converter(textData)
    return(text)


    
if __name__ == "__main__":
  app.run(port=5000, debug=True)