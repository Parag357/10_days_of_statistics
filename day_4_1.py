def fact(n):
    if n is 1 or n is 0:
        return 1
    else:
        return n*fact(n-1)
def func(x,n,p):
    temp=fact(n)/(fact(n-x)*fact(x))
    return temp*(p**x)*((1-p)**(n-x))
n=6
p=1.09/2.09
l=[3,4,5,6]
res=0
for x in l:
    res+=func(x,n,p)
print('%.3f' %res)
