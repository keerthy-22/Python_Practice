"""
Roll Number
Name
Subjects (Maths,Physics,Chemistry,Sanskrit)
Marks 
Score Grade 
"""
print("Mark Sheet Generator: ")
name = input("Enter your Name: ")
roll_no = input("Enter you Roll No.: ")
year = input("Enter year of pass out: ")
medium = input("Enter medium ( English / Telugu ): ")
sanskrit_marks = int(input("Enter Sanskrit Marks: "))
english_marks = int(input("Enter English Marks: "))
mathA_marks = int(input("Enter Math - A Marks: "))
mathB_marks = int(input("Enter Math - B Marks: "))
physics_marks = int(input("Enter Physics Marks: "))
chemistry_marks = int(input("Enter Chemistry Marks: "))
total = sum([sanskrit_marks,english_marks,mathA_marks,mathB_marks,
            physics_marks,chemistry_marks])
percentage = (total / 470) * 100  

marksheet = f"""
                Sri Chaitanya Jr. College
                Patamatalanka,Vijayawada
Name: {name}                        Roll No.: {roll_no}
Year: {year}                                   Medium  : {medium}
-----------------------------------------------------------
        Subject                             Marks 
        Sanskrit                            {sanskrit_marks}
        English                             {english_marks}
        Mathematics - A                     {mathA_marks}
        Mathematics - B                     {mathB_marks}
        Physics                             {physics_marks}
        Chemistry                           {chemistry_marks}

        Total: {total}
        Percentage: {percentage:.1f}%
"""
file_name = f"{roll_no}.txt"
with open(file_name,"w") as file:
    file.writelines([marksheet])
