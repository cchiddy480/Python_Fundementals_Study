# Review of OOP concepts in Python

# Class definition with contructor 
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year

# Creating 3 instances of the Student class
roger = Student("Roger van der Weyden", "Year 10")
sandro = Student("Sandro Botticelli", "Year 12")
pieter = Student("Pieter Bruegel the Elder", "Year 8")
        