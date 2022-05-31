a={'kan':'Emp1','jay':'emp2','govind':'emp3','gaurav':'emp4'}
b=list(a.keys())
c=list(a.values())
print(b)
print(c)
c=zip(c,b)
d=dict(c)
print(d)