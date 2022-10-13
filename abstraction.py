#abstract class contains abstract methods and those methods only declare methods but do not define them. Objects can be created only for concrete class;hence abstract classes have to be inherited. hiding implementation details and showing only the essential details
from abc import ABC, abstractmethod

class AbstractDemo(ABC): #inherited
    #abstract method
    @abstractmethod
    def absFunc(self):
        None
class ConcreteClass(AbstractDemo):
    def absFunc(self):
        print("Abstract Function")
obj=ConcreteClass()
obj.absFunc()