class Employee_System:
    def __init__(self,name,eid,salary):
        self.name = name
        self.eid = eid
        self.salary = salary
    def work(self):
        print("Working....")
    def get_salary(self):
        print("Salary Credited....")
class Developer(Employee_System):
    def __init__(self,salary):
        super().__init__("Developer","22",salary)
    def write_code(self):
        print("Coding....")
    def fix_bug(self):
        print("Bug Fixed....")
        
class Manager(Employee_System):
    def __init__(self,salary):
        super().__init__("Manager","09",salary)
    def conduct_meeting(self):
        print("Meeting Started....")
    def assign_task(self):
        print("Task Assigned....")
system = Developer("11 LPA")
system.write_code()
system.fix_bug()
print(system.name,system.eid,system.salary,sep = "\n")
print()
system = Manager("13 LPA")
system.conduct_meeting()
system.assign_task()
print(system.name,system.eid,system.salary,sep = "\n") 
