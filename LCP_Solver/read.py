import numpy as np

p1 = []
p2 = []

x = int(raw_input("Enter row: "))
y = int(raw_input("Enter col: "))

total = x + y
prod = x * y

# player 1's payoffs row-wise...
for i in range(prod):
    p1.append(int(raw_input("Enter payoff values for player 1 row-wise")))

for i in range(prod):
    p2.append(int(raw_input("Enter payoff values for player 2 col-wise")))

print "Player 1's payoff matrix row-wise"
print p1

print "Player 1's payoff matrix row-wise"
print p2

mat = np.zeros((total, total))

print mat

z = 0
for i in range(x):
    for j in range(total):
        if j >= x:
            mat[i][j] = p1[z]
            z += 1

print mat

for i in range(x):
    for j in range(total):
        if j >= x:
            mat[i][j] = p1[z]
            z += 1


"""print sum
print prod

mat = np.zeros((int(x), int(y)))

for i in range(int(x)):
    for j in range(int(y)):
        dt = raw_input("Enter data for (%d, %d)" % (i, j))
        mat[i][j] = int(dt)


print mat
a = mat[0][1]
print type(a)

for i in range(int(x)):
    for j in reversed(range(int(y))):
        dt = raw_input("Enter data for (%d, %d)" % (i, j))
        mat[i][j] = int(dt)
"""