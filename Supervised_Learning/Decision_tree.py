from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

# Features: [Temperature, Humidity]
X = np.array([
    [30, 70],   # Hot, humid → No
    [25, 65],   # Warm, not too humid → Yes
    [28, 90],   # Hot, very humid → No
    [22, 60],   # Cool, comfortable → Yes
    [18, 55],   # Cold, low humidity → No
    [22, 70],   # Cool, Humid  → Yes
    [24, 75],   # Mild, slightly humid → Yes
])

# Labels: 0= Stay Inside, 1= Play Outside
y = np.array([0, 1, 0, 1, 0, 1, 1])

model = DecisionTreeClassifier()
model.fit(X,y)

temp= int(input("Enter Temperature: "))
humidity= int(input("Enter Humidity: "))

prediction = model.predict([[temp,humidity]])[0]

if prediction == 1:
    print(f"Temperature: {temp}\tHumidity: {humidity} - Play Outside")
else:
    print(f"Temperature: {temp}\tHumidity: {humidity} - Stay Inside")