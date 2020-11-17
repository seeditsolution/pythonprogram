# Python program to reverse a given String
# Using a user-defined function
def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s


# given string
mystr = "BeginnersBook"
print("Given String: ", mystr)

# reversed string
print("Reversed String: ", reverse(mystr))
