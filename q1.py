"""
This program asks how many people are coming to the study group, asking how many pets, and displays how many cupcakes you should make.  
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Sept 11, 2022
"""

amountOfPeople = int(input("Please enter the number of people who will attend (including you): "))
amountOfPets = int(input("How many of these people have pets?: "))
cupcakes = (2 * amountOfPeople) + 4 + (1 * amountOfPets)
print("You should bake " + str(cupcakes) + " cupcakes")