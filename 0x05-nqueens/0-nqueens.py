#!/usr/bin/env python3
"""
This module solves the n queens math problem

"""
import sys


def is_safe(board, row, col):
    """
    Checks if it is safe to place a queen

    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, solutions):
    """
    Uses backtracking to find all solutions

    """
    n = len(board)
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, solutions)
            board[row] = -1


def n_queens(n):
    """
    Solves the N-Queens problem and print all solutions

    """
    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, solutions)
    return solutions


def print_solutions(solutions):
    """
    Print the solutions in the required format

    """
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(len(solution))]
        print(formatted_solution)


def main():
    """
    Main entry point to execute the solution

    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = n_queens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
