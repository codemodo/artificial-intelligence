import lights-out
import unittest

class TestLightsOut(unittest.TestCase):

    def test_init(self):
        puzzle = hw2.LightsOutPuzzle([[True, False, True],
                                      [False, False, False]])
        self.assertEqual(2, puzzle.M)
        self.assertEqual(3, puzzle.N)
        self.assertEqual([[True, False, True],[False, False, False]], puzzle.get_board())

    def test_get_board(self):
        puzzle = hw2.create_puzzle(4,5)
        self.assertEqual([ [False,False,False,False,False],
                            [False,False,False,False,False],
                            [False,False,False,False,False],
                            [False,False,False,False,False] ], puzzle.get_board())

    def test_perform_move(self):
        puzzle = hw2.LightsOutPuzzle([[True, False, True],
                                      [False, False, False]])
        puzzle.perform_move(0,0);
        self.assertEqual([[False,True,True], [True,False,False]], puzzle.get_board())

        puzzle = hw2.create_puzzle(3,3)
        puzzle.perform_move(1,1)
        self.assertEqual([[False, True, False],
                          [True,  True, True ],
                          [False, True, False]], puzzle.get_board())


    def test_scramble(self):
        puzzle = hw2.create_puzzle(3,4)
        puzzle.scramble()

    def test_is_solved(self):
        puzzle = hw2.LightsOutPuzzle([[True, False, True],
                                      [False, False, False]])
        self.assertFalse(puzzle.is_solved())

        puzzle = hw2.create_puzzle(5,7)
        self.assertTrue(puzzle.is_solved())

    def test_copy(self):
        puzzle1 = hw2.create_puzzle(4,4)
        puzzle2 = puzzle1.copy()
        self.assertEqual(puzzle1.get_board(),puzzle2.get_board())
        self.assertFalse(puzzle1.get_board()is puzzle2.get_board())

        puzzle2.perform_move(0,0)
        self.assertNotEqual(puzzle1.get_board(),puzzle2.get_board())

        puzzle1.perform_move(0,0)
        self.assertEqual(puzzle1.get_board(),puzzle2.get_board())

        puzzle1.perform_move(3,2)
        self.assertNotEqual(puzzle1.get_board(),puzzle2.get_board())

    def test_find_solution(self):
        p = hw2.create_puzzle(2, 3)
        for row in range(2):
            for col in range(3):
                p.perform_move(row, col)
        self.assertEqual([(0, 0), (0, 2)], p.find_solution())

if __name__ == '__main__':
    unittest.main()
