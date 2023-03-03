import pandas as pd
import numpy as np
import random as rd
from sklearn.preprocessing import MinMaxScaler,StandardScaler
attribute_list =  ["a1n", "a2n", "a3n", "a4n", "a5n", "a6n", "a7n", "a8n", "a9d"]
dataframe= pd.read_csv("diabetes.txt", sep=" ", header=None)
info = pd.read_csv("_info-data-discrete.txt", sep=" ", header=None)

print(dataframe)
#ZAD3 
#a)
print("Symbole klas decyzyjnych:",pd.unique(dataframe[1]))
#b)
print("Wielkoś klas decyzyjnych:" ,info[2][1])
#c
print("Min wartość dostępnych atrybutów:")
for col in dataframe.columns:
    print(f"{col} : {dataframe[col].min()}")
print("Wartosci max atrybutów:")
for col in dataframe:
    print(col, ":", dataframe[col].max())
#d
print("Liczba różnych wartości dla wszystkich atrybutów:")
for idx, col in enumerate(dataframe.columns):
    print(f"{attribute_list[idx]}: {len(dataframe[col].unique())}")
#e
print("Lista różnych dostępnych wartości wszystkich atrybutów:")
for idx, col in enumerate(dataframe.columns):
    print(f"{attribute_list[idx]}: {list(dataframe[col].unique())}")
#f
print("odchyl standardowe dla wszystkich atrybutów:")
for col in range(0, 7):
    print(f"{attribute_list[col]} : {dataframe[col].std()}")


#4 a)
df_missing = dataframe.mask(np.random.random(dataframe.shape) < 0.1)
df_missing = df_missing.fillna('?')
most_common = df_missing.mode()
print("przed zamianą")
print(df_missing)
print("najczesciej wyst wartosci")
most_common = dataframe.mode()
print(dataframe.mode())
print("po zamianie")
df_imputed = df_missing.replace("?", most_common.iloc[0])
print(df_imputed)
#4b <-1,1>
print("Normalizacja danych <-1,1>")
scal = MinMaxScaler(feature_range=(-1, 1))
dn = pd.DataFrame(scal.fit_transform(dataframe), columns=dataframe.columns)
print(dn)
#4b (0,1)
print("Normalizacja danych <0,1>")
scal = MinMaxScaler(feature_range=(0, 1))
dn = pd.DataFrame(scal.fit_transform(dataframe), columns=dataframe.columns)
print(dn)
#4b (-10,10)
print("Normalizacja danych <-10,10>")
scaler = MinMaxScaler(feature_range=(0, 1))
dn = pd.DataFrame(scal.fit_transform(dataframe), columns=dataframe.columns)
print(dn)

#4c
print("Standaryzacja danych")
scaler = StandardScaler()
data_scaled = pd.DataFrame(scaler.fit_transform(dataframe), columns=dataframe.columns)
print(data_scaled.describe())
print(data_scaled.var())
print("dane po standaryzacji")
print(data_scaled)
#4d
new = pd.read_csv("Churn_Modelling.csv", sep=",")
new.head()
dr = pd.get_dummies(data=new,columns=['Geography'])
print(dr)
dr = dr.drop("Geography_France", axis=1)
print(dr)