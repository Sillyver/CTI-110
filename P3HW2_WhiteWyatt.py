# Wyatt White
# 9/16/26
# P3HW2
# Salary calculator

# gathering info
employee = input("Enter employee's name: ")
hours =  float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))


# calculations

if hours >= 40:
    overtime = hours -40
else:
    overtime = 0

if overtime > 0:
    ot_pay = overtime * (pay_rate * 1.5)
else:
    ot_pay = 0

reg_pay = (hours - overtime) * pay_rate

gross_pay = reg_pay + ot_pay

# printing results
print("----------------------------")
print(f'Employee Name: {employee:<20}')
print()
print("Hours Worked     Pay Rate     Overtime      Overtime pay     Regular Pay     Gross Pay")
print("------------------------------------------------------------------------------------------")
print(f'{hours:<16.1f} {pay_rate:<12.1f} {overtime:<13.1f} {ot_pay:<16.2f} {"$"}{reg_pay:<15.2f} {"$"}{gross_pay:<10.2f}')