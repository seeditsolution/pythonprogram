def palindrome(s): #fuction creation
    c=""
    for i in s: #finding reverse string
        c=i+c
    if c==s: #Comparing strings using if
        print(s,"is Palindrome")
    else: #else if if is false
        print(s,"is not Palindrome")

s=input("Enter String\n")
palindrome(s)



    
    
