def diagonalDifference(arr) #function accepting a 2d array

  sum1=0
  sum2=0
  res=0
  for i in range(0,len(arr)):
  sum1=sum1+arr[i][i]
  sum2=sum2+arr[i][(len(arr)-1)-i]
  res=sum1-sum2
  return abs(res)
if __name__ == '__main__':
fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip) #size

arr = []

for _ in range(n):
arr.append(list(map(int, input().rstrip().split())))

print( diagonalDifference(arr))
  
