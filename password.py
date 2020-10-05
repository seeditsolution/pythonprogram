import re
p= input("Input your password ")
flag=0
while True:  
    if (len(p)<6 or len(p)>12):
        flag=1
        break
    elif not re.search("[a-z]",p):
        flag=1
        break
    elif not re.search("[0-9]",p):
        flag=1
        break
    elif not re.search("[A-Z]",p):
        flag=1
        break
    elif not re.search("[$#@]",p):
        flag=1
        break
    elif re.search("\s",p):
        flag=1
        break
    else:
        flag=0
        print("Valid Password")
        break

if flag==1:
    print("Not a Valid Password ")
