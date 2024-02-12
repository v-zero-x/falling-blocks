# User: next iteration: let's discuss piece rotation. when I test the game, this is the first piece that appears:
#     [[4, 0, 0],
#      [4, 4, 4]],

# when i press the UP arrow. this is the before and after rotation of the piece:
# before: [[4, 0, 0], [4, 4, 4]]
# after: [[4, 0, 0], [4, 4, 4]]

# the piece does not appear to rotate.

# here is the code that rotates the piece:
#     def rotate_piece(self):
#         print(self.current_piece.shape)
#         self.current_piece.rotate()
#         print(self.current_piece.shape)

#         if self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y)):
#             self.current_piece.rotate()  # Rotate back if there's a collision

# Iterative Coding:

# The issue with the rotation not appearing to change the piece's shape is due to the `rotate` method in the `Tetromino` class not actually modifying the shape of the tetromino. It only increments the `rotation` attribute without changing the tetromino's structure. For tetromino rotation, you generally need to transform the shape matrix.

# A common approach to rotate a tetromino (or any matrix) is to transpose the matrix and then reverse each row for a clockwise rotation. Let's implement this logic into the rotation functionality:

# ### Iteration 7: Implementing Tetromino Rotation

# We'll update the `Tetromino` class to properly handle the rotation of the tetromino shape. This involves modifying the `rotate` method to perform the matrix transformation described above.

# ```python
# class Tetromino:
#     def __init__(self, shape):
#         self.shape = shape
#         self.color = COLORS[TETROMINOES.index(shape)]
#         self.rotation = 0  # This might no longer be needed depending on your rotation implementation
#         self.x = int(SCREEN_WIDTH / 2 / BLOCK_SIZE) - len(shape[0]) // 2
#         self.y = 0

#     def rotate(self):
#         # Transpose the shape matrix
#         self.shape = [list(row) for row in zip(*self.shape)]
#         # Reverse each row to get a clockwise rotation
#         self.shape = [row[::-1] for row in self.shape]

# # Update to Game class's rotate_piece method
# class Game:
#     # Other parts of the class remain unchanged
    
#     def rotate_piece(self):
#         print(self.current_piece.shape)
#         original_shape = self.current_piece.shape
#         self.current_piece.rotate()
#         if self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y)):
#             self.current_piece.shape = original_shape  # Revert to the original shape if there's a collision after rotation
#         print(self.current_piece.shape)
# ```

# This implementation changes the `rotate` method in the `Tetromino` class to actually rotate the piece's shape. When the `rotate_piece` method of the `Game` class is called, it attempts to rotate the current piece. If a collision is detected post-rotation (indicating the rotated piece would overlap with the board boundaries or other locked pieces), the rotation is reverted to avoid the collision.

# This approach simplifies the rotation logic by directly modifying the piece's shape, eliminating the need for a separate `rotation` state variable unless you specifically need it for other functionalities (like tracking the number of rotations).

# Remember, this rotation strategy works well for most tetromino shapes, but the "I" tetromino (a straight line) and the "O" tetromino (a square) may require special handling to rotate correctly within the game grid, due to their unique bounding boxes. You might need to adjust their positions slightly after rotation to ensure they remain within the game boundaries.

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
        self.current_piece = self.new_piece()

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
