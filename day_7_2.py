def rank(l,n):
    res=[0 for i in range(n)]
    s=sorted(l)
    for i in range(n):
        for j in range(n):
            if l[i]==s[j]:
                res[i]=j+1
    return res
n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))
x=rank(x,n)
y=rank(y,n)
mx=sum(x)/n
my=sum(y)/n
cov=sum((x[i]-mx)*(y[i]-my) for i in range(n))/n
sdx=(sum((x[i]-mx)**2 for i in range(n))/n)**0.5
sdy=(sum((y[i]-my)**2 for i in range(n))/n)**0.5
pearson=cov/(sdx*sdy)
print('%.3f'%pearson)
