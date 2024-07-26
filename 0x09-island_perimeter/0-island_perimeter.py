#!/usr/bin/python3
"""
Island perimeter module
"""


def island_perimeter(grid: list[list[str]]) -> int:
    """
    Solve island perimeter problem
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r-1][c] == 1:  # Up
                    perimeter -= 1
                if r < rows - 1 and grid[r+1][c] == 1:  # Down
                    perimeter -= 1
                if c > 0 and grid[r][c-1] == 1:  # Left
                    perimeter -= 1
                if c < cols - 1 and grid[r][c+1] == 1:  # Right
                    perimeter -= 1

    return perimeter
