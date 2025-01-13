#write a python to calculate sum of any number of arguments
class test:
    def sum(self,*vector):
        total=0
        for i in vector:
            total=total+i
        print("sum of given values:\n",total)
obj=test()
obj.sum(10,20)
obj.sum(2,3,4,5,6,7,9,5,6,5,2,5,6,6,6,6,6,7,7,7,79,9,9,9,9)