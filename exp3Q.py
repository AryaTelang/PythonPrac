def histogram(l):
    s={}
    lis=[]

    cpSet=set(l)#remove all duplicates 
    
    for i in cpSet :
        lis.append({i,l.count(i)})
    print(lis)
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    return sum

def towerOfHanoi():

histogram([1,2,3,1,2,3,4,5])
print(perfect(28))
histogram([13,12,11,13,14,13,7,7,13,14,12])
