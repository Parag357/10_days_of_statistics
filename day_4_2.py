def fact(n):
    if n is 0 or n is 1:
        return 1
    else:
        return n*fact(n-1)
def func(x,n,p):
    temp=fact(n)/(fact(n-x)*fact(x))
    return temp*(p**x)*((1-p)**(n-x))
n=10
p=0.12
l=[0,1,2]
res=temp=0
for x in l:
    res+=func(x,n,p)
print('%.3f' %res)
temp=func(2,n,p)
print('%.3f' %(1-res+temp))
