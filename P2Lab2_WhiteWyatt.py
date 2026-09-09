#Wyatt White
#9/9/2026
#P2Lab2
#This project will use a dictonary to store a pair of keys and values.

auto = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}
keys = auto.keys()
print(keys)
print("")
car = input("Enter a vehicle to see it's mpg: ")
mpg = auto[car]
print("")
print("The",car,"gets",auto[car],"mpg.")
print("")
dis = float( input(f"How many miles will you drive the {car}? "))
print("")

gal = dis / mpg

print(f"{gal:.2} gallon(s) of gas are needed to drive the {car} {auto[car]} miles.")
