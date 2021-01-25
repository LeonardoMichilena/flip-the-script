from flask import Flask, request, render_template
import requests
import json
import re
from collections import Counter
from countNeutral import neutral_converter, list_string, recounting 
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
    list_conversions = re.findall(list_string, textData)
    data={'article': text, 'changedWords': list_conversions}
    return(data)

@app.route("/stats", methods=["GET", "POST"])
def stats(): 
    print(request.data)
    stats=json.loads(request.data)
    print(stats)
    return("hello")
    
    
if __name__ == "__main__":
  app.run(port=5000, debug=True)