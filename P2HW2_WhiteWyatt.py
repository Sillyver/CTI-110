# Wyatt White
# 9/14/2026
# P2HW2
# This program will take input of grades and list the max, min, and average of the grades.

print("Calculate your grades!")
grade1 = float(input("Enter grade for module 1: "))
grade2 = float(input("Enter grade for module 2: "))
grade3 = float(input("Enter grade for module 3: "))
grade4 = float(input("Enter grade for module 4: "))
grade5 = float(input("Enter grade for module 5: "))
grade6 = float(input("Enter grade for module 6: "))

module_grades = [grade1, grade2, grade3, grade4, grade5, grade6]

max_grade = max(module_grades)
min_grade = min(module_grades)
average_grade = sum(module_grades) / len(module_grades)

print()
print("-------Results-------")
print(f"{'Lowest grade: ':15}{min_grade}")
print(f"{'Highest grade: ':15}{max_grade}")
print(f"{'Sum of Grades: ':15}{sum(module_grades)}")
print(f"{'Average: ':15}{average_grade:.2f}")
print("---------------------")