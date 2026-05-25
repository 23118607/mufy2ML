#dictionary
age = {
    'Hans': 24, 
    'Prag': 23, 
    'Bunyod': 18
    }

#step 1
print(age)

#step 2
print(age['Hans'])

#step 3
age['Prag'] = 30

#step 4
print(age['Prag'])

#step 5
del age['Bunyod']
print(age)