def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score

def calc_average_score(subject_score):
  return "{:.2f}".format(round(sum(subject_score.values()) / len(subject_score), 2))

subject_score = {}
print(add_score(subject_score, 'python', 50))
print(add_score(subject_score, 'calculus', 60))
print(calc_average_score(subject_score))