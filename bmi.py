name=input("Enter your name")
height=int(input("Enter your height"))
weight=float(input("Enter your Weight"))
bmi=weight/(height**2)
print(f"BMI : {bmi}")
if bmi < 25 :
    print(name)
    print("is not overweight")
else :
    print(name)
    print("the person is overweigth")
