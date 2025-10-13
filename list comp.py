#list comprehension
#expression
numbers=[1,2,3,4,5]
square=[x**2 for x in numbers]
print(square)
words=["apple","banana","cherry"]
letters=[w[0] for w in words]
print(letters)
b=[w.upper() for w in words]
print(b)
print([len(w) for w in words])
#extract digit from a string
text="ab1c12"
digits=[ch for ch in text if ch.isdigit()]
print(digits)

data={"a":1,"b":2,"c":3}
keys=[k for k in data]
print(keys)