def add_score(subject_score, student, subject, score):
    if student not in subject_score: subject_score[student] = {}  
    subject_score[student][subject] = score
    return {student: subject_score[student]}

def calc_average_score(subject_score):
    return {student: "{:.2f}".format(round(sum(score.values()) / len(score), 2)) for student, score in subject_score.items()}

subject_score = {}
print(add_score(subject_score, '66010295', 'python', 50))
print(add_score(subject_score, '66010295', 'calculus', 60))
print(add_score(subject_score, '66010296', 'python', 40))
print(add_score(subject_score, '66010296', 'calculus', 90))
print(calc_average_score(subject_score))