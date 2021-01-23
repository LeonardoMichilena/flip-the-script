from flask import Flask, request, render_template
import requests
import json
from neutral_function import neutral_converter 
from gender_function import gender_converter

app = Flask(__name__)



@app.route("/mascfem", methods=["POST"])
def jsInfo(): 
    data = json.loads(request.data)
    textData = data['article']
    text=gender_converter(textData)
    return(text)

  


@app.route("/neutral", methods=["POST"])
def neutral():
    data = json.loads(request.data)
    textData = data['article']
    text=neutral_converter(textData)
    return(text)


    
if __name__ == "__main__":
  app.run(port=5000, debug=True)