from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

X = np.array([[1],[2],[3],[4],[5]])   #Hours of studies
y = np.array(["fail",'fail','pass','pass','pass'])    #Pass/ fail

#Encoding Fail/Pass into 0/1
encoder = LabelEncoder()
y_label = encoder.fit_transform(y)

model = LogisticRegression()
model.fit(X,y_label)
hours =float(input("\nEnter Study hours To predict Grade: "))
predicted_grade = model.predict([[hours]])[0]

if predicted_grade==0:
    print(f"Your estimate Grade after learning {hours} Hours is : Fail")
else:
    print(f"Your estimate Grade after learning {hours} Hours is : Pass")

