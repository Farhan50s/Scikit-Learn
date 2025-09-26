from sklearn.neighbors import KNeighborsClassifier
import numpy as np
X = np.array([
    [7.0, 130],   # Small, light → Apple
    [7.5, 135],   # Small, light → Apple
    [8.0, 160],   # Medium → Apple
    [8.5, 180],   # Medium → Orange
    [9.0, 200],   # Larger → Orange
    [9.5, 220],   # Large, heavy → Orange
])

y = np.array([0,0,0,1,1,1])

model = KNeighborsClassifier(n_neighbors = 3)
model.fit(X,y)

Size = float(input("\nEnter the Size: "))
Weight = int(input("Enter the Weight: "))
prediction= model.predict([[Size,Weight]])[0]

if prediction ==0:
    print(f'According to Size: {Size} and Weight: {Weight} it is most likely an: Apple')
else:
    print(f'According to Size: {Size} and Weight: {Weight} it is most likely an: Orange')