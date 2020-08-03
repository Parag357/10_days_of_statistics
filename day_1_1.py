def median(l):
    n=len(l)
    if n%2==0:
        return (l[n//2-1]+l[n//2])//2
    else:
        return(l[n//2])
n=int(input())
l=sorted(list(map(int,input().split())))
a=[]
b=[]
c=[]
if n%2==0:
    b.append(l[n//2-1])
    b.append(l[n//2])
    a=l[:n//2]
    c=l[n//2:]
else:
    b.append(l[n//2])
    a=l[:n//2]
    c=l[n//2+1:]
print(median(a))
print(median(b))
print(median(c))