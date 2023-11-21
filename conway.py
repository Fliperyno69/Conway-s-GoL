import numpy as np
import time


def create_random_board(rows, cols):
    return np.random.choice([0, 1], size=(rows, cols), p=[0.8, 0.2])


def print_board(board):
    for row in board:
        print(' '.join(['⬜' if cell else '⬛' for cell in row]))
    print()


def get_neighbors(board, x, y):
    rows, cols = board.shape
    neighbors = []

    for i in range(max(0, x - 1), min(rows, x + 2)):
        for j in range(max(0, y - 1), min(cols, y + 2)):
            if i != x or j != y:
                neighbors.append(board[i, j])

    return neighbors


def update_board(board):
    new_board = board.copy()
    rows, cols = board.shape

    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(board, i, j)
            live_neighbors = sum(neighbors)

            if board[i, j]:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[i, j] = 0
            else:
                if live_neighbors == 3:
                    new_board[i, j] = 1

    return new_board


def is_stable(history):
    return any((np.array_equal(history[-1], state) for state in history[:-1]))


def life_simulation(rows, cols, max_steps=100):
    board = create_random_board(rows, cols)
    history = [board.copy()]

    for step in range(max_steps):
        board = update_board(board)
        history.append(board.copy())
        print(f"Step {step + 1}")
        print_board(board)

        if is_stable(history[-11:]):
            print("End")
            break

        time.sleep(0.5)


if __name__ == "__main__":
    rows = 10
    cols = 10
    life_simulation(rows, cols)
