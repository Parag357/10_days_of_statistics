n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))
mx=sum(x)/n
my=sum(y)/n
cov=sum((x[i]-mx)*(y[i]-my) for i in range(n))/n
sdx=(sum((x[i]-mx)**2 for i in range(n))/n)**0.5
sdy=(sum((y[i]-my)**2 for i in range(n))/n)**0.5
pearson=cov/(sdx*sdy)
print('%.3f'%pearson)