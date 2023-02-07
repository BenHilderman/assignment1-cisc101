"""
This program uses the mass and acceleration to calculate the needed force
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Sept 11, 2022
"""

mass = float(input("Enter the Mass: "))
acceleration = float(input("Enter the Acceleration Rate: "))
force = (mass) * (acceleration)
print("To Move an object of Mass = " + str(mass) + " Kg at an acceleration rate of " + str(acceleration) + " m/s/s we need a force equal to " + str(format(force, '.1f')) + " Newtons")