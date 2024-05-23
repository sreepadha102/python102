#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.


class CalculateYear():

    def __init__(self):
        self.name = input("Enter your name :")
        self.age = int(input("Enter your age :"))
        while self.age < 0 and self.age > 100:
            self.age = int(input("Enter your age :"))


    def to_reach_hundered(self):
        age_diff = 100 - self.age
        reach_hundered_at = 2024 + age_diff
        return reach_hundered_at
        

calc_year = CalculateYear()
print(calc_year.name + ", You will turn 100 years old in the year:", calc_year.to_reach_hundered())