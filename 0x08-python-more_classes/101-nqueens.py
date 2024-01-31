#!/usr/bin/python3
"""Solves the N-queens puzzle.

This script finds all possible solutions for placing N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

    N must be an integer greater than or equal to 4.

Attributes:
    board (list): A 2D list representing the chessboard.
    solutions (list): A list of solutions, where each solution is represented as a list of queen positions.
"""

import sys


def init_board(n):
    """Initialize an empty chessboard of size `n`x`n`.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A 2D list representing the chessboard.
    """
    return [[' ' for _ in range(n)] for _ in range(n)]


def get_solution(board):
    """Get the positions of queens on the chessboard.

    Args:
        board (list): The current state of the chessboard.

    Returns:
        list: A list of queen positions as [row, column].
    """
    return [[r, c] for r in range(len(board)) for c in range(len(board)) if board[r][c] == "Q"]


def xout(board, row, col):
    """Mark positions on the chessboard as non-attacking.

    All spots where non-attacking queens can no longer be placed are marked with 'x'.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    n = len(board)
    
    # X out all forward spots
    for c in range(col + 1, n):
        if 0 <= row < n and 0 <= c < n:
            board[row][c] = "x"

    # X out all backward spots
    for c in range(col - 1, -1, -1):
        if 0 <= row < n and 0 <= c < n:
            board[row][c] = "x"

    # X out all spots below
    for r in range(row + 1, n):
        if 0 <= r < n and 0 <= col < n:
            board[r][col] = "x"

    # X out all spots above
    for r in range(row - 1, -1, -1):
        if 0 <= r < n and 0 <= col < n:
            board[r][col] = "x"

    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, n):
        if 0 <= r < n and 0 <= c < n:
            board[r][c] = "x"
            c += 1

    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if 0 <= r < n and 0 <= c < n:
            board[r][c] = "x"
            c -= 1

    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if 0 <= r < n and 0 <= c < n:
            board[r][c] = "x"
            c += 1

    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, n):
        if 0 <= r < n and 0 <= c < n:
            board[r][c] = "x"
            c -= 1



def recursive_solve(board, row, queens, solutions):
    """Recursively solve the N-queens puzzle.

    Args:
        board (list): The current state of the chessboard.
        row (int): The current row being explored.
        queens (int): The number of queens currently placed on the chessboard.
        solutions (list): A list of solutions found so far.

    Returns:
        list: A list of solutions found.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = [row.copy() for row in board]
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        print("Usage: nqueens N (N must be an integer greater than or equal to 4)")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)

