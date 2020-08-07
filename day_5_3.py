import math
def func(m,s,p):
    return 0.5*(1+math.erf((p-m)/(s*2**0.5)))
m=20
s=2
p1=19.5
p2=20
p3=22
res1=func(m,s,p1)
res2=func(m,s,p3)-func(m,s,p2)
print('%.3f\n%.3f'%(res1,res2))
