################ User: ############################

# next iteration [which number is this?]: gradually increase the speed at which the pieces drop over time, and therefore the difficulty of the game.

################ Iterative Coding: ################

# This next iteration will be focused on gradually increasing the speed at which the pieces drop over time, effectively increasing the game's difficulty as the player progresses. This mechanic encourages players to improve their skills over time and keeps the gameplay challenging and engaging.

# ### Iteration 12: Increasing Drop Speed Over Time

# To implement this feature, you can adjust the drop speed based on the player's score or the number of lines cleared. A simple approach is to decrease the `self.drop_speed` value as the player reaches certain score thresholds or clears a certain number of lines. Here's how you could modify your `run` method and other relevant parts of your `Game` class:

# ```python
# class Game:
#     def __init__(self):
#         # Initialization code...
#         self.score = 0
#         self.lines_cleared = 0  # Track the total number of lines cleared
#         self.drop_speed = 1000  # Initial drop speed in milliseconds
#         self.is_game_over = False

#     # Other methods...

#     def clear_lines(self):
#         new_board = [row for row in self.board if not all(color != (0,0,0) for color in row)]
#         lines_cleared_now = len(self.board) - len(new_board)
        
#         if lines_cleared_now > 0:
#             self.lines_cleared += lines_cleared_now  # Update total lines cleared
#             self.score += self.calculate_score(lines_cleared_now)
#             print(f"Score: {self.score}")  # Debugging or display in-game
#             self.adjust_drop_speed()  # Adjust drop speed based on lines cleared
        
#         for _ in range(lines_cleared_now):
#             new_board.insert(0, [(0,0,0) for _ in range(SCREEN_WIDTH // BLOCK_SIZE)])
#         self.board = new_board

#     def adjust_drop_speed(self):
#         # Example: Decrease drop speed every 10 lines cleared
#         if self.lines_cleared % 10 == 0:
#             self.drop_speed = max(100, self.drop_speed - 50)  # Prevent drop speed from becoming too fast

#     def run(self):
#         while True:  # Outer loop for restarting the game
#             self.reset_game()  # Reset the game state
#             while not self.is_game_over:
#                 current_time = pygame.time.get_ticks()
#                 keys = pygame.key.get_pressed()

#                 # Event handling...

#                 if keys[pygame.K_DOWN]:
#                     self.move(0, 1)

#                 drop_speed_adjusted = self.drop_speed
#                 if keys[pygame.K_DOWN]:
#                     drop_speed_adjusted = max(50, drop_speed_adjusted // 10)  # Faster fall on DOWN key

#                 if current_time - self.last_drop_time > drop_speed_adjusted:
#                     # Movement and locking logic...
#                     self.last_drop_time = current_time

#                 # Drawing the game state...

#             # Game over logic...

#         # After game over logic...
# ```

# ### Key Features of This Iteration:

# - **Lines Cleared Tracking**: Introduce a variable (`self.lines_cleared`) to keep track of the total number of lines the player has cleared throughout the game.
# - **Adjusting Drop Speed**: Implement an `adjust_drop_speed` method that decreases the `self.drop_speed` as the player clears more lines. This method is called every time lines are cleared.
# - **Difficulty Progression**: By reducing the drop speed (making pieces fall faster) at certain milestones (e.g., every 10 lines cleared), the game becomes progressively more challenging.

# This approach allows the game's difficulty to scale with the player's skill level, providing a balanced and engaging gameplay experience. Feel free to adjust the scaling of the drop speed and the milestones based on testing and player feedback to find the right level of challenge.


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
        self.lines_cleared = 0  # Track the total number of lines cleared
        self.drop_speed = 1000  # Initial drop speed in milliseconds
        self.is_game_over = False

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

    def clear_lines(self):
        new_board = [row for row in self.board if not all(color != (0,0,0) for color in row)]
        lines_cleared_now = len(self.board) - len(new_board)
        
        if lines_cleared_now > 0:
            self.lines_cleared += lines_cleared_now  # Update total lines cleared
            self.score += self.calculate_score(lines_cleared_now)
            print(f"Score: {self.score}")  # Debugging or display in-game
            self.adjust_drop_speed()  # Adjust drop speed based on lines cleared
        
        for _ in range(lines_cleared_now):
            new_board.insert(0, [(0,0,0) for _ in range(SCREEN_WIDTH // BLOCK_SIZE)])
        self.board = new_board

    def adjust_drop_speed(self):
        # Example: Decrease drop speed every 10 lines cleared
        if self.lines_cleared % 10 == 0:
            self.drop_speed = max(100, self.drop_speed - 50)  # Prevent drop speed from becoming too fast

    def run(self):
        while True:  # Outer loop for restarting the game
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
                        else:
                            # Line clearing and possibly adjusting drop speed due to game progression
                            self.clear_lines()
                    self.last_drop_time = current_time

                self.screen.fill((0, 0, 0))
                self.draw_grid()
                self.draw_piece(self.current_piece)
                self.draw_score()  # Make sure this method is defined to draw the score
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



