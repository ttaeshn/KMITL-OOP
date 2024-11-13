class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_mentor = None

stu1 = Student("66010295", "A")
stu2 = Student("65010295", "B")
stu3 = Student("64010295", "C")
stu4 = Student("63010295", "D")
stu5 = Student("64010200", "E")
stu6 = Student("65010200", "F")

stu1.student_mentor = stu2
stu2.student_mentor = stu3
stu3.student_mentor = stu4
stu5.student_mentor = stu6

stu_list1 = [stu1, stu2]
stu_list2 = [stu2, stu3]
stu_list3 = [stu3, stu4]
stu_list4 = [stu5, stu6]
all_list = [stu_list1, stu_list2, stu_list3, stu_list4]

def find_mentor(student_list, student_id):
    for lst in student_list:
        for student in lst:
            if student.student_id == student_id:
                if student.student_mentor:
                    return f"{student.student_mentor.student_id}, {student.student_mentor.student_name}"
                else:
                    return None
    return None

def is_mentor(student_list, id1, id2):
    mentors = {}
    for lst in student_list:
        for student in lst: mentors[student.student_id] = student.student_mentor

    while id1 in mentors:
        if mentors[id1] and mentors[id1].student_id == id2: return True
        id1 = mentors[id1].student_id if mentors[id1] else None

    return False

print(find_mentor(all_list, "63010295"))
print(is_mentor(all_list, "65010295", "63010295"))