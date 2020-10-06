from scipy.optimize import linprog

n=int(input())
polys = [[[int(x) for x in input().split()] for _ in range(int(input()))] for _ in range(n)]
polys.sort(key=lambda p: sum(p1[0]*p2[1] - p1[1]*p2[0] for p1,p2 in zip(p, p[1:] + [p[0]])))

ninc = n*4
a = []
b = []
c = [1]*ninc
for i in range(len(polys)-1):
    poly = polys[i+1]
    for p in polys[i]:
        for i1 in range(len(poly)):
            p0, p1 = poly[i1], poly[(i1+1)%len(poly)]
            dx, dy = p1[0]-p0[0], p1[1]-p0[1]
            eq = [0]*ninc
            eq[4*i  ] =  dy;  eq[4*i+1] = -dy
            eq[4*i+2] = -dx;  eq[4*i+3] =  dx
            eq[4*i+4] = -dy;  eq[4*i+5] =  dy
            eq[4*i+6] =  dx;  eq[4*i+7] = -dx
            a.append(eq)
            b.append(dx*(p[1]-p0[1]) - dy*(p[0]-p0[0]))

res = linprog(c, a, b, method='simplex', options={'maxiter':100000, 'tol':1e-7})
assert res.status == 0 or res.status == 2
print(res.fun if res.status == 0 else -1)
