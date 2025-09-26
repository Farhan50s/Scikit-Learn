from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([40,45,53,60,75])

model = LinearRegression()
model.fit(X,y)

hours =float(input("\nEnter Study hours To predict Marks: "))
predicted_marks = model.predict([[hours]])

print(f"Student after studing {hours} Gain {predicted_marks} ")