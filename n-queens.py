import math
import copy
import random


############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    N = n * n
    k = n
    return math.factorial(N)/ (math.factorial(k) * math.factorial(N - k))

def num_placements_one_per_row(n):
    return math.pow(n,n)

def n_queens_valid(board):
    # empty board is vacuously true
    if (len(board) == 0):
        return True
    
    # quick check if duplicates exists
    tmp = board[:]
    list.sort(tmp)
    for i in range(1, len(tmp)):
        if tmp[i-1] == tmp[i]:
            return False

    tmp = board[:]
    for i in range(0, len(tmp)):
        for j in range(i+1, len(tmp)):
            if (tmp[i] == tmp[j] + (j-i) or
                tmp[i] == tmp[j] - (j-i)):
                return False
    return True
    

def n_queens_solutions(n):
    possibilities_remain = True
    solution = []
    row, col = 0, 0

    if (n>0):

        while (possibilities_remain):

            # push next possible col for current row
            solution.append(col)

            # Not valid - pop and try next col
            if (not n_queens_valid(solution)):
                solution.pop()
                col = col + 1

            # Valid
            else:
                # Valid and Complete!  Yield it.
                if (row == n-1):
                    yield list(tuple(solution))
                    solution.pop()
                    col = col + 1
                # Valid, but more rows to go...
                else:
                    row = row + 1
                    col = 0

            # Regardless of valid/invalid, check if we've tried all the cols
            # in the current row.  If so, back up and try the next new col
            # from the previous row.
            while  (col == n):
                row = row - 1
                if (row < 0):
                    # No where else to back up.  We tried everything.
                    possibilities_remain = False
                    break
                col = solution[row] + 1
                solution.pop()
