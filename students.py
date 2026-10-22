import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("students.csv")
#print(df)
#print(df.head()) 

#print(df.shape)
#print( df.info()) 
#print(df.describe())
#print(df.columns) 

#print(df["marks"]) 
#print(df[["name", "marks"]])
#print(df[df["marks"] > 80] )
#print(df[(df["city"] == "Chennai") & (df["age"] < 21)] )
print(df.loc[df["city"] == "Delhi"])