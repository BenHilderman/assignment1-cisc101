"""
This program asks the price of four items, and outputs the subtotal, tax, and total
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Sept 11, 2022
"""

print("Hello customer, please use this program to enter the four items you are purchasing.")

firstItem = float(input("Please enter the price of item 1: "))
secondItem = float(input("Please enter the price of item 2: "))
thirdItem = float(input("Please enter the price of item 3: "))
fourthItem = float(input("Please enter the price of item 4: "))

subtotal = firstItem + secondItem + thirdItem + fourthItem
tax = subtotal * 0.13
total = subtotal + tax

print("The subtotal is $" + str(format(subtotal, '.2f')) + ", the sales tax is $" + str(format(tax, '.2f')) + ", and the total is $" + str(format(total, '.2f')) + ".")