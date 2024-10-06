import collections


class Solution:
    board1, board2 = 0, 0


'''
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
    1.Each row must contain the digits 1-9 without duplicates.
    2.Each column must contain the digits 1-9 without duplicates.
    3.Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false
Note: A board does not need to be full or be solvable to be valid.
'''


def isValidSudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":  # if there is an empty position, continue
                continue
            if (board[r][c] in rows[r] or  # if the current digit(board[r][c]) is already in the rows
                    board[r][c] in cols[c] or  # cols, or squares...
                    board[r][c] in squares[(r // 3,
                                            c // 3)]):
                return False  # return false because only 1 valid ## is accepted
            cols[c].add(board[r][c])  # add current column digit to board
            rows[r].add(board[r][c])  # ditto, except rows
            squares[(r // 3, c // 3)].add(board[r][c])  # ditto, except squares
    return True


board1 = [["1", "2", ".", ".", "3", ".", ".", ".", "."], ["4", ".", ".", "5", ".", ".", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", ".", "3"], ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
          [".", ".", ".", "8", ".", "3", ".", ".", "5"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", ".", ".", ".", ".", ".", "2", ".", "."], [".", ".", ".", "4", "1", "9", ".", ".", "8"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
board2 = [["1", "2", ".", ".", "3", ".", ".", ".", "."], ["4", ".", ".", "5", ".", ".", ".", ".", "."],
          [".", "4", "8", ".", ".", ".", ".", ".", "3"], ["2", ".", ".", ".", "6", ".", ".", ".", "4"],
          [".", ".", ".", "1", ".", "3", ".", ".", "5"], ["3", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", ".", ".", ".", ".", ".", "2", ".", "."], [".", ".", ".", "4", "1", "9", ".", ".", "8"],
          [".", ".", ".", ".", "4", ".", ".", "4", "9"]]

print(isValidSudoku(board1))
print(isValidSudoku(board2))
