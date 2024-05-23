given_string = 'madam'
j = -1
flag = 0
for i in given_string:
    if i != given_string[j]:
        flag = 1
        break
    j = j - 1
if flag == 1:
    print("Try a different string")
else:
    print("The given", type(given_string), "is a palindrome")