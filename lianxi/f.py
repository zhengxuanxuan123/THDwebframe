class Person:
    def _init_(self,name):
        self.name=name
    def sayhello(self):
        print ('My name is:',self.name)
p1=Person('Bill')
p2 = Person('Apple')
print (p1)