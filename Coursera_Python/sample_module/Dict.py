"""
Examples on dictionaries
"""
PURSE = dict()  # dict() constructor to create a dictionary object
PURSE['money'] = 25
PURSE['candy'] = 15
PURSE['tissue'] = 10
print('Before modifying:')
print(PURSE)
PURSE['money'] += 20
print('\nAfter modifying:')
print(PURSE)

# dictionary literal constants
print('Dictionary Literal constants:')
JJJ = {'chuck': 111, 'Gir': 222, 'Kav': 333}
print(JJJ)

# dictionaries will not allow duplicate values...
JJJ['chuck'] = 456
print(JJJ)

# counting names in a dictionaries..
print('\nCounting names:')
COUNT = dict()

NAMES = ['csev', 'cwen', 'csev', 'cwen', 'zqian']

for name in NAMES:
    if name not in COUNT:
        COUNT[name] = 1
    else:
        COUNT[name] += 1

print(COUNT)

# use of get() to return the value of a specified key
print('\nThe get() takes a name and a default value for int and returns the value of the key:')
print(COUNT.get('cwen', 0))
print(COUNT.get('gir', 0))

# simplified counting with get()
print('Simulates the simplified counting with get()')
C = dict()
for name in NAMES:
    C[name] = C.get(name,0) + 1

print(C)

