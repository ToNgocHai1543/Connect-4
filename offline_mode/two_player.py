import pygame
import sys
import math
from constants import *
from game_logic import *

def play_2p():
    board = create_board()
    game_over = False
    turn = 0

    pygame.init()

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE
    size = (width, height)

    screen_game = pygame.display.set_mode(size)
    draw_board(board, screen_game)
    pygame.display.update()

    myfont = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen_game, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen_game, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else: 
                    pygame.draw.circle(screen_game, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen_game, BLACK, (0,0, width, SQUARESIZE))
                #print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render("Player 1 wins!!", 1, RED)
                            screen_game.blit(label, (40,10))
                            game_over = True


                # # Ask for Player 2 Input
                else:				
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render("Player 2 wins!!", 1, YELLOW)
                            screen_game.blit(label, (40,10))
                            game_over = True

                print_board(board)
                draw_board(board, screen_game)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)


