import re
a="192.168.1.1"
b="((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)"
c=re.findall(b,a)
print(c)
d=".".join(c)

print(d)
f=open("ipadd","r")
x=f.read()
print(x)
y=re.findall(b,x)
print(y)

