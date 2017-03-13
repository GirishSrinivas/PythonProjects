import numpy as np
import LCPSolve

row = int(raw_input("Enter row: "))
col = int(raw_input("Enter col: "))

total = row + col

p1 = np.zeros((row, col))
p2 = np.zeros((row, col))


print "Enter for player 1"

for i in range(row):
    for j in range(col):
        p1[i][j] = int(raw_input("Enter data for (%d, %d)" % (i, j)))


print "Enter for player 2"
for i in range(row):
    for j in range(col):
        p2[i][j] = int(raw_input("Enter data for (%d, %d)" % (i, j)))

print "Player 1:"
print p1

print "Player 2:"
print p2

print "Transpose of player - 2"
p2 = p2.transpose()
print p2

d1 = np.zeros((row, total - col))
d2 = np.zeros((col, total - row))

m1 = np.hstack((d1, p1))
m2 = np.hstack((p2, d2))


mat = np.vstack((m2, m1))

print "Final matrix: "
print mat

print len(mat)

"""for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j] > 0:
            mat[i][j] = -mat[i][j]
        elif mat[i][j] < 0:
            mat[i][j] = (mat[i][j] * -1)
"""
print "Final matrix after correction: "
print mat

q = np.zeros(total)
for i in range(total):
    q[i] = -1

"""q = []
for i in range(total):
    q.append(-1)
    """

print q
# q = np.ones(total)
# q = q.transpose()

w, z, r = LCPSolve.LCPSolve(mat, q)

print "Solution is:"
print w
print z
print r




