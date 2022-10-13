# class Student:
#     usn=40
#     name="Pragati"
#     branch="ISE"
#     def display(self): #self is an argument that points to itself. It is mandatory. Also can access instance variables inside a method
#         print("Method inside the class")

# #object of the class
# s1=Student()
# s1.display()
# print("The USN is:",s1.usn)
# print("Name is:",s1.name)
# print("Branch is:",s1.branch)
# class MyClass:
#     n=40 #instance variable, defined within a class,is accessed by creating an instance(object)
#     a='abc'
#     def myFunc(self):
#         print(self.a)
#         n=50 #local variable
#         print("Inside myFunc")
#         print("Local variable n is",n)
#         print("Instance variable n is",self.n)
# obj=MyClass()
# print(obj.n)
# obj.myFunc()

#Python doesn't have a destructor ; contains only constructor

# class Sample:
#     #constructor to initialize the variables
#     def __init__(self,n1,n2):
#         self.num1=n1
#         self.num2=n2
#     def display(self):
#         print(self.num1,self.num2)
# obj=Sample(10,20)
# obj.display()

# class Sample:
#     def add(self,a,b):
#         self.n1=a
#         self.n2=b
#         print(self.n1+self.n2)
# obj=Sample()
# obj.add(40,60)
# ob=Sample()
# ob.add(4,6)
class Ise:
    def details(self,usn,name,age):
        self.usn=usn
        self.name=name
        self.age=age
        print("USN: {} \nName: {}\nAge: {}".format(self.usn,self.name,self.age))
ob1=Ise()
ob1.details(40,'Pragati',20)
ob2=Ise()
ob2.details(1,'Bob',21)