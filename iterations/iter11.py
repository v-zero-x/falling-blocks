################ User: ############################

# next iteration: Game Over Screen that displays "GAME OVER" with an option to restart the game.

################ Iterative Coding: ################

# ### Iteration 11: Implementing a Game Over Screen with Restart Option

# To implement a game over screen that displays a "GAME OVER" message and offers an option to restart the game, you'll need to add a new method for handling the game over state and modify your game loop to react accordingly. This involves drawing text on the screen and handling keyboard input to restart the game.

# Here's how to add these features:

# #### Step 1: Implementing the Game Over Screen Method

# ```python
# class Game:
#     def __init__(self):
#         # Initialization code...
#         self.is_game_over = False  # Indicates if the game is in a "game over" state

#     # Other methods...

#     def game_over_screen(self):
#         self.screen.fill((0, 0, 0))  # Clear the screen or choose a background color
#         font = pygame.font.Font(None, 72)  # Larger font for the game over message
#         text = font.render("GAME OVER", True, (255, 255, 255))  # Create the text
#         text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
#         self.screen.blit(text, text_rect)  # Display the text

#         # Smaller font for the restart message
#         restart_font = pygame.font.Font(None, 36)
#         restart_text = restart_font.render("Press R to Restart", True, (255, 255, 255))
#         restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
#         self.screen.blit(restart_text, restart_rect)  # Display the text

#         pygame.display.flip()  # Update the screen

#         # Wait for the player to press 'R' to restart
#         waiting_for_input = True
#         while waiting_for_input:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     waiting_for_input = False
#                     self.is_game_over = False  # To ensure we exit the game completely
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_r:
#                         waiting_for_input = False
#                         self.reset_game()

#     def reset_game(self):
#         # Reset game state for a new game
#         self.board = [[(0,0,0) for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
#         self.current_piece = self.new_piece()
#         self.is_game_over = False
#         self.score = 0
#         # You may want to reset other game state variables here as well

#     def run(self):
#         while True:  # Main game loop now loops indefinitely
#             while not self.is_game_over:
#                 # Game loop logic...
#                 if self.game_over:  # If game_over condition is met within the loop
#                     self.is_game_over = True
#                     self.game_over_screen()

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     return  # Exit the main loop and end the game
# ```

# ### Key Changes:

# - **Game Over State Management**: Introduced `self.is_game_over` to manage the game over state separately from the game loop.
# - **Game Over Screen Display**: The `game_over_screen` method handles displaying the game over message and the restart option. It halts the game loop and waits for the user's input.
# - **Restarting the Game**: Pressing 'R' restarts the game by calling `reset_game`, which resets the game state and starts a new game session.
# - **Infinite Game Loop**: The outer `while True` loop in `run` allows the game to be restarted indefinitely without ending the script.

# ### Enhancing the Game Over Experience:

# - **Animations and Effects**: Consider adding simple animations or effects to the game over screen for visual interest.
# - **High Score Display**: Show the player's score and high score on the game over screen to encourage competition.
# - **Menu Options**: Provide options for quitting or returning to a main menu, if you have one, for better navigation.

# This implementation provides a basic game over screen with a restart option, enhancing the game's usability and replayability. It's a significant step towards a complete game experience, allowing players to easily try to beat their previous scores without restarting the application.

################ User: ############################

# I was able to integrate all of the new code except the changes to 'def run(self)'. Please help me with that integration.

################ Iterative Coding: ################

# Certainly! Let's focus on integrating the changes into the `run` method of your `Game` class to ensure it handles the game loop, game over state, and restart functionality smoothly. The goal is to maintain the game loop when the game is active and display the game over screen with an option to restart when the game ends.

# Given the structure of your existing `run` method and the need to integrate game over handling, here's how you can modify it:

# ### Revised `run` Method with Game Over Integration

# ```python
# class Game:
#     def __init__(self):
#         # Initialization code (unchanged)
#         # Make sure to initialize is_game_over here
#         self.is_game_over = False

#     # Assume other methods including game_over_screen and reset_game are defined here

#     def run(self):
#         while True:  # This outer loop allows the game to be restarted
#             self.reset_game()  # Reset the game state before starting/restarting the game
#             while not self.is_game_over:
#                 # Game loop logic
#                 current_time = pygame.time.get_ticks()
#                 for event in pygame.event.get():
#                     if event.type == pygame.QUIT:
#                         return  # Exit the entire game
#                     if event.type == pygame.KEYDOWN:
#                         if event.key == pygame.K_LEFT:
#                             self.move(-1, 0)
#                         elif event.key == pygame.K_RIGHT:
#                             self.move(1, 0)
#                         elif event.key == pygame.K_DOWN:
#                             self.move(0, 1)
#                         elif event.key == pygame.K_UP:
#                             self.rotate_piece()

#                 if current_time - self.last_drop_time > self.drop_speed:
#                     if not self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y + 1)):
#                         self.move(0, 1)
#                     else:
#                         self.lock_piece()
#                         # Check for game over condition right after locking a piece
#                         if self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y)):
#                             self.is_game_over = True
#                     self.last_drop_time = current_time

#                 self.screen.fill((0, 0, 0))
#                 self.draw_grid()
#                 self.draw_piece(self.current_piece)
#                 self.draw_score()
#                 pygame.display.flip()
#                 self.clock.tick(60)

#                 if self.is_game_over:
#                     self.game_over_screen()  # Display game over screen

#             # Outside the inner while loop but inside the outer loop
#             # This is where you could handle any cleanup or setup between games if needed
# ```

# ### Key Integration Points:

# 1. **Resetting the Game**: At the beginning of the outer loop, `reset_game()` is called to ensure the game starts in a clean state, useful for both initial starts and restarts after a game over.

# 2. **Game Loop**: The inner `while not self.is_game_over` loop contains the main game logic that runs while the game is active.

# 3. **Game Over Check**: Inside this loop, after locking a piece, you check if placing the new piece would result in a collision (indicative of a game over condition). If so, `self.is_game_over` is set to `True`.

# 4. **Game Over Screen**: Once `self.is_game_over` is `True`, the `game_over_screen()` method is called to display the game over message and handle restarts. Because `game_over_screen()` halts execution until the player decides to restart or quit, no additional code is needed outside of this call to pause the game.

# 5. **Continual Restart**: The outer `while True` loop ensures that once the game over screen concludes, either the game resets for another round or the application exits based on player input.

# This approach ensures that the game can seamlessly transition between playing, game over, and restarting states, providing a cohesive gameplay experience.


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
        while True:  # This outer loop allows the game to be restarted
            self.reset_game()  # Reset the game state before starting/restarting the game
            while not self.is_game_over:
                # Game loop logic
                current_time = pygame.time.get_ticks()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return  # Exit the entire game
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.move(-1, 0)
                        elif event.key == pygame.K_RIGHT:
                            self.move(1, 0)
                        elif event.key == pygame.K_DOWN:
                            self.move(0, 1)
                        elif event.key == pygame.K_UP:
                            self.rotate_piece()

                if current_time - self.last_drop_time > self.drop_speed:
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

                if self.is_game_over:
                    self.game_over_screen()  # Display game over screen

            # Outside the inner while loop but inside the outer loop
            # This is where you could handle any cleanup or setup between games if needed


if __name__ == "__main__":
    game = Game()
    game.run()
