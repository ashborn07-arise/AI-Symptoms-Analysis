from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('symptom_model.pkl','rb'))
label_encoder = pickle.load(open('label_encoder.pkl','rb'))
symptoms = ['fever','cough','fatigue','headache','sore_throat','runny_nose','nausea','diarrhea']

@app.route('/')
def home():
    return render_template('index.html',symptoms=symptoms)

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [int(request.form.get(symptoms,0))for symptoms in symptoms]
    prediction = model.predict([input_features])[0]
    predicted_disease = label_encoder.inverse_transform([prediction])[0]


    return render_template('index.html',symptoms=symptoms,result=f"Predicted illness:{predicted_disease}")

if __name__ == '__main__':
   app.run(debug=True)
