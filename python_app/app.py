from flask import Flask, request, render_template
import requests
import json
import re
from collections import Counter 
from gender_function import pre_gender_converter, pron_converter
from neutral_function import neutral_converter, list_string 


app = Flask(__name__)



@app.route("/mascfem", methods=["POST"])
def jsInfo(): 
    data = json.loads(request.data)
    textData = data['article']
    text=pre_gender_converter(textData)
    text_converted = pron_converter(text)
    return(text_converted)

  


@app.route("/neutral", methods=["POST"])
def neutral():
    data = json.loads(request.data)
    textData = data['article']
    print("origional: ", textData)
    text=neutral_converter(textData)
    return(text)

@app.route("/stats", methods=["GET", "POST"])
def statistics(): 
    stats=json.loads(request.data)
    print(stats)
    statArray = [int(numeric_string) for numeric_string in stats]
    print(statArray)
    import numpy as np
    import pickle
    

    filename = 'finalized_model.sav'

    loaded_model = pickle.load(open(filename, 'rb'))

    src= {  "abc news": 1,
            "al jazeera": 2,
            "bbc news": 3,
            "cnn": 4,
            "deutsche welle": 5,
            "newsweek": 6,
            "reuters": 7,
            "the irish times": 8,
            "the new york times": 9,
            "science": 10,
            "cnbc": 11,
            "npr": 12        
            }

    tpc= {  "business": 1,
            "culture": 2,
            "food and drinks": 3,
            "local news": 4,
            "local news": 5,
            "people": 6,
            "politics": 7,
            "sports": 8,
            "technology": 9,
            "travel": 10,
            "world": 11,
            "social science": 12        
            }

    sex= {  "male": 0,
            "female": 1       
            }

    bias= { 0 :"non-biased",
            1: "slightly biased",
            2: "biased"      
            }

    # Array with user's selection, converting it into a numpy array and then reshaping it.
    user_input = statArray
    user_input = np.array(user_input)
    user_input = user_input.reshape(1,-1)

    y_prediction = loaded_model.predict(user_input)
    prediction = y_prediction[0]

    # Prediction as a string
    return(bias[prediction])
    
    
    
if __name__ == "__main__":
  app.run(port=5000, debug=True)