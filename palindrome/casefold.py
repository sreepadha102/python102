given_string = "madam"

def ispalnidromestr(given_string):
    if given_string.casefold() == given_string[::-1].casefold():
        print("The given", type(given_string), "is a palindrome")
    else:
        print("Try a different string")

ispalnidromestr(given_string)