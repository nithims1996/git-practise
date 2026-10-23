import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
students=pd.read_csv("students.csv")
#print(df)
#print(df.head())
#print(df.shape)
#print(students.tail())
#print(students[["name","marks"]])

#print(students[students["marks"]>=80])
print(students[students["city"]=="Mumbai"].sort_values("marks",ascending=False))