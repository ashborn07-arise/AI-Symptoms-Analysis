import pandas as pd
import random

symptoms = ['fever','cough','fatigue','headache','sore_throat','runny_nose','nausea','diarrhea']
diseases = ['flu','cold','allergy','food_poisoning','covid']

data = []
for _ in range(200):
    entry = {symptom:random.randint(0,1) for symptom in symptoms}

    if entry['fever'] and entry['cough'] and entry['fatigue']:
        disease = 'flu'
    elif entry['sore_throat'] and entry['runny_nose']:
        disease = 'allergy'
    elif entry['nausea'] and entry['diarrhea']:
        disease = 'food_poisoing'
    elif entry['fever'] and entry['cough'] and entry['headache']:
        disease = 'covid'
    else:
        disease = random.choice(diseases)

    entry['disease'] = disease
    data.append(entry)

    df = pd.DataFrame(data)

    df.to_csv('symptom_data.csv', index = False) 
    print("Random dataset saved to symptom_data.csv")
