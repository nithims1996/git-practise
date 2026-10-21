scores = [78, 91, 55, 88] 
def grade(mark):
 if mark >= 85: return "A"
 if mark >= 70: return "B"
 return "C"
#print(grade(91))

df = pd.read_csv("students.csv")
df.head() # first 5 rows
df.shape # (rows, columns)
df.info() # column names, types, non-null counts
df.describe() # count, mean, min, max of number columns
df.columns