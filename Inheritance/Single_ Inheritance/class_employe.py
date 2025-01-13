class emp:
    emp_name="Nagendra"
    emp_phone="9000723703"
    emp_id="20RU1A0538"
    emp_address="7-37 JM Thanda,Pattikonda,Dudekonda,Kurnool,AP-518380"
    def about_emp_name(self):
        print("detail about emp name",self.emp_name)
    def about_emp_phone(self):
        print("detail about emp phone",self.emp_phone)
    def about_emp_id(self):
        print("detail about emp phone", self.emp_id)
    def about_emp_address(self):
        print(self.emp_address)
obj=emp()
obj.about_emp_name()
obj.about_emp_id()
obj.about_emp_address()


