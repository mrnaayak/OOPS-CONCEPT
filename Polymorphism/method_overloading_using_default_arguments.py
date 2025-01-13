class test:
    def sum(self,a=None,b=None,c=None,d=None,e=None):
        if(a!=None and b!=None and c!=None and d!=None and e!=None):
            print("sum of 5 values:",a+b+c+d+e)
        elif(a!=None and b!=None and c!=None and d!=None):
            print("sum of 4 values:",a+b+c+d)
        elif(a!=None and b!=None and c!=None):
            print("sum of 3 values:",a+b+c)
        elif(a!=None and b!=None):
            print("sum of 2 values:",a+b)
        else:
            print("hey atleast two values required to perform any arithmetic operation")
obj=test()
obj.sum(10,20,30,40,50,60)
#NOTE:using default arguments concept for the
#method overloading resolve as many arguments u have
#defined in a method