#Program to find maximum in arr[] of size n  

def largest(arr,n): 
    max = arr[0] 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max
  
arr = [2, 24, 54, 121, 2201, 662, 313, 535] 
n = len(arr) 
ans = largest(arr,n) 
print ("Largest in given array is",ans) 