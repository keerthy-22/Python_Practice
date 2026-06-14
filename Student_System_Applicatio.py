class Student_System:
    def __init__(self,name,roll_number,course):
        self.name = name
        self.roll_number = roll_number
        self.course = course
    def attend_class(self):
        print("Attending Class....")
    def submit_assignment(self):
        print("Assignment Submitted....")
class Engineering_Student(Student_System):
    def __init__(self,course):
        super().__init__("Bhuvana","504",course)
    def build_project(self):
        print("Project Building....")
    def write_exam(self):
        print("Exam Writing....")
        
class MedicalStudent(Student_System):
    def __init__(self,course):
        super().__init__("Keerthi","2004",course)
    def study_anatomy(self):
        print("Studying Anatomy....")
    def do_practice(self):
        print("Doing practice....")
student = Engineering_Student("Engineering")
student.build_project()
student.write_exam()
print(student.name,student.roll_number,student.course,sep = "\n")
print()
student = MedicalStudent("Medicine")
student.study_anatomy()
student.do_practice()
print(student.name,student.roll_number,student.course,sep = "\n") 
