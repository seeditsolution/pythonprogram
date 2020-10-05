def prime(n):
    prime=[]
    i=2
    while(i*i<=n):
        if i in prime:
            for j in range(i*2,n+1,i):
                if j in prime:
                    prime.remove(j)
        i+=1

    return prime
n=int(input())
print(prime(n))
