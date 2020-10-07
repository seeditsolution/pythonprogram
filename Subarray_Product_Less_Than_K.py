L = [1,2,3]
n = [nums[i:i+j] for i in range(0,len(nums)) for j in range(1,len(nums)-i+1)]
c = 0
for x in n:
    pro = 1
    for m in x:
        pro *= m
    if pro < k:
        c += 1
print(c)
