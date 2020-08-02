n=int(input())
l1=input().split()
l2=input().split()
for i in range(n):
    l1[i]=int(l1[i])
    l2[i]=int(l2[i])
s=0
for i in range(n):
    s+=l1[i]*l2[i]
print('%.1f'%(s/sum(l2)))
