def is_safe(board, row, col):

    for prev_row in range(row):

        placed_col = board[prev_row]

        if placed_col == col:
            return False

        if abs(prev_row - row) == abs(placed_col - col):
            return False

    return True


def solve_n_queens(n):

    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):

        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):

            if is_safe(board, row, col):

                board[row] = col

                backtrack(row + 1)

                board[row] = -1

                backtrack_count[0] += 1

    backtrack(0)

    return solutions, backtrack_count[0]


def get_board(solution, n):

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
