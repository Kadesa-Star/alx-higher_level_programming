#!/usr/bin/python3
""" a program tha prints all possible solutions to a queens problem """


import sys


def is_safe(board, row, col, N):
    """check if there is a queen in the same column of that row"""
    for k in range(row):
        if board[k][col] == 1:
            return False

    # check upper diagonal on the left side
    for k, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[k][j] == 1:
            return False

    # check upper diagonal on the right side
    for k, j in zip(range(row, -1, -1), range(col, N)):
        if board[k][j] == 1:
            return False

    return True


def solve_n_queens(board, row, N):
    """recursively solves the N queens problem using backtracking."""
    if row == N:
        print_solution(board, N)
        return True

    res = False
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            res = solve_n_queens(board, row + 1, N) or res
            board[row][col] = 0
        # backtrack if placing queen at board[row][col] doesnt lead to solution

    return res


def print_solution(board, N):
    """
    This function prints the current state
    of the board, representing queens as '1'
    and empty squares as '0'."""
    solution = []
    for k in range(N):
        for j in range(N):
            if board[j][k] == 1:
                solution.append([k, j])
    print(solution)


def nqueens(N):
    """ This is the main function that
    orchestrates the solving of the N
    queens problem."""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    # check if N is atleast 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for s in range(N)] for s in range(N)]
    solve_n_queens(board, 0, N)


if __name__ == "__main__":
    """It checks if the correct number of
    arguments is provided when running the script"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
