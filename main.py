import copy
import numpy as np
import pygame
import sys

if __name__ == '__main__':
    # Initialize
    max_tps = 2.0
    clock = pygame.time.Clock()
    delta = 0.0

    pygame.init()
    board_size = 400
    board_no_of_cells = 20
    board = np.zeros([board_no_of_cells, board_no_of_cells], dtype='int8')
    block_size = 20
    screen = pygame.display.set_mode((board_size, board_size))

    # kolumna, wiersz
    board[4, 2] = 1
    board[5, 2] = 1
    board[2, 3] = 1
    board[7, 3] = 1
    board[8, 4] = 1
    board[8, 5] = 1
    board[2, 5] = 1
    board[3, 6] = 1
    board[4, 6] = 1
    board[5, 6] = 1
    board[6, 6] = 1
    board[7, 6] = 1
    board[8, 6] = 1
    #
    while True:
        # Config events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
        screen.fill((0, 0, 0))

        delta += clock.tick()/1000.0
        while delta > 1 / max_tps:
            delta -= 1/max_tps

            # Iteration of game of life
            old_board = copy.deepcopy(board)
            for j in range(board_no_of_cells):
                for i in range(board_no_of_cells):
                    alive_neighbors = 0
                    if i > 0 and old_board[i - 1, j]:
                        alive_neighbors += 1
                    if i < board_no_of_cells - 1 and old_board[i + 1, j]:
                        alive_neighbors += 1
                    if j > 0 and old_board[i, j - 1]:
                        alive_neighbors += 1
                    if j < board_no_of_cells - 1 and old_board[i, j + 1]:
                        alive_neighbors += 1
                    if i > 0 and j > 0 and old_board[i-1, j-1]:
                        alive_neighbors += 1
                    if i > 0 and j < board_no_of_cells-1 and old_board[i-1, j+1]:
                        alive_neighbors += 1
                    if i < board_no_of_cells-1 and j > 0 and old_board[i+1, j-1]:
                        alive_neighbors += 1
                    if i < board_no_of_cells-1 and j < board_no_of_cells-1 and old_board[i+1, j+1]:
                        alive_neighbors += 1
                    if old_board[i, j] and (alive_neighbors < 2 or alive_neighbors > 3):  # alive cell
                        board[i, j] = 0  # cell dies
                    if old_board[i, j] == 0 and alive_neighbors == 3:  # dead cells
                        board[i, j] = 1  # cell is alive again
        # Drawing
        for i in range(0, board_size, block_size):
            for j in range(0, board_size, block_size):
                filled = 0
                color = (255, 255, 255)
                rectangle = pygame.Rect(i, j, block_size, block_size)
                if board[i // block_size, j // block_size]:
                    filled = 0
                else:
                    filled = 1
                pygame.draw.rect(screen, color, rectangle, filled)
        pygame.display.update()
