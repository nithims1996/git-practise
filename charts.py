import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("students.csv")
course=pd.read_csv("course.csv")

print(df.groupby("city")["marks"].mean().plot(kind="bar"))
print(plt.title("Average marks by city"))
plt.ylabel("Marks")
plt.show()