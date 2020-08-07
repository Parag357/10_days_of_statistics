import math
m=2.5
k=5
e=math.exp(1)
f=1
for i in range(1,k+1):
    f*=i
print('%.3f'%((m**k)*(e**-m)/f))