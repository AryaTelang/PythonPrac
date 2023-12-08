x=["arya",1,3.4,2+3j,1]
y=("aryaTelang",4)
z={"Arya":1,"Telang":2,"Bear":3}#no duplicates
a={"hey","this","is","set"}#unordered, unchangeable*, and unindexed.
binString=b"Hello"
k=None #null
for key in z.keys():
    print(key)
for val in z.values():
    print(val)
for i in range(len(x)):
    print(type(x[i]))
b=2
c=3
if(c>b and c>1 or c<7):# combine conditional statements
    print("hi")
if( c is not b):# compare the objects
    print("b is not C")
if("hey" in a):
    print("Hey present in set")




print("Exponential",b**c)
print("Floor",c//b)
print(binString)
print(type(binString))
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(z["Arya"])
print(y[1])