################ User: ############################

# the game iterations are going well. the pieces now fall, rotate, remain on the board once locked, and respect boundaries correctly.

################ Iterative Coding: ################

# I'm glad to hear the game iterations are going well! With the core mechanics like piece falling, rotation, boundary respect, and locking in place now working correctly, you have a solid foundation for a Tetris game. 

# ### Next Steps to Consider

# To further develop your Tetris clone, here are some additional features and refinements you might consider adding:

# 1. **Line Clearing**: Implement logic to detect when a line is fully occupied by blocks and should be cleared. This involves checking each row of the game board for completeness, removing any complete lines, and shifting down the blocks above the cleared line.

# 2. **Scoring System**: Introduce a scoring system where points are awarded for clearing lines. The scoring could increase for clearing multiple lines at once (e.g., a Tetris, which is clearing four lines simultaneously).

# 3. **Leveling Up**: Increase the game's difficulty as the player scores more points or clears more lines. Typically, this means increasing the falling speed of the tetrominoes.

# 4. **Next Piece Preview**: Show the player a preview of the next piece to come. This helps players plan their placement strategy in advance.

# 5. **Game Over Detection**: Implement logic to detect a game over condition, typically when a new piece cannot be placed on the game board without overlapping existing blocks.

# 6. **Rotation Improvements**: For a more polished rotation feature, consider implementing wall kicks. This is a feature that allows pieces to rotate in tight spaces by slightly shifting them away from walls or other blocks if a direct rotation is not possible.

# 7. **Sound Effects and Music**: Adding sound effects for line clears, tetromino rotation, and drops, as well as background music, can greatly enhance the game experience.

# 8. **Graphical User Interface Enhancements**: Improve the visual appeal of the game with more sophisticated graphics for the game board, tetrominoes, and background. Adding animations for line clears and tetromino drops can also make the game more engaging.

# 9. **Pause/Restart Options**: Allow players to pause the game and resume it, or restart the game after a game over.

# 10. **High Score Tracking**: Keep track of high scores locally or even online, so players can see their progress and compete with others.

# Each of these features introduces new challenges and learning opportunities, especially in areas like game logic, state management, and graphical rendering. Prioritize based on what you think will most enhance the gameplay experience and your own learning goals.

# If you need further assistance implementing any of these features or have more questions as you continue developing your Tetris clone, feel free to ask!

################ User: ############################


# next iteration: Line Clearing. Note that each complete row should be removed and remaining rows should be dropped to fill the space of the cleared rows.

################ Iterative Coding: ################

# ### Iteration 8: Implementing Line Clearing

# To implement line clearing, we need to add logic that iterates through the board's rows, checks for completeness, removes any complete rows, and then shifts all above rows down to fill the cleared spaces. This functionality is crucial for the core gameplay of Tetris.

# Let's integrate line clearing into the game:

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

#     def new_piece(self):
#         return Tetromino(random.choice(TETROMINOES))

#     # Other methods remain unchanged...

#     def lock_piece(self):
#         for y, row in enumerate(self.current_piece.shape):
#             for x, cell in enumerate(row):
#                 if cell:
#                     self.board[y + self.current_piece.y][x + self.current_piece.x] = self.current_piece.color
#         self.clear_lines()  # Check and clear lines after locking a piece
#         self.current_piece = self.new_piece()

#     def clear_lines(self):
#         # Create a new board without the complete lines
#         new_board = [row for row in self.board if not all(color != (0,0,0) for color in row)]
#         # Calculate how many lines were cleared
#         lines_cleared = len(self.board) - len(new_board)
#         # Add empty lines at the top of the board to replace the cleared lines
#         for _ in range(lines_cleared):
#             new_board.insert(0, [(0,0,0) for _ in range(SCREEN_WIDTH // BLOCK_SIZE)])
#         self.board = new_board

#     # Drawing methods and game loop remain unchanged...
# ```

# ### Explanation:

# 1. **Locking and Clearing**: When a piece is locked into place (`lock_piece` method), we immediately check for and clear any complete lines with `clear_lines`.

# 2. **Clear Lines Logic**: The `clear_lines` method iterates through the board to find complete rows. A row is considered complete if all its cells are filled (none are the default color `(0,0,0)`). We create a new board that excludes these complete rows. The difference in length between the old and new boards tells us how many lines were cleared.

# 3. **Adding Empty Rows**: For each cleared line, we add an empty row at the top of the board. This effectively drops the remaining rows down to fill the space left by the cleared rows.

# 4. **Game Continuation**: After clearing lines and adjusting the board, the game continues with a new piece.

# This iteration introduces the ability to clear lines and compact the board accordingly, which is a fundamental aspect of Tetris gameplay. With line clearing implemented, players can now work towards clearing multiple rows to prevent the board from filling up too quickly.

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
        # Create a new board without the complete lines
        new_board = [row for row in self.board if not all(color != (0,0,0) for color in row)]
        # Calculate how many lines were cleared
        lines_cleared = len(self.board) - len(new_board)
        # Add empty lines at the top of the board to replace the cleared lines
        for _ in range(lines_cleared):
            new_board.insert(0, [(0,0,0) for _ in range(SCREEN_WIDTH // BLOCK_SIZE)])
        self.board = new_board

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
            self.draw_grid()  # Draw the locked pieces on the board
            self.draw_piece(self.current_piece)  # Draw the current moving piece
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
