from board import Board
from ai import get_best_column
import unittest

class MyTest(unittest.TestCase):
    def test1(self):
        grid = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [1,1,2,0,2,2,0]]
        board = Board(grid)
        self.assertEqual(get_best_column(board,True),3)

    def test2(self):
        grid = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,2,0,0,0,0],
                [0,2,1,1,0,0,0],
                [2,1,1,1,2,0,0],
                [1,1,1,2,2,0,0]]
        board = Board(grid)
        self.assertEqual(get_best_column(board,True),3)

    def test3(self):
        grid = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0],
                [1,0,2,0,0,0,0],
                [1,2,2,0,0,0,0]]
        board = Board(grid)
        self.assertEqual(get_best_column(board,True),0)

    def test4(self):
        grid = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,2,1,0,0,0],
                [0,2,1,1,0,0,0],
                [2,1,1,1,2,0,0],
                [1,1,1,2,2,0,0]]
        board = Board(grid)
        self.assertTrue(board.check_win())

    def test5(self):
        grid = [[0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0],
                [0,1,2,0,0,0,0],
                [0,2,1,2,0,0,0],
                [2,1,1,1,2,0,0],
                [1,1,1,2,2,0,0]]
        board = Board(grid)
        self.assertTrue(board.check_win())

    def test6(self):
        grid = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [1,1,1,1,0,0,0],
                [2,2,1,2,0,0,0],
                [2,2,1,1,2,0,0],
                [1,1,1,2,2,0,0]]
        board = Board(grid)
        self.assertTrue(board.check_win())

    def test7(self): #check for a tie
        grid = [[1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1]]
        board = Board(grid)
        self.assertTrue(board.check_win())
        
if __name__ == '__main__':
    unittest.main()
