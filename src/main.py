from FileHandler import *
from Sudoku import *
import numpy as np

f = FileHandler()
container = f.read('tc1')
# matrix = np.matrix(f.read('new'))
# print(matrix)
sudoku = Sudoku(container)
# draw = sudoku.drawSudoku()
sudoku.drawSudoku()
sudoku.solve()
# sudoku.drawSudoku()
# f.write('tc1', draw)