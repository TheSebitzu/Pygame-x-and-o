# Example file showing a basic pygame "game loop"
import pygame
import sys


def main():

    # pygame setup
    pygame.init()
    font = pygame.font.Font(None, 300)

    # Set desired resolution here
    screen = pygame.display.set_mode((1000, 1000))

    clock = pygame.time.Clock()
    running = True

    game_end_time = 0

    # Empty board
    board = ["", "", "", "", "", "", "", "", ""]

    # Whose turn it is
    turn = "x"

    # Message to display
    winner_message = []
    font_winner = pygame.font.Font(None, 100)

    game_over = False

    # Get resolution
    height = screen.get_height()
    width = screen.get_width()

    while running:
        # Poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        # Fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        if pygame.mouse.get_pressed()[0] and not game_over:
            # Get mouse position
            x = int(pygame.mouse.get_pos()[0] / (screen.get_width() / 3))
            y = int(pygame.mouse.get_pos()[1] / (screen.get_height() / 3))

            # Calculate board position based on where mouse is
            if board[y * 3 + x] == "":
                board[y * 3 + x] = turn

                # Switch turn
                turn = "o" if turn == "x" else "x"

                if winner(board) == "x" or winner(board) == "o":
                    # print("-------------------")
                    # print(f"| Winner is ... {winner(board).upper()} |")
                    # print("-------------------")
                    winner_message = [
                        "-------------------",
                        f"| Winner is ... {winner(board).upper()} |",
                        "-------------------",
                    ]
                    game_over = True
                    game_end_time = pygame.time.get_ticks()

                elif winner(board) == "draw":
                    # print("---------------")
                    # print(f"| It's a draw |")
                    # print("---------------")
                    winner_message = [
                        "---------------",
                        "| It's a draw |",
                        "---------------",
                    ]
                    game_over = True
                    game_end_time = pygame.time.get_ticks()

        # Display winner message
        if game_over:
            if game_over:
                screen.fill("white")
                if pygame.time.get_ticks() - game_end_time > 3000:
                    for i, line in enumerate(winner_message):
                        text_surface = font_winner.render(line, True, "blue")
                        text_rect = text_surface.get_rect(center=(width // 2, height // 2 + i * 50))
                        screen.blit(text_surface, text_rect)

        # RENDER YOUR GAME HERE
        # pygame.draw.line(screen, "black", (0, 0), (width, height), 10)
        render_grid(screen)
        render_pieces(board, font, screen)
        draw_winner(board, screen)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


def render_grid(screen):
    height = screen.get_height()
    width = screen.get_width()

    # Draw the lines
    pygame.draw.line(screen, "black", (width / 3, 0), (width / 3, height), 1)
    pygame.draw.line(screen, "black", (width * 2 / 3, 0), (width * 2 / 3, height), 1)

    pygame.draw.line(screen, "black", (0, height / 3), (width, height / 3), 1)
    pygame.draw.line(screen, "black", (0, height * 2 / 3), (width, height * 2 / 3), 1)


def render_pieces(board, font, screen):
    for i in range(len(board)):
        pos_x = i % 3 * screen.get_width() / 3
        pos_y = int(i / 3) * screen.get_height() / 3
        screen.blit(font.render(board[i], True, "black"), (pos_x, pos_y))


def draw_winner(board, screen):

    height = screen.get_height()
    width = screen.get_width()

    cell_width = width / 3
    cell_height = height / 3

    # If 3 in a row are the same
    if board[0] == board[1] == board[2] != "":
        # Draw line
        pygame.draw.line(
            screen, "red", (0, 1 / 2 * cell_height), (width, 1 / 2 * cell_height), 10
        )
    if board[3] == board[4] == board[5] != "":
        pygame.draw.line(
            screen, "red", (0, 3 / 2 * cell_height), (width, 3 / 2 * cell_height), 10
        )
    if board[6] == board[7] == board[8] != "":
        pygame.draw.line(
            screen, "red", (0, 5 / 2 * cell_height), (width, 5 / 2 * cell_height), 10
        )

    if board[0] == board[3] == board[6] != "":
        pygame.draw.line(
            screen, "red", (1 / 2 * cell_width, 0), (1 / 2 * cell_width, height), 10
        )
    if board[1] == board[4] == board[7] != "":
        pygame.draw.line(
            screen, "red", (3 / 2 * cell_width, 0), (3 / 2 * cell_width, height), 10
        )
    if board[2] == board[5] == board[8] != "":
        pygame.draw.line(
            screen, "red", (5 / 2 * cell_width, 0), (5 / 2 * cell_width, height), 10
        )

    if board[0] == board[4] == board[8] != "":
        pygame.draw.line(screen, "red", (0, 0), (width, height), 10)
    if board[2] == board[4] == board[6] != "":
        pygame.draw.line(screen, "red", (width, 0), (0, height), 10)


def winner(board):

    if board[0] == board[1] == board[2]:
        return board[0]
    if board[3] == board[4] == board[5]:
        return board[3]
    if board[6] == board[7] == board[8]:
        return board[6]

    if board[0] == board[3] == board[6]:
        return board[0]
    if board[1] == board[4] == board[7]:
        return board[1]
    if board[2] == board[5] == board[8]:
        return board[2]

    if board[0] == board[4] == board[8]:
        return board[0]
    if board[2] == board[4] == board[6]:
        return board[2]

    if len("".join(board)) == 9:
        return "draw"

    return ""


if __name__ == "__main__":
    main()
