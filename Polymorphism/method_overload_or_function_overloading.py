#method overloading using older method
class test:
    def method1(self):
        print("no paramters")
    def method1(self,a):
        print("one paramter")
    def method1(self,a,b):
        a=20
        b=30
        print("two parameters",a+b)
    def method1(self,x,y,z):
        print("three parameters")
obj=test()
#obj.method1()
#obj.method1(10)
obj.method1(10,20)