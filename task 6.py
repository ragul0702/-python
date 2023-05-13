a=[1,2,3,4]
b=[1,3,4,8]
c=a+b
print(c)

d=set(c)
print(d)

e=list(d)
print(e)

f=max (e)
print (f)

p=[]
h=[]
for i,j in enumerate(e):
    print(i,j)
    p.append(i)
    h.append(j)
print(p)
print(h)

l = p+h
print(l)

u=set(l)
print(u)

k=list(u)
print(k)
