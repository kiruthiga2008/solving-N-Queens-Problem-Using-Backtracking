def is_safe(board, row, col):
    """
    Check whether placing a queen at (row, col) is safe.
    """

    for prev_row in range(row):
        placed_col = board[prev_row]

        # Same column
        if placed_col == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed_col - col):
            return False

    return True


def solve_n_queens(n):
    """
    Solve the N-Queens problem using backtracking.

    Returns:
        solutions: List of all valid solutions
        backtrack_count: Number of backtracking operations
    """

    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):

        # All queens placed successfully
        if row == n:
            solutions.append(board[:])
            return

        # Try placing queen in every column
        for col in range(n):

            if is_safe(board, row, col):

                # Place queen
                board[row] = col

                # Move to next row
                backtrack(row + 1)

                # Remove queen and backtrack
                board[row] = -1
                backtrack_count[0] += 1

    backtrack(0)

    return solutions, backtrack_count[0]


def get_board(solution, n):
    """
    Convert a solution into a visual board.
    """

    board = []

    for row in range(n):

        current_row = []

        for col in range(n):

            if solution[row] == col:
                current_row.append("Q")
            else:
                current_row.append(".")

        board.append(current_row)

    return board
