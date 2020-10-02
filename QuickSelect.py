def quickselect(array,startind,endind,position):  
    while True:
        pivotind = startind
        leftmark = startind + 1
        rightmark = endind
        while leftmark <= rightmark:
            if array[leftmark] > array[pivotind] and array[rightmark] < array[pivotind]:
                swap(leftmark,rightmark,array)
            if array[leftmark] <= array[pivotind]:
                leftmark += 1
            if array[rightmark] >= array[pivotind]:
                rightmark -=1
        swap(pivotind, rightmark,array)
        if rightmark == position:
            print(array[rightmark])
            return
        elif rightmark < position :
            startind = rightmark+1
        else :
            endind = rightmark - 1
            
def swap(one,two,array):
    array[one],array[two]=array[two],array[one]
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    k = int(input())
    quickselect(arr,0,n-1,k-1)
