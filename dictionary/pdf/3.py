Employee1={
        'name':'bob',
        'age':45,
        'profession':'writer',
        'city':'varanasi'
    }
Employee1['name']='Naa' #this will change value
print(Employee1)
Employee1['kkk']=Employee1["name"]
del Employee1['name']
print(Employee1)