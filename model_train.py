import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv('symptom_data.csv')

le = LabelEncoder()
df['disease'] = le.fit_transform(df['disease'])


with open('label_encoder.pkl','wb') as f:
    pickle.dump(le,f)

X = df.drop('disease',axis=1)
y = df['disease']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state = 42)


model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

with open('symptom_model.pkl','wb') as f:
    pickle.dump(model,f)

print("Logistic Regression model trained and saved.")    
