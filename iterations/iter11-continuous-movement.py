################ User: ############################

# next iteration: currently, if the player holds down the DOWN key, a piece will only move down one line. they need to keep tapping the DOWN key to move the piece all the way to the bottom. how can we fix that so if they hit the key once, it moves down one space, but if they hold the key down it repeats?

################ Iterative Coding: ################

# To implement a feature where holding down the DOWN key continuously moves the tetromino downwards until it locks in place, you need to adjust the event handling in your game loop to differentiate between a single key press and holding down a key. Pygame's event system can detect both scenarios, but for continuous movement, you should use the state of the keys rather than the event queue. This approach involves checking the current state of specific keys each frame, rather than relying solely on the event queue.

# Here's how you can modify your game loop to support this feature:

# ### Updated Game Loop with Continuous Downward Movement

# ```python
# def run(self):
#     while True:  # This outer loop allows the game to be restarted
#         self.reset_game()  # Reset the game state before starting/restarting the game
#         while not self.is_game_over:
#             current_time = pygame.time.get_ticks()
#             keys = pygame.key.get_pressed()  # Get the state of all keyboard keys

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     return  # Exit the entire game
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_LEFT:
#                         self.move(-1, 0)
#                     elif event.key == pygame.K_RIGHT:
#                         self.move(1, 0)
#                     elif event.key == pygame.K_UP:
#                         self.rotate_piece()

#             # Continuous downward movement when the DOWN key is held
#             if keys[pygame.K_DOWN]:
#                 self.move(0, 1)

#             # Adjusting the drop speed for continuous movement
#             # This checks if the DOWN key is pressed and adjusts the drop speed accordingly
#             drop_speed_adjusted = self.drop_speed
#             if keys[pygame.K_DOWN]:
#                 drop_speed_adjusted = max(50, drop_speed_adjusted // 10)  # Adjust drop speed for faster fall

#             if current_time - self.last_drop_time > drop_speed_adjusted:
#                 if not self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y + 1)):
#                     self.move(0, 1)
#                 else:
#                     self.lock_piece()
#                     # Check for game over condition right after locking a piece
#                     if self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y)):
#                         self.is_game_over = True
#                 self.last_drop_time = current_time

#             self.screen.fill((0, 0, 0))
#             self.draw_grid()
#             self.draw_piece(self.current_piece)
#             self.draw_score()
#             pygame.display.flip()
#             self.clock.tick(60)

#             if self.is_game_over:
#                 self.game_over_screen()  # Display game over screen
# ```

# ### Key Changes and Features:

# - **Key State Checking**: By calling `pygame.key.get_pressed()`, you obtain the state of all keys. This allows you to check if the DOWN key is currently pressed down on each frame.
# - **Continuous Movement**: If the DOWN key is pressed, `self.move(0, 1)` is called outside the event loop, enabling continuous movement downwards as long as the key is held.
# - **Drop Speed Adjustment**: When the DOWN key is held, the drop speed is significantly reduced to allow the piece to move down faster. The `drop_speed_adjusted` variable allows for a quicker drop but still provides a small delay between movements, making the downward movement visually smoother and more controllable.

# This solution allows for both single key presses for precise movement and holding down the key for rapid descent, improving the gameplay experience by giving the player more control over the tetrominoes.

################ User: ############################

# thank you. next iteration: this is a small one. Only after restarting the game, command-q or clicking on the window close button no longer quits the game. please output the entire 'run(self)' block to make sure I get it right, thank you.

################ Iterative Coding: ################

# The issue you're experiencing with quitting the game not working after a restart likely stems from the way the game loop and event handling are structured, especially with how the game restart is implemented. When the game is restarted, the event loop must continue to correctly handle quit events.

# To ensure that quit events (like Command-Q or clicking the window's close button) are correctly handled at all times, including after a game restart, you should structure your game loop to consistently check for quit events, even when outside the main gameplay loop. This can be achieved by placing event checks in any waiting loops and ensuring that the quit event leads to a break out of all loops and subsequently exits the program.

# Here's how you can adjust your game loop to ensure quitting works correctly after restarting:

# ### Revised Approach for Handling Quit Events

# ```python
# def run(self):
#     running = True  # Controls the outermost loop
#     while running:  # This outer loop allows the game to be restarted
#         self.reset_game()  # Reset the game state before starting/restarting the game
#         while not self.is_game_over:
#             current_time = pygame.time.get_ticks()
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False  # Ensures we break out of the outer loop as well
#                     break  # Exit the inner loop
#                 # Handle other events (including KEYDOWN) here
                
#             if not running:  # Check if we need to exit the outer loop
#                 break

#             # Game loop contents (movement, drawing, etc.) go here

#             if self.is_game_over:
#                 self.game_over_screen()  # Display game over screen and wait for input
                
#         # You can handle any cleanup or preparation for a new game here if necessary

#     # If the loop exits, quit Pygame and the program
#     pygame.quit()
# ```

# ### Key Adjustments:

# - **Unified Quit Handling**: By using a `running` variable to control the outer loop and checking for the `pygame.QUIT` event, you ensure that quit events are respected no matter where in the game loop they occur.
# - **Immediate Loop Exit**: When a quit event is detected, the code sets `running` to `False` and breaks out of the current loop. It then checks `running` after exiting the inner loop, allowing for a clean exit out of the outer loop as well.
# - **Pygame Quit**: Calling `pygame.quit()` after the loops ensures that Pygame shuts down properly when the game is closed.

# This structure ensures that quit events are handled consistently throughout the game, including after restarting, making the game more robust and user-friendly by allowing players to exit at any time.

import pygame
import random

# Constants for the game
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Define the shapes of the tetrominoes
TETROMINOES = [
    [[1, 1, 1],
     [0, 1, 0]],
    
    [[0, 2, 2],
     [2, 2, 0]],
    
    [[3, 3, 0],
     [0, 3, 3]],
    
    [[4, 0, 0],
     [4, 4, 4]],
    
    [[0, 0, 5],
     [5, 5, 5]],
    
    [[6, 6, 6, 6]],
    
    [[7, 7],
     [7, 7]]
]

# Colors for the tetrominoes
COLORS = [(0, 255, 255), (255, 165, 0), (0, 0, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0)]

class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = COLORS[TETROMINOES.index(shape)]
        self.rotation = 0  # This might no longer be needed depending on your rotation implementation
        self.x = int(SCREEN_WIDTH / 2 / BLOCK_SIZE) - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        # Transpose the shape matrix
        self.shape = [list(row) for row in zip(*self.shape)]
        # Reverse each row to get a clockwise rotation
        self.shape = [row[::-1] for row in self.shape]

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris Clone')
        self.clock = pygame.time.Clock()
        self.board = [[(0,0,0) for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.drop_speed = 1000  # Milliseconds
        self.last_drop_time = pygame.time.get_ticks()
        self.score = 0
        self.is_game_over = False  # Indicates if the game is in a "game over" state

    def new_piece(self):
        piece = Tetromino(random.choice(TETROMINOES))
        if self.check_collision(piece.shape, (piece.x, piece.y)):
            self.game_over = True  # Game over condition met
            print("Game Over!")  # For debugging; consider showing a message on the screen
        return piece

    def check_collision(self, shape, offset):
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if x + off_x < 0 or x + off_x >= len(self.board[0]) or y + off_y >= len(self.board) or self.board[y + off_y][x + off_x] != (0,0,0):
                        return True
        return False

    def move(self, dx, dy):
        new_x = self.current_piece.x + dx
        new_y = self.current_piece.y + dy
        if not self.check_collision(self.current_piece.shape, (new_x, new_y)):
            self.current_piece.x = new_x
            self.current_piece.y = new_y

    def rotate_piece(self):
        print(self.current_piece.shape)
        original_shape = self.current_piece.shape
        self.current_piece.rotate()
        if self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y)):
            self.current_piece.shape = original_shape  # Revert to the original shape if there's a collision after rotation
        print(self.current_piece.shape)
        
    def lock_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[y + self.current_piece.y][x + self.current_piece.x] = self.current_piece.color
        self.clear_lines()  # Check and clear lines after locking a piece
        self.current_piece = self.new_piece()

    def clear_lines(self):
        new_board = [row for row in self.board if not all(color != (0,0,0) for color in row)]
        lines_cleared = len(self.board) - len(new_board)
        
        # Scoring
        if lines_cleared > 0:
            self.score += self.calculate_score(lines_cleared)
            print(f"Score: {self.score}")  # For debugging, or display this in your game window
        
        for _ in range(lines_cleared):
            new_board.insert(0, [(0,0,0) for _ in range(SCREEN_WIDTH // BLOCK_SIZE)])
        self.board = new_board

    def calculate_score(self, lines_cleared):
        # Define scoring based on lines cleared
        score_dict = {1: 100, 2: 300, 3: 500, 4: 800}
        return score_dict.get(lines_cleared, 0)


    def draw_grid(self):
        for y, row in enumerate(self.board):
            for x, color in enumerate(row):
                if color != (0,0,0):
                    pygame.draw.rect(self.screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_piece(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, piece.color, (x * BLOCK_SIZE + piece.x * BLOCK_SIZE, y * BLOCK_SIZE + piece.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_score(self):
        font = pygame.font.Font(None, 36)  # Adjust font and size as needed
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))  # White color
        self.screen.blit(text, (10, 10))  # Position the score in the top-left corner

    def game_over_screen(self):
        self.screen.fill((0, 0, 0))  # Clear the screen or choose a background color
        font = pygame.font.Font(None, 72)  # Larger font for the game over message
        text = font.render("GAME OVER", True, (255, 255, 255))  # Create the text
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(text, text_rect)  # Display the text

        # Smaller font for the restart message
        restart_font = pygame.font.Font(None, 36)
        restart_text = restart_font.render("Press R to Restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)  # Display the text

        pygame.display.flip()  # Update the screen

        # Wait for the player to press 'R' to restart
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_input = False
                    self.is_game_over = False  # To ensure we exit the game completely
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting_for_input = False
                        self.reset_game()

    def reset_game(self):
        # Reset game state for a new game
        self.board = [[(0,0,0) for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_piece = self.new_piece()
        self.is_game_over = False
        self.score = 0
        # You may want to reset other game state variables here as well

    def run(self):
        while True:  # This outer loop allows for restarting the game
            self.reset_game()  # Reset the game state before starting/restarting the game
            while not self.is_game_over:
                current_time = pygame.time.get_ticks()
                keys = pygame.key.get_pressed()  # Get the state of all keyboard keys

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()  # Ensure pygame is properly quit
                        return  # Exit the entire game function, ending the game
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.move(-1, 0)
                        elif event.key == pygame.K_RIGHT:
                            self.move(1, 0)
                        elif event.key == pygame.K_UP:
                            self.rotate_piece()

                # Continuous downward movement when the DOWN key is held
                if keys[pygame.K_DOWN]:
                    self.move(0, 1)

                # Adjusting the drop speed for continuous movement
                drop_speed_adjusted = self.drop_speed
                if keys[pygame.K_DOWN]:
                    drop_speed_adjusted = max(50, drop_speed_adjusted // 10)  # Adjust drop speed for faster fall

                if current_time - self.last_drop_time > drop_speed_adjusted:
                    if not self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y + 1)):
                        self.move(0, 1)
                    else:
                        self.lock_piece()
                        # Check for game over condition right after locking a piece
                        if self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y)):
                            self.is_game_over = True
                    self.last_drop_time = current_time

                self.screen.fill((0, 0, 0))
                self.draw_grid()
                self.draw_piece(self.current_piece)
                self.draw_score()
                pygame.display.flip()
                self.clock.tick(60)

            # Handle the game over state
            self.game_over_screen()  # Display game over screen

            # Process events after game over to allow for quitting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return


if __name__ == "__main__":
    game = Game()
    game.run()
