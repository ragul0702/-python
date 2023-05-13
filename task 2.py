import datetime
a = datetime.datetime .today()
print(a)

b=[a.strftime("%d-%B-%y")]
print(b) 

c =a.strftime('%A')
print(c)

d = c.upper()
print(d)

v=list(d)
print(v)

h=''.join(v)
print(h)

i=h.lower()
print(i)

z=len(i)
print(z)

n=[]
for i in range(z):
    print(i)
    n.append(i)
print(n)
