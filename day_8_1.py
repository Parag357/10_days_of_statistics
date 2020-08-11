data=[(95,85),(85,95),(80,70),(70,65),(60,70)]
x1=80
n=len(data)
x=sum(a for a,b in data)
y=sum(b for a,b in data)
xx=sum(a**2 for a,b in data)
xy=sum(a*b for a,b in data)
m1=x//n
m2=y//n
c2=((n*xy)-(x*y))/((n*xx)-(x**2))
c1=m2-(c2*m1)
y1=c1+(x1*c2)
print('%.3f'%y1)
