#Ask the user for a number. 
#Depending on whether the number is even or odd, print out an appropriate message to the user.


class OddOrEven():

    def __init__(self):
        self.num = int(input("Enter a number to check if its even or odd? "))

    def check(self):
        if self.num % 2 == 0:
            return "Its an Even number"
        else:
            return "Its an Odd number"
        
check_number = OddOrEven()
print(check_number.check())