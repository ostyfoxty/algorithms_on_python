n, x, y = int(input()), int(input()), int(input())
if x > y:
    x, y = y, x

m = y*(n-1)//(x+y) #make M copies on the fast one
#N-1-M on the slow one
t_max = x+max(x*m, y*(n-1-m)) #make a copy on the faster copier (x) plus the total time
for i in range(max(0, m-1), min(n-1, m)+2):
    t = x + max(x*i, y*(n-1-i))
    if (t < t_max):
        t_max = t

print(t)
