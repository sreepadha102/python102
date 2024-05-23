given_string = input("Enter the string to check if its palindrom? ")

def ispalnidromestr(given_string):
    if given_string.casefold() == given_string[::-1].casefold():
        print("The given", type(given_string), "is a palindrome")
    else:
        print("Try a different string or list")

ispalnidromestr(given_string)


