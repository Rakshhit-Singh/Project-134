import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('final2.csv')

distance=pd.to_numeric(df['Distance'],errors='coerce').dropna()

gravity=df['Gravity']

df=df[(distance<=100) & ((gravity>=150) & (gravity<=350))]

print("Solar systems of" , len(df), "stars are habitable")

df.to_csv("habitable.csv" ,index=False)