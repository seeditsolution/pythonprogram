# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# use tuple unpacking to swap
x,y=y,x
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
