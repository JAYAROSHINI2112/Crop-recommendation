import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv('cpdata.csv')
features=['temperature','humidity','ph','rainfall']
X=df[features]
df.label=LabelEncoder().fit_transform(df.label)
print(df.label.unique)
Y=df.label
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(X,Y)
preds=rf.predict(X)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(Y,preds))
print(confusion_matrix(Y,preds))
import pickle
with open('crop.pkl','wb') as f:
     pickle.dump(rf,f)
