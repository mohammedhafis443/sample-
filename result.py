import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie','ammu','anu'], 'mark1': [25,30,35,25,43],'mark2':[45,65,67,23,78]}
df = pd.DataFrame(data)
print(df)
df['total']=df['mark1']+df['mark2']
print(df)
# df.head()