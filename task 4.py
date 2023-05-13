a =input('enter the user name :')
b =input('enter the user pass :')
c=a+b
if 'demo' in a:
    open('website.html','w').write(c)
elif'demohi'in a:
    open('website.html','w').write(c)
else:
    print('not valid')
d=open('website.html','r').read()
print(d)

e=len(d)
print(e)

f=[f for f in range(e)]
print(f)
