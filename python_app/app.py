from flask import Flask, request, render_template
import requests
import json
import re
from collections import Counter
# countNeutral import neutral_converter, list_string, recounting 
from gender_function import pre_gender_converter, pron_converter
from neutral_function import neutral_converter, list_string 

app = Flask(__name__)



@app.route("/mascfem", methods=["POST"])
def jsInfo(): 
    data = json.loads(request.data)
    textData = data['article']
    text=pre_gender_converter(textData)
    print(text)
    text_converted = pron_converter(text)
    print(text_converted)
    return(text_converted)

  


@app.route("/neutral", methods=["POST"])
def neutral():
    data = json.loads(request.data)
    textData = data['article']
    text=neutral_converter(textData)
    list_conversions = re.findall(list_string, textData)
    data={'article': text, 'changedWords': list_conversions}
    print(data)
    return(data)

@app.route("/stats", methods=["GET", "POST"])
def stats(): 
    print(request.data)
    stats=json.loads(request.data)
    print(stats)
    return("hello")
    
    
if __name__ == "__main__":
  app.run(port=5000, debug=True)