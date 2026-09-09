#Wyatt White
#9/9/26
#P2HW1
#Changing formating for old assignement


print("This program calculates travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
des = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel?  "))
print()
food = float(input("Last, how much do you need for food? "))
print()
balance = budget - gas - hotel - food

print("-------Travel Expenses-------")
print(f"{'Location:':20}{des}")
print(f"{'Initial Budget:':20}{'$'}{budget:.2f}")
print(f"{'Fuel:':20}{'$'}{gas:.2f}")
print(f"{'Hotel:':20}{'$'}{hotel:.2f}")
print(f"{'Food:':20}{'$'}{food:.2f}")
print("----------------------------")
print(f"{'Remaining Balance:':20}{'$'}{balance:.2f}")