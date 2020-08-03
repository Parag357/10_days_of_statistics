def median(l):
    n=len(l)
    if n%2==0:
        return (l[n//2-1]+l[n//2])/2
    else:
        return l[n//2]
n=int(input())
x=list(map(int,input().split()))
f=list(map(int,input().split()))
l=[]
for i in range(n):
    for j in range(f[i]):
        l.append(x[i])
l=sorted(l)
n=len(l)
if n/2==0:
    a=l[:n//2]
    b=l[n//2:]
else:
    a=l[:n//2]
    b=l[n//2+1:]
print('%.1f'%abs(median(a)-median(b)))