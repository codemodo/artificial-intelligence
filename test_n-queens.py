import n-queens
import unittest

class TestNQueens(unittest.TestCase):

    def test_num_placements_all(self):
        self.assertEqual(1820, hw2.num_placements_all(4))
        self.assertEqual(4426165368, hw2.num_placements_all(8))

    def test_num_placements_one_per_row(self):
        self.assertEqual(16777216, hw2.num_placements_one_per_row(8))

    def test_n_queens_valid(self):
        self.assertEqual( False, hw2.n_queens_valid([0, 0]) )
        self.assertEqual( True, hw2.n_queens_valid([0, 3, 1]) )
        self.assertEqual( False, hw2.n_queens_valid([0, 1]) )
        self.assertEqual( True, hw2.n_queens_valid([]))

    def test_n_queens_solutions(self):
        pass
        #print list(hw2.n_queens_solutions(9))

if __name__ == '__main__':
    unittest.main()
