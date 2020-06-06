# class Sudoku :
#     def __init__(self, board) :
#         self.board = board

#     def drawSudoku(self) :
#         draw = ''
#         for i in range(len(self.board)) :
#             for j in range(len(self.board[i])) :
#                 if (self.board[i][j] == 0) :
#                     draw += '# '
#                 else :
#                     draw += str(self.board[i][j]) + ' '
#                 if (j == 2 or j == 5) :
#                     draw += '| '
#             if (i != 8) :
#                 draw += '\n'
#             if (i == 2 or i == 5) :
#                 draw += '- - - - - - - - - - - \n'
#         print(draw)
#         # return draw

#     def findEmpty(self) :
#         for i in range(9) :
#             for j in range(9) :
#                 if (self.board[i][j] == 0) :
#                     return (i,j)
#         return None

#     def isValid(self, row, col, x) :
#         """
#         Checking whether x is valid or not
#         Valid if :
#             x is not on spesific row
#             x is not on spesific col
#         """
#         # Check column per row (horizontal)
#         for i in range(9) :
#             if (self.board[row][i] == x) :
#                 return False
#         # Check row per column (vertical)
#         for i in range(9) :
#             if (self.board[i][col] == x) :
#                 return False
#         # Check squares
#         row_square = (row // 3) * 3
#         col_square = (col // 3) * 3
#         for i in range(3) :
#             for j in range(3) :
#                 if (self.board[i+row_square][j+col_square] == x) :
#                     return False
#         # Valid
#         return True

#     # def solve(self) :
#     #     """
#     #     Using recursion-backtracking method for solving
#     #     sudoku puzzle.
#     #     """
#     #     # find = self.findEmpty()
#     #     # if not find :
#     #     #     return True
#     #     # else :
#     #     # Loop for every row
#     #     for i in range(9) :
#     #         # Loop for every col
#     #         for j in range(9) :
#     #             if (self.board[i][j] == 0) :
#     #                 # Check possibilities numbers from 1-9
#     #                 for k in range(1,10) :
#     #                     if (self.isValid(i, j, k)) :
#     #                         self.board[i][j] = k
#     #                         # Recursion
#     #                         self.solve()
#     #                         # Backtrack
#     #                         self.board[i][j] = 0
#     #                 # Return here if all possibilities numbers were checked
#     #                 return
#     #     self.drawSudoku()

#     def valid(self, num, pos) :
#         for i in range(9) :
#             if (self.board[pos[0]][i] == num and pos[1] != i) :
#                 return False
#         for i in range(9) :
#             if (self.board[i][pos[1]] == num and pos[0] != i) :
#                 return False
#         x = (pos[1] // 3) * 3
#         y = (pos[0] // 3) * 3
#         for i in range(x, y + 3) :
#             for j in range(x, y + 3) :
#                 if self.board[i][j] == num and (i,j) != pos :
#                     return False
#         return True

#     def solve(self) :
#         find = self.findEmpty()
#         if not find :
#             return True
#         else :
#             row, col = find
#         for i in range(1, 10) :
#             if self.valid(i, (row, col)) :
#                 self.board[row][col] = i

#                 if (self.solve()) :
#                     return True
                
#                 self.board[row][col] = 0

#         return False

class Sudoku :
    def __init__(self, board):
        self.board = board
    
    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def valid(self, num, pos):
        # Check row
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # # Check box
        # box_x = pos[1] // 3
        # box_y = pos[0] // 3

        # for i in range(box_y*3, box_y*3 + 3):
        #     for j in range(box_x * 3, box_x*3 + 3):
        #         if self.board[i][j] == num and (i,j) != pos:
        #             return False

        return True


    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")


    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col

        return None