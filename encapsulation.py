''''
2 scopes in python
1. Public
2.Python
'''
#public class
class Sample:
    a=10
    def encapFunc(self):
        print(self.a)
        print("Encapsulation")
obj=Sample()
obj.encapFunc()
print(obj.a)
private class
class Sample:
    __a=10
    def encapFunc(self):
        print(self.__a) #private variables(__)are accessed only from the methods of the class
        print("Encapsulation")
obj=Sample()
obj.encapFunc()