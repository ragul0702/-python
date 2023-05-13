a = int(input('enater the num :'))
b=[]
for i in range(a):
    b.append (i+1)
print(b)

c = [i*2 for i in b]
print(c)

f=(c[::-1])
print(f)

f[5] = 50
print(" cganftyfth ",f)
f[7] = 70
print('hhhh',f)
v = [i for i in range(f[5])]
print(v)
d = [i for i in range(f[7])]
print(d)

v = c.pop(5)
c.insert(5,50)
print(c)
