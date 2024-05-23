given_string = "madam"

def ispalnidromestr(given_string):
    xv = ""
    for i in given_string:
        xv = i + xv

    if xv == given_string:
        return True
    else:
        return False
            

check_string = ispalnidromestr(given_string)

if check_string:
    print("The given", type(given_string), "is a palindrome")
else:
    print("Try a different string")