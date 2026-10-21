import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("students.csv")
course=pd.read_csv("course.csv")
print(df.head()) 
#print(df.shape)
df.info() 
df.describe() 
df.columns