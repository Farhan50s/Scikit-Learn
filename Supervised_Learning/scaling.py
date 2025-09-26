from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd

data= {
    "Hours":[1,2,3,4,6],
    "Scores":[40,45,50,55,65]
}

df = pd.DataFrame(data)

standardscaler = StandardScaler() #convert b/w -2 to 2
scaled = standardscaler.fit_transform(df)

minmax = MinMaxScaler() #convert b/w 0 to 1
scaled_minmax = minmax.fit_transform(df)

# print(pd.DataFrame(scaled, columns=["Hours", 'Scores']))
# print(pd.DataFrame(scaled_minmax, columns=["Hours", 'Scores']))

X = df[["Hours"]]
y = df[["Scores"]]

X_train, X_test, y_train, y_test = train_test_split(X ,y ,test_size=0.2 ,random_state=42)

print(X_test)
 
