lis=[]

for i in range(5):
    lis.append(int(input("Enter number")))
print(lis)
lis.sort()#works in place
print("sorted",lis)
print("Count of 1=",lis.count(1))

lis1=lis.copy()

delindex=int(input("Enter index to delete"))
delitem=lis1.pop(delindex)


addindex=int(input("Enter index to insert"))
addele=input("Enter element to insert")
lis1.insert(addindex,addele)#index,element

print("Popped item",delitem)
print("New list",lis1)

remFirst=int(input("Enter element to remove"))
lis1.remove(remFirst)

print("After removing",lis1)
lis1.reverse()
print("Reverse list",lis1)#reverses order