################ User: ############################

# next iteration: Scoring System

################ Iterative Coding: ################

### Iteration 9: Implementing a Scoring System

# To implement a scoring system in Tetris, we'll need to track the number of lines cleared at once and award points based on this count. The typical scoring rule is to give more points for clearing multiple lines in a single move. Here's a simple way to integrate a scoring system:

# 1. **Single line**: 100 points
# 2. **Double lines**: 300 points
# 3. **Triple lines**: 500 points
# 4. **Tetris (four lines)**: 800 points

# Let's add a scoring system to the game:

# ```python
# class Game:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#         pygame.display.set_caption('Tetris Clone')
#         self.clock = pygame.time.Clock()
#         self.board = [[(0,0,0) for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
#         self.current_piece = self.new_piece()
#         self.game_over = False
#         self.drop_speed = 1000  # Milliseconds
#         self.last_drop_time = pygame.time.get_ticks()
#         self.score = 0  # Initialize score

#     def new_piece(self):
#         return Tetromino(random.choice(TETROMINOES))

#     # Other methods remain unchanged...

#     def clear_lines(self):
#         new_board = [row for row in self.board if not all(color != (0,0,0) for color in row)]
#         lines_cleared = len(self.board) - len(new_board)
        
#         # Scoring
#         if lines_cleared > 0:
#             self.score += self.calculate_score(lines_cleared)
#             print(f"Score: {self.score}")  # For debugging, or display this in your game window
        
#         for _ in range(lines_cleared):
#             new_board.insert(0, [(0,0,0) for _ in range(SCREEN_WIDTH // BLOCK_SIZE)])
#         self.board = new_board

#     def calculate_score(self, lines_cleared):
#         # Define scoring based on lines cleared
#         score_dict = {1: 100, 2: 300, 3: 500, 4: 800}
#         return score_dict.get(lines_cleared, 0)

#     # Drawing methods and game loop remain unchanged...
# ```

# ### Explanation:

# - **Score Tracking**: A new attribute `self.score` is added to the `Game` class to keep track of the player's score.
# - **Calculating Score**: The `calculate_score` method determines the points awarded based on the number of lines cleared at once. This method uses a dictionary to map the number of lines to their corresponding score.
# - **Updating Score**: When lines are cleared (`clear_lines` method), the score is updated based on the number of lines cleared. The new score is printed out or could be displayed on the game window.

# ### Displaying the Score:

# To display the score on the game window, you can draw text on the Pygame window. Here's an example of how you might add a method to `Game` for drawing the score:

# ```python
# def draw_score(self):
#     font = pygame.font.Font(None, 36)  # Adjust font and size as needed
#     text = font.render(f"Score: {self.score}", True, (255, 255, 255))  # White color
#     self.screen.blit(text, (10, 10))  # Position the score in the top-left corner
# ```

# Remember to call `draw_score` within your game loop, after filling the screen with the background color and before updating the display with `pygame.display.flip()`.

# This iteration adds a basic scoring mechanism, rewarding players for clearing multiple lines at once and enhancing the game's competitive aspect.

## User:

# i added the new methods in the locations you recommended. please indicate how to integrate scoring system into the game loop.

## Iterative Coding

# To integrate the scoring system into your game loop effectively, you need to ensure that the score is updated and displayed on the screen continuously as the game progresses. Following the modifications and additions I've outlined, here's how you can update your game loop to include the scoring display:

# 1. **Update Score**: The score is automatically updated in the `clear_lines` method whenever lines are cleared. So, you don't need to add any additional score updates in the game loop; this is handled during the line-clearing process.

# 2. **Display Score**: To display the score, you should call the `draw_score` method within your game loop, after all game elements have been drawn but before `pygame.display.flip()` to ensure the score is visible on top of everything else.

# Here is how you can integrate the `draw_score` method into your game loop:

# ```python
# class Game:
#     def __init__(self):
#         # Initialization code (unchanged)

#     # Other methods (unchanged)

#     def draw_score(self):
#         font = pygame.font.Font(None, 36)  # Adjust font and size as needed
#         text = font.render(f"Score: {self.score}", True, (255, 255, 255))  # White color
#         self.screen.blit(text, (10, 10))  # Position the score in the top-left corner

#     def run(self):
#         while not self.game_over:
#             current_time = pygame.time.get_ticks()
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.game_over = True
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_LEFT:
#                         self.move(-1, 0)
#                     elif event.key == pygame.K_RIGHT:
#                         self.move(1, 0)
#                     elif event.key == pygame.K_DOWN:
#                         self.move(0, 1)
#                     elif event.key == pygame.K_UP:
#                         self.rotate_piece()

#             if current_time - self.last_drop_time > self.drop_speed:
#                 if not self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y + 1)):
#                     self.move(0, 1)
#                 else:
#                     self.lock_piece()
#                 self.last_drop_time = current_time

#             self.screen.fill((0, 0, 0))
#             # Draw the game state (tetrominoes, grid, etc.)
#             self.draw_grid()
#             self.draw_piece(self.current_piece)
#             self.draw_score()  # Draw the current score
#             pygame.display.flip()
#             self.clock.tick(60)
# ```

# ### Key Integration Points:

# - **After Drawing the Game State**: Make sure to call `self.draw_score()` after all other drawing calls (e.g., drawing the grid, current piece) to ensure the score text appears on top of the game elements and is not obscured.
# - **Before `pygame.display.flip()`**: Updating the display with `pygame.display.flip()` should be the last step after all drawing operations, including drawing the score, have been completed.

# This integration ensures that the score is continuously updated and displayed as part of the game loop, allowing players to see their progress in real-time. By incorporating the scoring system in this manner, you enhance the gameplay experience by adding a competitive element and providing players with immediate feedback on their performance.

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

    def new_piece(self):
        return Tetromino(random.choice(TETROMINOES))

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

    def run(self):
        while not self.game_over:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
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
                self.last_drop_time = current_time

            self.screen.fill((0, 0, 0))
            # Draw the game state (tetrominoes, grid, etc.)
            self.draw_grid()
            self.draw_piece(self.current_piece)
            self.draw_score()  # Draw the current score
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
