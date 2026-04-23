import pandas as pd
data={
    "names":["Alice","Bob","Charlie","Akhil","Ema","Ann","Arun","lini"],
    "marks":[34,25,65,78,56,82,90,44]

}

df=pd.DataFrame(data)

print(df.loc[4],df.loc[7])