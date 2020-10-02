# Selection Sort 
import sys 
a = [ 170, 40, 72, 90, 802, 24, 2, 66, 32]
string = "SUBSCRIBETOSEEDITSOLUTIONS"
  
for i in range(len(a)): 
    min_idx = i 
    for j in range(i+1, len(a)): 
        if a[min_idx] > a[j]: 
            min_idx = j 
              
    a[i], a[min_idx] = a[min_idx], a[i] 

print ("Selection Sorted array: ") 
for i in range(len(a)): 
    print("%d \t" %a[i], sep=' ', end='', flush=True) 
    
# Bubble Sort 
def bubbleSort(a): 
    n = len(a) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if a[j] > a[j+1] : 
                a[j], a[j+1] = a[j+1], a[j] 
  

# Insertion Sort 
def insertionSort(a): 
    for i in range(1, len(a)): 
        key = a[i] 
        j = i-1
        while j >=0 and key < a[j] : 
            a[j+1] = a[j] 
            j -= 1
        a[j+1] = key 
    

# Heap Sort 
def heapify(a, n, i): 
    largest = i 
    l = 2 * i + 1    
    r = 2 * i + 2   
    if l < n and a[i] < a[l]: 
        largest = l 

    if r < n and a[largest] < a[r]: 
        largest = r 
  
    if largest != i: 
        a[i],a[largest] = a[largest],a[i]
        heapify(a, n, largest) 
  
def heapSort(a): 
    n = len(a) 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(a, n, i) 
  
    for i in range(n-1, 0, -1): 
        a[i], a[0] = a[0], a[i]  
        heapify(a, i, 0) 

# Radix Sort 
def countingSort(a, exp1): 
    n = len(a) 
    output = [0] * (n) 
    count = [0] * (10) 
    for i in range(0, n): 
        index = (a[i]/exp1) 
        count[int((index)%10)] += 1

    for i in range(1,10): 
        count[i] += count[i-1] 
    i = n-1
    while i>=0: 
        index = (a[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = a[i] 
        count[int((index)%10)] -= 1
        i -= 1
    i = 0
    for i in range(0,len(a)): 
        a[i] = output[i] 

def radixSort(a):
    max1 = max(a)
    exp = 1
    while max1/exp > 0:
        countingSort(a,exp)
        exp *= 10

# Shell Sort 
def shellSort(a): 
    n = len(a) 
    gap = n/2
    while int(gap) > 0: 
        for i in range(int(gap),int(n)): 
            temp = a[i] 
            j = int(i) 
            while  int(j) >= int(gap) and a[int(j)-int(gap)] >temp: 
                a[j] = a[j-gap] 
                j -= gap 
            a[j] = temp 
        gap /= 2

# Counting sort 
def countSort(string): 
    output = [0 for i in range(256)] 
    count = [0 for i in range(256)] 
    ans = ["" for _ in string] 
    for i in string: 
        count[ord(i)] += 1
  
    for i in range(256): 
        count[i] += count[i-1] 
  
    for i in range(len(string)): 
        output[count[ord(string[i])]-1] = string[i] 
        count[ord(string[i])] -= 1
  
    for i in range(len(string)): 
        ans[i] = output[i] 
    return ans  
  
    
bubbleSort(a) 
print ("\nBubble Sorted array:") 
for i in range(len(a)): 
    print ("%d \t" %a[i], sep=' ', end='', flush=True)

insertionSort(a) 
print ("\nInsertion Sorted array:") 
for i in range(len(a)): 
    print ("%d\t" %a[i], sep=' ', end='', flush=True) 
    
heapSort(a) 
n = len(a) 
print ("\nHeap Sorted array:") 
for i in range(n): 
    print ("%d\t" %a[i], sep=' ', end='', flush=True)   
    
radixSort(a)
print ("\nRadix Sorted array:")
for i in range(len(a)):
    print("%d\t" %a[i], sep=' ', end='', flush=True)
    
shellSort(a) 
print ("\nShell Sorted array:") 
for i in range(n): 
    print("%d\t" %a[i], sep=' ', end='', flush=True)

b = countSort(string) 
print("\nSorted character array is %s" %(" ".join(b)))

