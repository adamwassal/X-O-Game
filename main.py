import pygame, sys
import numpy as np

pygame.init()

screen_height = 800
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARDS_COLS = 3

CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (239, 231, 200)
CROSS_WIDTH = 25
SPACE = 55

RED = (255, 0, 0)
BG_COLOR = (18, 170, 156)
LINE_COLOR = (23, 145, 135)
CROSS_COLOR = (66, 66, 66)
font = pygame.font.SysFont("Constantia", 30)
text_col = (78, 81, 139)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("Tic Tac Toe")
screen.fill( BG_COLOR )

board = np.zeros( (BOARD_ROWS, BOARDS_COLS) )



def draw_lines():
    pygame.draw.line( screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH )

    pygame.draw.line( screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH )

    pygame.draw.line( screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH )

    pygame.draw.line( screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH )

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARDS_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100),int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)

            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE , row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE , row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def avilable_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARDS_COLS):
            if board[row][col] == 0:
                return False

    return True

def check_win(player):
    for col in range(BOARDS_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True


    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2]== player:
            draw_horizontal_winning_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True


    return False





def draw_vertical_winning_line(col, player):
    posx = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posx, 15), (posx, HEIGHT - 15), 15)

def draw_horizontal_winning_line(row, player):
    posy = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posy), (WIDTH - 15, posy), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15),15)

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15),15)



def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARDS_COLS):
            board[row][col] = 0

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

player = 1
game_over = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mousex = event.pos[0]
            mousey = event.pos[1]

            clicked_row = int(mousey // 200)
            clicked_col = int(mousex // 200)

            if avilable_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    draw_text("CLICK r  TO START", font, text_col, 50, 8)
                    game_over = True
                player = player %  2 + 1



                draw_figures()
                print(board)


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                
                restart()
                game_over  = False


    pygame.display.update()

    draw_lines()