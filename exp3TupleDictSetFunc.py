marks=(11,23,24,15,11,11,23)
print(marks)
print("No of 11 =>",marks.count(11))
print("Index of 15=>",marks.index(15))

setA={"A","B","C","D"}
setB={"B","L","D"}
setC={"A","B","C","L"}
k=input("Enter for set A-")
if ( k not in setA):
    setA.add(k)
    print("Added")
else:
    print("Already present")
print("A-B",setA.difference(setB))
print("B-A",setB.difference(setA))
print("AUB",setB.union(setA))
print("A intersection B",setB.intersection(setA))

setC.add("Arya")
setC.discard("A") #remove() gives kye error this does not

print("Set C: ",setC)
setC.clear()
print("Empty",setC)

#kekw do for dictionary
