'''
Base class-Parent Class
derived class-child class
1. Single level
2. Multi-level
3. Heirarchical
4. Multiple
'''
#Single level
# class Parent:
#     def pdisplay(self):
#         print("Parent property")
# class Child(Parent): 
#     def cdisplay(self):
#         print("Child property")
# obj=Child()
# obj.cdisplay()
# obj.pdisplay()

#multilevel
# class GrandParent:
#     def gpdisplay(self):
#         print("GrandParent property")
# class Parent(GrandParent):
#     def pdisplay(self):
#         print("Parent property")
# class Child(Parent):
#     def cdisplay(self):
#         print("Child property")
# obj=Child()
# obj.gpdisplay()
# obj.pdisplay()
# obj.cdisplay()

#heirarchical
# class Parent:
#     def pdisplay(self):
#       print("Parent property")
# class Child1(Parent):
#     def c1display(self):
#         print("Child 1 property")
# class Child2(Parent):
#     def c2display(self):
#         print("Child 2 property")
# class Child3(Parent):
#     def c3display(self):
#         print("Child 3 property")
# obj1=Child1()
# obj1.pdisplay()
# obj1.c1display()
# o2=Child2()
# o2.pdisplay()
# o2.c2display()

#multiple 
class Father:
    def fdisplay(self):
        print("Father property")
class Mother:
    def mdisplay(self):
        print("Mother property")
class Child(Father,Mother):
    def cdisplay(self):
        print("Child property")
obj=Child()
obj.fdisplay()
obj.mdisplay()
obj.cdisplay()