def diagonalDifference(arr):
    '''Finds the diagonal Difference of 2D square matrix'''

    result,size = (0,len(arr))
    for i in range(0,size):
        result += arr[i][i] - arr[i][size-1-i]  #calculating difference
    return abs(result)

if __name__ == '__main__':

    n = abs(int(input("Enter matrix size : ").strip())) #input martrix size
    arr = []

    for i in range(n):
        lst = []
        while(len(lst)!=n):
            row = input(f"Enter {n} space separated values for row {i+1} : ")
            lst = list(map(int,row.strip().split(" "))) #converting string to list
        arr.append(lst)

    print( diagonalDifference(arr))
