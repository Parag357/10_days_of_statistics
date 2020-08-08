import math
def func(m,s,p):
    return 0.5*(1+math.erf((p-m)/(s*2**0.5)))
z=9800
n=49
m=205
s=15
x=m*n
y=s*(n**0.5)
res=func(x,y,z)
print('%.4f'%res)
