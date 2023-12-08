name=input("Enter your name: ")
print("Hello",name,sep="\n", end="!\n")

studentList=["Pratham"]
setA={"A","Arya"}
studentList.append(name)#appends an element to the end of the list.
setA.add(name)# element already exists, not added
def expo(x):
    return x**3
num=[1,2,3,4,5]
new_num=list(map(expo,num))

def characterCount(A):
    return len(A)
Sentence="I am in Third Year"
lis=list(map(characterCount,Sentence.split()))# list of no of charact
count=0
for letter in "AryaTelang":
    letter=letter.lower()
    if (letter=="a"or letter=="e"or letter=="i"or letter=="o"or letter=="u"):
        continue
    count+=1
print("Num of non vowels=",count)
print(studentList)
print(setA)
print(new_num)
print(lis)
