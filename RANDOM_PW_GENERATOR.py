from random import *
print('The random password generated is:')
#using input list:
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print(choice(l),randint(0,9),choice(l),randint(0,9),choice(l),randint(0,9),sep='')
#using chr conversion of ASCII values for alphabet:
print(chr(randint(65,90)),randint(0,9),chr(randint(65,90)),randint(0,9),chr(randint(65,90)),randint(0,9),sep='')
