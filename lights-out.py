import math
import copy
import random

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board
        self.M = len(board)
        self.N = len(board[0])

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        #initial move
        self.board[row][col] = not self.board[row][col]

        #residual moves
        if (row == 0 and col == 0): moves = ['r','d']
        elif (row == 0 and col == self.N-1): moves = ['l','d']
        elif (row == self.M-1 and col == 0):  moves = ['r','u']
        elif (row == self.M-1 and col == self.N-1): moves = ['l','u']
        elif (row == 0): moves = ['l','r','d']
        elif (row == self.M-1): moves = ['l','r','u']
        elif (col == 0): moves = ['r','u','d']
        elif (col == self.N-1): moves = ['l','u','d']
        else: moves = ['l','r','u','d']
        
        #UP
        if 'u' in moves:
            self.board[row - 1][col] = not self.board[row - 1][col]

        #DOWN
        if 'd' in moves:
            self.board[row + 1][col] = not self.board[row + 1][col]

        #LEFT
        if 'l' in moves:
            self.board[row][col - 1] = not self.board[row][col - 1]

        #RIGHT
        if 'r' in moves:
            self.board[row][col + 1] = not self.board[row][col + 1]

    def scramble(self):
        for row in range(self.M):
            for col in range(self.N):
                if (random.random()<0.5):
                    self.perform_move(row,col)

    def is_solved(self):
        return not (True in (light for row in self.board for light in row))

    def copy(self):
        board_copy = copy.deepcopy(self.board)
        return LightsOutPuzzle(board_copy)

    def successors(self):
        for row in range(self.M):
            for col in range(self.N):
                initial_state = self.copy()
                initial_state.perform_move(row,col)
                yield ((row,col), initial_state)
                

    def as_tuple(self):
        return tuple(tuple(row) for row in self.board)
    
    def find_solution(self):
        
        graph = {} # current:(parent,move)
        queue, solution = [], []
        visited = set()

        # add myself to the queue
        queue.append(self)

        # while queue is still active, keep looking for a solution
        while(queue):
            current = queue.pop(0)

            # yay, we found one!
            if (current.is_solved()):
                # trace back our steps till we reach our starting point
                while (current != self):
                    # and collect our moves along the way
                    solution.append(graph[current][1])
                    current = graph[current][0]
                return solution[::-1]

            # keep looking - enqueue all non-visited immediate successors
            else:
                for move, successor in current.successors():
                    if (successor.as_tuple() not in visited):
                        visited.add(successor.as_tuple())

                        # hash the successor to its parent and transition move
                        graph[successor] = (current,move)
                        queue.append(successor)

        # done if no more in queue
        return None

def create_puzzle(rows, cols):
    board = [[False for c in range(cols)] for r in range(rows)]
    return LightsOutPuzzle(board)
