import copy

class Sudoku :
    def __init__(self, board) :
        self.board = board
        self.found = False

    def drawSudoku(self) :
        """
        Draw Sudoku board
        """
        draw = "======= Before ======\n"
        # Start draw sudoku
        for i in range(9) :
            for j in range(9) :
                if (self.board[i][j] == 0) :
                    draw += '# '
                else :
                    draw += str(self.board[i][j]) + ' '
                if (j == 2 or j == 5) :
                    draw += '| '
            draw += '\n'
            if (i == 2 or i == 5) :
                draw += '- - - - - - - - - - - \n'
        print(draw)

    def drawResult(self) :
        """
        Draw Sudoku board
        """
        draw = "======= After =======\n"
        # Start draw sudoku
        for i in range(9) :
            for j in range(9) :
                draw += str(self.result[i][j]) + ' '
                if (j == 2 or j == 5) :
                    draw += '| '
            draw += '\n'
            if (i == 2 or i == 5) :
                draw += '- - - - - - - - - - - \n'
        print(draw)
        return draw
    
    def getNumberFive(self) :
        """
        Get number 5 coordinate from board
        """
        result = "==== 5 Coordinate ===\n"
        count = 1
        # Start get 5 coordinate
        for i in range(9) :
            for j in range(9) :
                if (self.result[i][j] == 5) :
                    result += str(count) + '. (' + str(i+1) + ',' + str(j+1) + ')\n'
                    count += 1
        print(result)
        return result

    def isValid(self, row, col, x) :
        """
        Checking whether x is valid or not
        Valid if :
            x is not on spesific row
            x is not on spesific col
        """
        # Check column per row (horizontal)
        for i in range(9) :
            if (self.board[row][i] == x) :
                return False
        # Check row per column (vertical)
        for i in range(9) :
            if (self.board[i][col] == x) :
                return False
        # Check squares
        row_square = (row // 3) * 3
        col_square = (col // 3) * 3
        for i in range(3) :
            for j in range(3) :
                if (self.board[i+row_square][j+col_square] == x) :
                    return False
        # Valid
        return True
    
    def isFull(self) :
        """
        Check whether the board is full
        or still has empty spot
        """
        # Start checking element
        for i in range(9) :
            for j in range(9) :
                if (self.board[i][j] == 0) :
                    return False
        return True
 
    def solve(self) :
        """
        Using recursion-backtracking method for solving
        sudoku puzzle.
        """
        # Basis
        if self.isFull() :
            if not self.found :
                self.found = True
                self.result = copy.deepcopy(self.board)
            return
        # Recurrences
        else :
            # Loop for every row
            for i in range(9) :
                # Loop for every column
                for j in range(9) :
                    if (self.board[i][j] == 0) :
                        # Check all posibilities numbers between 1 and 9
                        for k in range(1, 10) :
                            if (self.isValid(i, j, k)) :
                                self.board[i][j] = k
                                # Recursion
                                self.solve()
                                # Backtrack
                                self.board[i][j] = 0
                        # Return here if all possibilities numbers were checked 
                        return