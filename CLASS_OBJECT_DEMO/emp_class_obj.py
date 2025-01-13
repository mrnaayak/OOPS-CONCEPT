class emp:
    #class level variables
    dept_name="sales"
    #below __init__() is constructor
    def __init__(self,empid,empname,empdesignation,empsalary,location):
        self.empid=empid
        self.empname=empname
        self.empdesignation=empdesignation
        self.empsalary=empsalary
        self.location=location
    def emp_details(self):
        print("emp details:",self.empid,self.empsalary,self.location,self.empdesignation)
    def emp_experience(self):
        print("total experience:15")