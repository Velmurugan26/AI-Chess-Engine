import pygame
from board import ChessBoard
from chess_engine import ChessAI

# Pygame settings
pygame.init()
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Chess Engine ♟️")

# Colors
WHITE = (245, 245, 245)
BLACK = (30, 30, 30)
HIGHLIGHT = (0, 255, 0)

# Load piece images
IMAGES = {}
PIECES = ["WP", "BP"]
for piece in PIECES:
    IMAGES[piece] = pygame.transform.scale(
        pygame.image.load(f"assets/{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE)
    )

def draw_board(win, board):
    win.fill(WHITE)
    for r in range(ROWS):
        for c in range(COLS):
            if (r + c) % 2 != 0:
                pygame.draw.rect(win, BLACK, (c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board.board[r][c]
            if piece != "--":
                win.blit(IMAGES[piece], (c*SQUARE_SIZE, r*SQUARE_SIZE))
    pygame.display.update()

def main():
    board = ChessBoard()
    ai = ChessAI(depth=3)  # AI difficulty level: 3
    clock = pygame.time.Clock()
    run = True
    selected_square = None
    player_color = "W"

    while run:
        draw_board(WIN, board)
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and player_color == "W":
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                if selected_square:
                    start_row, start_col = selected_square
                    move = f"{chr(start_col+97)}{8-start_row}{chr(col+97)}{8-row}"
                    if board.make_move(move, "W"):
                        selected_square = None
                        # AI turn
                        ai_move = ai.get_best_move(board)
                        board.make_move(ai_move, "B")
                    else:
                        selected_square = (row, col)
                else:
                    selected_square = (row, col)

        # Check for game over
        if board.is_game_over():
            winner = board.get_winner()
            print(f"Game Over! Winner: {winner}")
            run = False

    pygame.quit()

if __name__ == "__main__":
    main()
