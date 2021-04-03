
# inverse stirng
def palindrome(string):
    return string == string[::-1]
 
# input string
string = "des"

# result
result = palindrome(string)

# check if string is palindrome then print
if result:
    print("Yes")
else:
    print("No")