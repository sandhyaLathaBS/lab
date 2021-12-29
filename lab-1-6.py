def palindromeORnot(string):
    revString = reverse(string)
    if (string == revString):
        print("this is a palindrome string")
    else:
        print("this is not a palindrome string")


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


string = str(input("ENter a string "))

palindromeORnot(string)
