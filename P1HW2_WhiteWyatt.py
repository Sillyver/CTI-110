# Wyatt White
# 9/2/2026
# P1HW2
#  This program will calculate and display travel expenses

print("This program calculates travel expenses")
print()
budget = int(input("Enter Budget: "))
print()
des = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
hotel = int(input("Approximately, how much will you need for accomodation/hotel?  "))
food = int(input("Last, how much do you need for food? "))
print()
balance = budget - gas - hotel - food

print("-------Travel Expenses-------")
print("Location:",des)
print("Initial Budget:",budget)
print()
print("Fuel:",gas)
print("Hotel:",hotel)
print("Food:",food)
print()
print("Remaining Balance:",balance)