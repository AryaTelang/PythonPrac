#a=float(input("Enter num"))
#print(a**(0.5))

# Swapping of two numbers with and without using third variable.
x=2
y=3
x=x+y  #2+3=5
y=x-y  #5-3=2
x=x-y
print(x)
print(y)

for i in range(6):
    for j in range(i):
        print(" ",i,end="")
    print("\n")

n=5
fact=1
for i in range(n):
    fact=(i+1)*fact
print(fact)

n=123

if(n%2==0):
    print("even")
else:
    print("odd")

for letter in 'abcdefgh':
    pass
print("Last letter:", letter)
