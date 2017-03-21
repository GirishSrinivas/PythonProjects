"""
Lists Examples
"""

LIST1 = ['hello', 'world', 'python']
LIST2 = [2, 3, 4, 5, 6, 7]
LIST3 = ['hello', 24, 99.9]

print(LIST1)
print(LIST2)
print(LIST3)

# accessing lists using the index
print(LIST1[0])
print(LIST1[1])
print(LIST1[2])

# mutable example
LIST2[0] = 10
print(LIST2)

# length of lists and range() function
print('Length of LIST1: %d' % len(LIST1))
print(range(len(LIST1)))
print('Length of LIST2: %d' % len(LIST2))
print(range(len(LIST2)))
print('Length of LIST3: %d' % len(LIST3))
print(range(len(LIST3)))

# printing each element in the list TYPE - 1
print('\nLIST1\n')
for ele in LIST1:
    print(ele)

print('\nLIST2\n')
for ele in LIST2:
    print(ele)

print('\nLIST3\n')
for ele in LIST3:
    print(ele)

# printing each element in the list using range() function
print('\nLIST1 using range()\n')
for i in range(len(LIST1)):
    print(LIST1[i])

print('\nLIST2 using range()\n')
for ele in range(len(LIST2)):
    print(LIST2[ele])

print('\nLIST3 using range()\n')
for ele in range(len(LIST3)):
    print(LIST3[ele])

# printing each element in the list using enumerate() function
print('\nLIST1 using enumerate()\n')
for i, ele in enumerate(LIST1):
    print(LIST1[i])

print('\nLIST2 using enumerate()\n')
for i, ele in enumerate(LIST2):
    print(LIST2[i])

print('\nLIST3 using enumerate()\n')
for i, ele in enumerate(LIST3):
    print(LIST3[i])
