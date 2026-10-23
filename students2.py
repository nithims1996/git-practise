import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("students.csv")
course=pd.read_csv("course.csv")
#print(df.sort_values("marks", ascending=False).head(3))
#print(df["grade"]== df["marks"].apply("grade"))
#(df["pass"]== df["marks"] >= 60)
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

df["grade"] = df["marks"].apply(grade)

#print(df[["marks", "grade"]])

#print( df.groupby("city")["marks"].mean())
#print(df.groupby("city").agg(students=("name","count"),avg_marks=("marks","mean")))

#print(df["city"].value_counts())

#print(df.isnull().sum())
#print(df["course_id"].fillna("Not enrolled")) 
#print(df.dropna(subset=["course_id"]) )
#print(pd.merge(students, courses,on ="course_id",how="inner"))


print(df.groupby("city")["marks"].mean().plot(kind="bar"))
plt.title("Average marks by city")
plt.ylabel("Marks")
plt.show()