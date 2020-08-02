from collections import Counter
n=int(input())
l=input().split()
for i in range(n):
    l[i]=int(l[i])
l=sorted(l)
print('%.1f'%(sum(l)/n))
if n%2 is 0:
    print('%.1f'%((l[n//2-1]+l[n//2])/2))
else:
    print('%.1f'%l[n//2])
d=dict(Counter(l))
mx=0
for i in d.values():
    if i>mx:
        mx=i
for i in d.keys():
    if d[i] is mx:
        print(i)
        break
