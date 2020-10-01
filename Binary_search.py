def binarySearch(arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid+1, r, x) 
    else: 
        return -1

    
if __name__ == "__main__":
    n_arr = list(map(int, input().split()))
    arr = n_arr[1:]
    n_keys = list(map(int, input().split()))
    n = n_keys[0]
    keys = n_keys[1:]
    for i in range(n):
        res = binarySearch(arr, 0, len(arr)-1, keys[i])
        print(res, end=" ")
