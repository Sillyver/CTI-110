# Wyatt White
# 9/14/2026
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

print()
print("----------Results----------")
print(f"{'Lowest grade is: ':15} {low}")
print(f"{'Highest grade is: ':15} {high}")
print(f"{'Sum of grades is: ':15} {sum}")
print(f"{'Average of grades is: ':15} {avg:.2f}")
print()
# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
else:
    if avg > 80:
        print('Your grade is: B')
    else:
        if avg > 70:
            print('Your grade is: C')
        else:
            if avg > 60:
                print('Your grade is: D')
            else:
                print('Your grade is: F')





