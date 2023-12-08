import math
import datetime
import calendar
#type conversion
a=int(input("Enter number"))
print(complex(a))
print(float(a))

#type coercion
print(5/6.0)#convert to float even though int

def circle(r):
    return math.pi*r*r

rad=int(input("Enter radius"))
print("Area of circle", circle(rad))


print(datetime.datetime.now())
print("Hour",datetime.datetime.now().hour)
print(calendar.month(2022, 9))

nums=[1,2,3,4,5]

res=list(filter(lambda x:x%2 !=0, nums))
sent="this is me"
res2=list(map(lambda x: x+"!!",sent.split()))
print(res2)

#help(list)
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
print("Recursive Factorial",fact(5))