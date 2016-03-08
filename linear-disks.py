import math
import copy
import random

def solve_identical_disks(length, n):
    puzzle = LinearDisks(length, n, False)
    solution = puzzle.find_solution()
    return solution

def solve_distinct_disks(length, n):
    puzzle = LinearDisks(length, n, True)
    solution = puzzle.find_solution()
    return solution

class LinearDisks(object):

    def __init__(self, length, n, distinct_flag=False, board=None, id_board=None):
        self.distinct_flag = distinct_flag
        self.L = length
        self.N = n

        # wrote init initially as taking length and n and didn't want to change
        # once I realized down the line that I needed to be able to pass the board too
        if board is not None:
            self.board = board
        else:
            self.board = [True for disk in range(n)] + [False for empty in range(length-n)]

        # id_board only used for distinct solutions
        if id_board is not None:
            self.id_board = id_board
        else:
            self.id_board = [id for id in range(n)] + [-1 for empty in range(length-n)]

    def get_board(self):
        return self.board

    # helper for unit testing
    def set_board(self, board, length, n):
        self.board = board
        self.L = length
        self.N = n

    # does not care about the validity of the move... just makes it
    def perform_move(self, fr, to):
        self.board[fr] = not self.board[fr]
        self.board[to] = not self.board[to]

    def perform_id_move(self, fr, to):
        tmp = self.id_board[fr]
        self.id_board[fr] = self.id_board[to]
        self.id_board[to] = tmp


    # checks if solution reached for case when identical
    def is_solved_identical(self):
        n = self.N
        l = self.L
        return (all(disk==True for disk in self.board[:-(n+1):-1]) and all(disk==False for disk in self.board[:l-n]))

    # checks if solution reached for case when distinct
    def is_solved_distinct(self):
        if (self.is_solved_identical()):
            n=self.N
            length=self.L
            tmp = [id for id in range(n)] + [-1 for empty in range(length-n)]
            tmp.reverse()
            curr = copy.deepcopy(self.id_board)
            if (tmp == curr):
                return True
        return False

    def copy(self):
        board_copy = copy.deepcopy(self.board)
        id_board_copy = copy.deepcopy(self.id_board)
        return LinearDisks(self.L, self.N, self.distinct_flag, board_copy, id_board_copy)

    def successors(self):
        length = self.L
        for cell in range(length):

            # if cell has disk
            if (self.board[cell]):

                # 2 left
                if (cell-2 >= 0):
                    if ((not self.board[cell-2]) and (self.board[cell-1])):
                        tmp_state = self.copy()
                        tmp_state.perform_move(cell, cell-2)
                        tmp_state.perform_id_move(cell, cell-2)
                        yield ((cell,cell-2), tmp_state)

                # 1 left
                if (cell-1 >= 0):
                    if (not self.board[cell-1]):
                        tmp_state = self.copy()
                        tmp_state.perform_move(cell, cell-1)
                        tmp_state.perform_id_move(cell, cell-1)
                        yield ((cell,cell-1), tmp_state)

                # 1 right
                if (cell+1 < length):
                    if (not self.board[cell+1]):
                        tmp_state = self.copy()
                        tmp_state.perform_move(cell, cell+1)
                        tmp_state.perform_id_move(cell, cell+1)
                        yield ((cell,cell+1), tmp_state)

                # 2 right
                if (cell+2 < length):
                    if ((not self.board[cell+2]) and (self.board[cell+1])):
                        tmp_state = self.copy()
                        tmp_state.perform_move(cell, cell+2)
                        tmp_state.perform_id_move(cell, cell+2)
                        yield ((cell,cell+2), tmp_state)
                

    # handles both identical and distinct cases
    def as_tuple(self):
        if(not self.distinct_flag):
            return tuple(cell for cell in self.board)
        return tuple(cell for cell in self.board) + tuple(cell for cell in self.id_board)

    # handles both identical and distinct cases
    def find_solution(self):
        
        graph = {} # current:(parent,move)
        queue, solution = [], []
        visited = set()

        # add myself to the queue
        queue.append(self)

        # while queue is still active, keep looking for a solution
        while(queue):
            current = queue.pop(0)

            if  (   #found a solution when disks are identical
                    ((not current.distinct_flag) and current.is_solved_identical())
                    or
                    #found a solution when disks are distinct
                    (current.distinct_flag and current.is_solved_distinct())
                ):
                
                # trace back our steps till we reach our starting point
                while (current != self):
                    # and collect our moves along the way
                    solution.append(graph[current][1])
                    current = graph[current][0]
                return solution[::-1]

            else: # not a solution, so enqueue all non-visited immediate successors
                for move, successor in current.successors():
                    if (successor.as_tuple() not in visited):
                        visited.add(successor.as_tuple())

                        # hash the successor to its parent and transition move
                        graph[successor] = (current,move)
                        queue.append(successor)

        # done if no more in queue
        return None
