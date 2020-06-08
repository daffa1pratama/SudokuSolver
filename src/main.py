from FileHandler import *
from Sudoku import *
import numpy as np
import sys

file = sys.argv[1].split('.')
filename = file[0]
fileformat = file[1]

if (fileformat != 'txt' and fileformat != 'png') :
    print("Error : Invalid file format. Please input txt/png file format !")
    sys.exit
else :
    print("=== SUDOKU SOLVER ===")
    if (fileformat == 'txt') :
        board = readTextFile(filename)
    elif (fileformat == 'png') :
        board = readImageFile(filename)
    sudoku = Sudoku(board)
    sudoku.drawSudoku()
    sudoku.solve()
    result = sudoku.drawResult()
    result += sudoku.getNumberFive()
    writeFile(filename, result)