
def lcs(u, v):
   
    c = [[-1]*(len(v) + 1) for _ in range(len(u) + 1)]
    lcs_helper(u, v, c, 0, 0)
    return c
 
 
def lcs_helper(u, v, c, i, j):
   
    if c[i][j] >= 0:
        return c[i][j]
 
    if i == len(u) or j == len(v):
        q = 0
    else:
        if u[i] == v[j]:
            q = 1 + lcs_helper(u, v, c, i + 1, j + 1)
        else:
            q = max(lcs_helper(u, v, c, i + 1, j),
                    lcs_helper(u, v, c, i, j + 1))
    c[i][j] = q
    return q
 
 
def print_lcs(u, v, c):
    i = j = 0
    while not (i == len(u) or j == len(v)):
        if u[i] == v[j]:
            print(u[i], end='')
            i += 1
            j += 1
        elif c[i][j + 1] > c[i + 1][j]:
            j += 1
        else:
            i += 1
 
 
u = input('Enter first string: ')
v = input('Enter second string: ')
c = lcs(u, v)
print('Longest Common Subsequence: ', end='')
print_lcs(u, v, c)
