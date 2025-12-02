import pandas as pd
s=pd.Series([1,2,3,4])
print(s)
a=pd.Series([10,20,30],index=['a','b','c'])
print(a)
print(a['b'])
b=pd.Series ({'a':1,'b':2,'c':3})
print(b)
w=pd.DataFrame({'name':['Alice','Bob','Smith'],'Age':[20,30,40],'city':['delhi','calicut','kochi']})
print(w)
data={'product':['apple','mango','graph','chery'],'price':[100,80,70,150],'quantity':[10,5,15,8]}
df=pd.DataFrame(data)
print(df)
dat=[['Alice','Kuttu','Thanku'],[20,30,27],['delhi','mumbai','kolkata']]
d=pd.DataFrame(dat)
print(d)
# df.groupby('city')