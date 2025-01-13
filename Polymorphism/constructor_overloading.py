#constructor is used to initialize members of
#of the class as instance variables
#method1: using formal way to implement constructor overloading
class test:
    def __init__(self):
        print("a constructor withour arguments")
    def __init__(self,a):
        print("a constructor with one argument")
    def __init__(self,a,b):
        print("a constructor with two argumets")
    def __init__(self,a,b,c):
        print("a constructor with three arguments")
obj=test(10,20,10)#we are calling constructor without any argument





#method2: implementation of constructor overloading using
#default arguments concept
'''class test:
    def _init_(self,a=None,b=None,c=None):
        print("with default arguments concept, a constructor is called for specified no.of arguments")

obj=test(10,20,30,40)'''
#=========================================================================
'''METHOD3: implmentation of constructor overloading with variable length arguments'''
class test:
    def __init__(self,*vector):
        print("constructor is called for any no.of arguments ")
#create an object
obj=test(10,20,2,3,4,5,67,7,9,2,3,5,4,6,4,5,5,6,2,5,7,7,2,3,25,2)





'''METHOD OVERRIDING CONCEPT:
---------------------------
--This is concept is applicable when the program
follows inheritance concept.
--overriding means overwriting.
ex: class rbi:
        def rate_of_interest_house_loan(self):
            roi=8.5
        def roi_for_car_loan():
             roi=9
        def roi_for_crop_loan():
            roi=11

    class hdfc(rbi):=----=---=-----=-=-----------------------------------------------------==================================================================================================================================================-==--=-=-----=--=-==-====-=-=-===================-----=---=----------=----=----=-=----=-------==-===================================================================================================================================================================================================================================================================================================================================================================================================================================-=-=-==-----------------------------------------------------------------------------------------------------------------------------------------------------------------=---=--===-=---=
        def rate_of_interest_house_loan(self):
            roi=8.5
        def roi_for_car_loan():
             roi=9
        def roi_for_crop_loan():
            roi=11
    class icici(rbi):

    class muthut():

    class ifl()

    class bajaj()
'''
class kcr_strategies:
    def pension(self):
        val=2500
        print("candidate will get :",val)
    def crop_loan_per_acre(self):
        val=5000
        print("crop loan per acre:",val)
    def ghmc_emp_bonus(self):
        val_bonus=2000
        print("bonus:",val_bonus)
    def gas_bill(self):
        gas_bill=1300
        subsidy=500
        total_bill=gas_bill-subsidy
        print("u have to pay:",total_bill)
class revanth_policies(kcr_strategies):
    def pension(self):
        val=3500
        print("candidate will get :",val)
    def crop_loan_per_acre(self):
        val=7000
        print("crop loan per acre:",val)
    def ghmc_emp_bonus(self):
        val_bonus=500
        print("bonus:",val_bonus)
    def gas_bill(self):
        if(white_ration_card==True):
            print("rate:",500)
        else:
            rate=1300
            print("cost per gas:",rate)
#method overriding: sub class methods
# will override to the parent class methods
obj=revanth_policies()
obj.pension() #3500
obj.ghmc_emp_bonus()
kcr_obj=kcr_strategies()
kcr_obj.pension()