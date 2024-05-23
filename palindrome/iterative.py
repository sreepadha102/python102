given_string = "madam"

def ispalnidromestr(given_string):
    for i in range(0, int(len(given_string)/2)):
        if given_string[i] != given_string[len(given_string)-i-1]:
            return False
        else:
            return True
            


check_string = ispalnidromestr(given_string)

if check_string:
    print("The given", type(given_string), "is a palindrome")
else:
    print("Try a different string")