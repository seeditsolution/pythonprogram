def gr(x, y):
    if x > y:
        return x
    else:
        return y
num = int(input("enter first number: "))
numt = int (input("enter second number: "))
g = gr(num, numt)    
print (f"greater number is {g}")  
