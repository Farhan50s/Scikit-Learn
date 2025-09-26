from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv('sample_data.csv')
df_label = df.copy()
le = LabelEncoder()

df_label['G'] = le.fit_transform(df_label['Gender'])
df_label['P'] = le.fit_transform(df_label['Passed'])
# df_label['City_encoded'] = le.fit_transform(df_label['City'])
# print("\n Label Encoded DataFrame:")
# print(df_label[["Name", "Gender",'G','Passed', 'P','City','City_encoded']])

# One Hot Encoding
df_encoded = pd.get_dummies(df_label, columns=['City'] ,dtype=int)
print("\n One Hot Encoded DataFrame:")
print(df_encoded.head())