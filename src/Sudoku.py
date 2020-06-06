class Sudoku :
    def __init__(self, board) :
        self.board = board

    def drawSudoku(self) :
        """
        Draw Sudoku board
        """
        draw = ''
        for i in range(len(self.board)) :
            for j in range(len(self.board[i])) :
                if (self.board[i][j] == 0) :
                    draw += '# '
                else :
                    draw += str(self.board[i][j]) + ' '
                if (j == 2 or j == 5) :
                    draw += '| '
            if (i != 8) :
                draw += '\n'
            if (i == 2 or i == 5) :
                draw += '- - - - - - - - - - - \n'
        print(draw)
        # return draw

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
        # Valid
        return True
    
    def isFull(self) :
        """
        Check whether the board is full
        or still has empty spot
        """
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
            self.drawSudoku()
            return
        # Recurrences
        else :
            # print('======================')
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