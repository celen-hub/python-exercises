
student_heights = input("Input a list of student heights ").split()

student_heights = [int(x) for x in student_heights]
print(student_heights)



total = 0
y = 0
while y < len(student_heights):
  total += student_heights[y]
  y += 1

avg = total / len(student_heights)
round(avg, 2)

print(avg)

