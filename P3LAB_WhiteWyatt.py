# Wyatt White
# 9/14/2026
# P3LAB
# This program will calculate the most efficient amount of coins to equal a sum of money

import math

base = float(input("Enter the amount of money as a float: $"))
money = (base * 100)
dollar = math.floor(base)
coin = f"{base - dollar:.2f}"
cents =float(coin) * 100
inti =float(coin) * 100
#determines the dollars
if base >= 1:
    print(dollar , "Dollars")
else:
    dollar = 0

#determines the quarters
if cents >= 25:
    quarters = math.floor(cents / 25)
    print(quarters , "Quarters")
    cents = cents - (quarters * 25)
else:
    quarters = 0

#determines the dimes
if cents >= 10:
    dimes = math.floor(cents / 10)
    print(dimes , "Dimes")
    cents = cents - (dimes * 10)
else:
    dimes = 0

#determines the nickels
if cents >= 5:
    nickels = math.floor(cents / 5)
    print(nickels , "Nickels")
    cents = cents - (nickels * 5)
else:
    nickels = 0

#determines the pennies
if cents >= 1:
    pennies = math.floor(cents / 1)
    print(pennies , "Pennies")
else:
    pennies = 0

#if zero is submitied
if base == 0:
    print("No change")