'''
Python Code to implement the following inheritance example:
Classes: Employee, Developer, Tester, Manager.
Developer, tester, Manager inherit Employee.
Manager handles Developer, tester.
Manager class: implement functions to add Developer/Tester and Remove Developer/Tester.
Display to see the list of employees he manages.
'''
class Employee():
    def __init__(self,empName,eid,type):
        self.emp= empName
        self.id=eid
        self.job=type
    def info(self):
        print(f"{self.emp} with id {self.id} works as {self.job}")

class Dev(Employee):

class Manager(Employee):

    def __init__(self, empName, eid, type):
        super().__init__(empName, eid, type)
    def add(self, em)

class Tester(Employee):
