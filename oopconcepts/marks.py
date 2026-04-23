import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("marksexcel.csv")

print(df)

plt.bar(df["Name"],df["Marks"])
plt.xlabel("Names")
plt.ylabel("Marks")
plt.title("Student Marks Graph")

plt.show()
