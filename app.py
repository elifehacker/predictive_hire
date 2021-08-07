from flask import Flask, jsonify, request
import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import json  
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Define a function to clean the text
def clean(text):
# Removes all special characters and numericals leaving the alphabets
    text = re.sub('[^A-Za-z]+', ' ', text)
    return text

def is_positive(text) -> bool:
    """True if tweet has positive compound sentiment, False otherwise."""
    if sia.polarity_scores(text)["compound"] > 0:
        return 1
    return 0


le = preprocessing.LabelEncoder()

data=pd.read_csv("sample_dataset.csv")
data = data[data['selected'] != -1]
print(data.head(3))

uniquejobs = data['job_family'].unique()

print(uniquejobs)

le_gender = preprocessing.LabelEncoder()
gender = data['gender'].to_list()
le_gender.fit(gender)
data['gender_code'] = le_gender.transform(gender)

le_job = preprocessing.LabelEncoder()
job_family = data['job_family'].to_list()
le_job.fit(job_family)
data['job_code'] = le_job.transform(job_family)

data['cleaned_resp'] = data['text_response'].apply(clean)
data['sentiment'] = data['cleaned_resp'].apply(is_positive)

input_columns = ['MCQ_A10','MCQ_A11','MCQ_A13','MCQ_A14','MCQ_A15','MCQ_A18','MCQ_A2','MCQ_A20','MCQ_B7','MCQ_B76','MCQ_B78','MCQ_B79','MCQ_B8','MCQ_B82','MCQ_B85','MCQ_B89','MCQ_B90','MCQ_B91','MCQ_B95','MCQ_B98','job_code','gender_code', 'sentiment']

model = RandomForestClassifier()
x_train = data[input_columns]
y_train = data['selected']
model.fit(x_train, y_train)

app = Flask(__name__, static_url_path="")

'''
test with below cmd in the same directory as the app.py file
curl -vX POST http://localhost:5000/api/selected -d @payload.json --header "Content-Type: application/json"
'''
@app.route('/api/selected', methods=['GET', 'POST'])
def get_avgs():
    #print("get request")
    """ 
    s = dict()
    for c in input_columns:
        s[c] = [0,3]
    print(json.dumps(s, indent = 4)) 
    """
    content = request.json
    content["job_code"] = le_job.transform(content["job_family"])
    content["gender_code"] = le_gender.transform(content["gender"])
    content['sentiment'] = list()
    for text in content["text_response"]:
        content['sentiment'].append(is_positive(clean(text)))
    test_input = pd.DataFrame(content)
    test_input = test_input[input_columns]
    print(test_input.head())
    pred =  model.predict(test_input)
    print(pred)
    return jsonify({'selected': np.array_str(pred)})

if __name__ == '__main__':
    app.run(debug=True)

'''
pipreqs .
pip install -r requirements.txt
docker build --tag python-docker .
docker run -p 5000:5000 python-docker
'''