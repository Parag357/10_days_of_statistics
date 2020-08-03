n=int(input())
l=list(map(int,input().split()))
mean=sum(l)/n
for i in range(n):
    l[i] = (l[i]-mean)**2
print('%.1f'%(sum(l)/n)**0.5)
