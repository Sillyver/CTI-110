# Wyatt White
# 9/16/26
# P4LAB2
# Psuedocode algorithm

repeat = 'yes'

while repeat != "no":
    base = int(input("Enter an integer: "))
    if base >= 0:
        for item in range(1, 13):
            print(f"{base} x {item} = {base * item}")
    else:
        print("Error: Please enter a positive integer.")
        
    repeat = input("Would you like to run the program again? (yes/no): ")

print("Exiting Program...")
