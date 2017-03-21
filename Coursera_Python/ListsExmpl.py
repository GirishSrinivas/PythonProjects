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

# length of lists
print('Length of LIST1: %d' % len(LIST1))
print('Length of LIST2: %d' % len(LIST2))
print('Length of LIST3: %d' % len(LIST3))
