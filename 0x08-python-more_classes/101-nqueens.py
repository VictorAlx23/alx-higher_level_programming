#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.
"""

import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(board, row, solutions):
    """Solve the N-queens problem using backtracking."""
    if row == len(board):
        solutions.append([''.join(row) for row in board])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1, solutions)
            board[row][col] = ' '

def nqueens(N):
    """Solve the N-queens problem for a given N."""
    if N < 4:
        print("N must be at least 4")
        return

    board = init_board(N)
    solutions = []
    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])
    nqueens(N)

