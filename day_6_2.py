import math
def func(m,s,p):
    return 0.5*(1+math.erf((p-m)/(s*2**0.5)))
z=250
n=100
m=2.4
s=2.0
x=m*n
y=s*(n**0.5)
res=func(x,y,z)
print('%.4f'%res)
