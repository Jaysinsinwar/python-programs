a={}
x='A'
y='a'
for i in range(26):
    a.update({x:y})
    x=chr(ord(x)+1)
    y=chr(ord(y)+1)
print(a)
