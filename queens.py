import numpy as np

board = np.zeros( (8,8), int )

# Get the diagonal 'index' for any point (m,n)
def getdiagd(m,n):
	if (m == n):
		return 0
	else:
		return (n-m)

def getCollisionCount(m,n,b):
	# Get row and col sums for row m, col n
	colsum = np.sum(b, axis=0)[n]
	rowsum = np.sum(b, axis=1)[m]
	# Get sum of diagonal that includes (m,n)
	d = getdiagd(m,n)
	ddiagsum = np.sum(b.diagonal(d))
	# Rotate board 270 degrees CCW (90 CW) and get diagonal that includes (n, 7-m)
	# This is the same as finding the sum of the upward diagonal of the original board
	# just a lot easier.
	d = getdiagd(n, (7-m))
	udiagsum = np.sum(np.rot90(b, 3).diagonal(d))
	return (colsum + rowsum + ddiagsum + udiagsum)

def queens(m):
	if m > 7:
		print board
		return True
	for n in xrange(8):
		if getCollisionCount(m,n, board) == 0:
			board[m][n] = 1
			if queens(m+1):
				return True
			else:
				board[m][n] = 0
	return False

queens(0)