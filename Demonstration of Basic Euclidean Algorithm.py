# To demonstrate Basic Euclidean Algorithm 

def gcd(a, b):  
    if a == 0 : 
        return b  
    return gcd(b%a, a) 
  
a = 55
b = 20
print("gcd(", a , "," , b, ") = ", gcd(a, b)) 
  
c = 94
d = 6
print("gcd(", c , "," , d, ") = ", gcd(a, b)) 
  
e = 34
f = 69
print("gcd(", e , "," , f, ") = ", gcd(a, b)) 