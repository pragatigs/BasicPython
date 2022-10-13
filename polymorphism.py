#implementation of same method in different context
#overloading and overriding can achieve polymorphism
'''
2 types
1. Overloading
   a.Operator overloading
   b.Method overloading
2. Overriding
'''
#operator overloading
#'+' string(concatenation) and integer(addition)
#string
# n1='1'
# n2='2'
# print(n1+n2)

# #integer
# n1=1
# n2=2
# print(n1+n2)

# # '*' data structures(replication),integers(multiplication)
# #ds
# l=[10,20]
# print(l*3)
# #integers
# print(10*20)

#method overloading
# def add():
#     a=1
#     b=2
#     print(a+b)
# add()
# def add(c,d):
#     print(c+d)
# add(3,4)
# def add(x,y,z):
#     print(x+y+z)
# add(5,6,7)

#overriding
class Parent:
    a=10
    def display(self):
        print("Parent property")
class Child(Parent):
    a=30
    def display(self):
        print("Child property")

ob=Child()
print(ob.a)
ob.display()