class Employee:
    emp_name="Arya"
    emp_occ="App Developer"

    #most methods have self argument in class
    def info(self):
        print(f"{self.emp_name} is a {self.emp_occ}")

print(Employee.emp_name)
print(Employee.emp_occ)



a=Employee()
b=Employee() #object of class employee

a.emp_name="Pratham"
a.emp_occ="Web Developer"

b.emp_name="Mickey Mouse"
b.emp_occ="Dumbass"

a.info()
b.info() # access the info method through object of class

class Person():
    #parameterized constructor gets called when object is made
    def __init__(self,n,o):
        self.name=n
        self.age=o
    def info(self):
        print(f"{self.name} is {self.age} ")

a=Person("Pratham","20")
a.info()
del a.name# delete object
print(a.name)

