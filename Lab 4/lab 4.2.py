class Student:
    def __init__(self, stu_id, name):
        self.name = name
        self.id = stu_id

        
class Subject:
    def __init__(self, subject_id, subject_name,section,credit):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section
        self.credit = credit
        self.student_list = []
        self.teacher_list = []

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        
def finding_student_in_subject(subject_list, teacher_id):
    student_names = []
    for subject in subject_list:
            for teacher in subject.teacher_list:
                if teacher_id == teacher.teacher_id:
                    for student in subject.student_list: student_names.append(student.name)
    return student_names

def enrolled_subject(student_id, subject_list):
    enrolled_subject_list = []
    for subject in subject_list:
        for student in subject.student_list:
            if student_id == student.id: enrolled_subject_list.append(subject.subject_name)
    return enrolled_subject_list

stu1 = Student("66010295","Tae")
stu2 = Student("66010240","Nick")
stu3 = Student("66010085","Int")
stu4 = Student("66010405","Alice")
stu5 = Student("66010261","Nat")

sub1 = Subject("0001","object oriented programming","16",3)
sub2 = Subject("0001","object oriented programming","17",3)

teacher1 = Teacher("01","Aj.Orachat")
teacher2 = Teacher("02","Aj.Thana")

sub1.student_list.append(stu1)
sub1.student_list.append(stu2)
sub1.student_list.append(stu3)
sub2.student_list.append(stu4)
sub2.student_list.append(stu5)

sub1.teacher_list.append(teacher1)
sub2.teacher_list.append(teacher2)

print(finding_student_in_subject([sub1,sub2], "01"))
print(enrolled_subject("66010240", [sub1,sub2]))