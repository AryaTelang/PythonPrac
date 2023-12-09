f= open('myfile.txt','r')
k= open('myfile2.text','w')
j= open('myfile2.text','a')
import os
# the w mode creates file if not existing
#r for read,w for write, append a, keep modes and function

text=f.read(2)#how many characters one wants to return.

k.write("This text has been added from exp6")
j.write(" append mode")

print(text)
#By calling readline() two times, you can read the two first lines.
print(f.readline())

z=open("todelete.text",'w')
z.close()
os.remove("todelete.text")
#make a todelete file to see
if os.path.exists("todelete.text"):
    z.close()
    os.remove("todelete.text")
else:
    print("File doesnt exist")
    
#make a deletefol folder to see
if os.path.exists("deletefol"):
    os.rmdir("deletefol")
else:
    print("folder doesnt exist")

j.close()
f.close()
k.close()