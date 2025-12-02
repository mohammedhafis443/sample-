import pandas as pd

df=pd.DataFrame({'name':['Alice','Bob','Smith'],'Age':[20,30,40],'city':['delhi','calicut','kochi']})
print(df)
df.groupby('city')

b=pd.DataFrame({'a':[1,2,None,4,5],'b':[6,None,7,8,9]})
print(b)
#forward fill
b_ffill=b.ffill()
print(b_ffill)
#backward fill
a_bfill=b.bfill()
print(a_bfill)
#drop rows 
a=b.dropna()
print(a)
#a1=b.dropna(axis=1)
#print(a1)
a2=b.fillna(0)
print(a2)
a3=b.fillna(b.mean())
print(a3)
