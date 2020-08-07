import math
def func(m,s,p):
    return 0.5*(1+math.erf((p-m)/(s*2**0.5)))
m=70
s=10
p1=80
p2=60
res1=100-func(m,s,p1)*100
res2=100-func(m,s,p2)*100
res3=func(m,s,p2)*100
print('%.2f\n%.2f\n%.2f'%(res1,res2,res3))
