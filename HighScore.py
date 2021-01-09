
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


student_scores.sort()
print(student_scores[-1])


high_score = 0
for i in student_scores:
  if i > high_score:
    high_score = i
print(high_score)

print(max(student_scores))