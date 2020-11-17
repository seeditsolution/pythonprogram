'''python script to print
   *
   **
   ***
   ****
   *****
'''


for i in range(1,6):
   for j in range(1,6):
       if j<=i:
          print("*",end="")
       else:
          print("",end="")
   print("")    

