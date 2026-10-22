import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("students.csv")

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

print(df[["marks", "grade"]])

# df.groupby("city")["marks"].mean()
# df.groupby("city").agg(students=("name","count"),
# avg_marks=("marks","mean"))

# df["city"].value_counts()

# df.isnull().sum() # how many blanks per column
# df["course_id"].fillna("Not enrolled") # replace blanks
# df.dropna(subset=["course_id"]) # drop those rows
# pd.merge(students, courses, on="course_id",)