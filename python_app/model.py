import numpy as np
import pickle
#from app import stats

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
user_input = [5, 7, 2]
user_input = np.array(user_input)
user_input = user_input.reshape(1,-1)

y_prediction = loaded_model.predict(user_input)
prediction = y_prediction[0]

# Prediction as a string
print(bias[prediction])
 

