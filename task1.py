"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

name = input("name: ")
age = int(input("age: "))
year = 2020+(100-age)
print(year)
