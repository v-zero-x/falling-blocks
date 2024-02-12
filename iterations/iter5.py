################ User: ############################

# next iteration: the collision check on the right side of the board works, but tetronimos can move past the left side of the board. maybe check tetronimo width and update collision checks?

################ User: ############################

# ### Iteration 5: Improving Collision Checks for Left Boundary

# To address the issue with tetrominoes moving past the left side of the board, we need to refine our collision check logic. We'll ensure that the collision detection accounts for the entire width of the tetromino, including checking against the left boundary of the board. This involves updating the `check_collision` method to accurately determine if a tetromino's position after a move would result in an out-of-bounds situation or overlap with existing pieces on the board.

# Let's incorporate these adjustments into our code:

# ```python
# import pygame
# import random

# # Constants for the game
# SCREEN_WIDTH = 300
# SCREEN_HEIGHT = 600
# BLOCK_SIZE = 30

# # Define the shapes of the tetrominoes
# TETROMINOES = [
#     [[1, 1, 1],
#      [0, 1, 0]],
    
#     [[0, 2, 2],
#      [2, 2, 0]],
    
#     [[3, 3, 0],
#      [0, 3, 3]],
    
#     [[4, 0, 0],
#      [4, 4, 4]],
    
#     [[0, 0, 5],
#      [5, 5, 5]],
    
#     [[6, 6, 6, 6]],
    
#     [[7, 7],
#      [7, 7]]
# ]

# # Colors for the tetrominoes
# COLORS = [(0, 255, 255), (255, 165, 0), (0, 0, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0)]

# class Tetromino:
#     def __init__(self, shape):
#         self.shape = shape
#         self.color = COLORS[TETROMINOES.index(shape)]
#         self.rotation = 0
#         self.x = int(SCREEN_WIDTH / 2 / BLOCK_SIZE) - len(shape[0]) // 2
#         self.y = 0

#     def rotate(self):
#         self.rotation = (self.rotation + 1) % len(self.shape)

# class Game:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#         pygame.display.set_caption('Tetris Clone')
#         self.clock = pygame.time.Clock()
#         self.board = [[0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
#         self.current_piece = self.new_piece()
#         self.game_over = False
#         self.drop_speed = 1000  # Milliseconds
#         self.last_drop_time = pygame.time.get_ticks()

#     def new_piece(self):
#         return Tetromino(random.choice(TETROMINOES))

#     def check_collision(self, shape, offset):
#         off_x, off_y = offset
#         for y, row in enumerate(shape):
#             for x, cell in enumerate(row):
#                 if cell:
#                     if x + off_x < 0 or x + off_x >= len(self.board[0]) or y + off_y >= len(self.board):
#                         return True
#                     if self.board[y + off_y][x + off_x]:
#                         return True
#         return False

#     def move(self, dx, dy):
#         new_x = self.current_piece.x + dx
#         new_y = self.current_piece.y + dy
#         if not self.check_collision(self.current_piece.shape, (new_x, new_y)):
#             self.current_piece.x = new_x
#             self.current_piece.y = new_y

#     def rotate_piece(self):
#         self.current_piece.rotate()
#         if self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y)):
#             self.current_piece.rotate()  # Rotate back if there's a collision

#     def lock_piece(self):
#         for y, row in enumerate(self.current_piece.shape):
#             for x, cell in enumerate(row):
#                 if cell:
#                     self.board[y + self.current_piece.y][x + self.current_piece.x] = self.current_piece.color
#         self.current_piece = self.new_piece()

#     def draw_piece(self, piece):
#         for y, row in enumerate(piece.shape):
#             for x, cell in enumerate(row):
#                 if cell:
#                     pygame.draw.rect(self.screen, piece.color, (x * BLOCK_SIZE + piece.x * BLOCK_SIZE, y * BLOCK_SIZE + piece.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

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
#             self.draw_piece(self.current_piece)
#             pygame.display.flip()
#             self.clock.tick(60)

# if __name__ == "__main__":
#     game = Game()
#     game.run()
# ```

# This iteration refines the `check_collision` function to prevent tetrominoes from moving past the left side of the board. The updated logic checks if any part of the tetromino is outside the board's left boundary or collides with existing pieces on the board, ensuring a more robust and accurate collision detection mechanism.

# This adjustment ensures that tetrominoes cannot move beyond the game board's left edge, addressing the issue from the previous iteration.



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
        self.rotation = 0
        self.x = int(SCREEN_WIDTH / 2 / BLOCK_SIZE) - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris Clone')
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
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
                    if x + off_x < 0 or x + off_x >= len(self.board[0]) or y + off_y >= len(self.board):
                        return True
                    if self.board[y + off_y][x + off_x]:
                        return True
        return False

    def move(self, dx, dy):
        new_x = self.current_piece.x + dx
        new_y = self.current_piece.y + dy
        if not self.check_collision(self.current_piece.shape, (new_x, new_y)):
            self.current_piece.x = new_x
            self.current_piece.y = new_y

    def rotate_piece(self):
        self.current_piece.rotate()
        if self.check_collision(self.current_piece.shape, (self.current_piece.x, self.current_piece.y)):
            self.current_piece.rotate()  # Rotate back if there's a collision

    def lock_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[y + self.current_piece.y][x + self.current_piece.x] = self.current_piece.color
        self.current_piece = self.new_piece()

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
            self.draw_piece(self.current_piece)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
