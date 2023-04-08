# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
import math

for stu in student_heights:
  student = len(student_heights)
  total = sum(student_heights)
  rounded = total / student
  rounds = round(rounded)
print(rounds)
  