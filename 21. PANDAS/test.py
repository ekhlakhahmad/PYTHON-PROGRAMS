import pandas as pd
df = pd.read_csv ("C:\\Users\\ekhla\\Desktop\\marksheet.csv")
row1 = df.loc[0]
print (row1)
print(df.head(3))