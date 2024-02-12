################ User: ############################

# the Game class was missing the 'score' attribute so I added it:
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
#         self.score = 0 # added score and tested the Scoring System. it works!

#         # Other methods remain unchanged...

################ Iterative Coding: ################

# Fantastic! Adding the `score` attribute to the `Game` class and successfully integrating the scoring system marks significant progress in developing your Tetris clone. With the scoring system working, players now have a clear goal to aim for, enhancing the game's competitiveness and replay value.

# ### Review and Next Steps

# With the core mechanics, line clearing, and scoring system in place, your Tetris clone has taken shape nicely. Here are a few more aspects you might consider adding or refining to further polish your game:

# 1. **Level Progression**: Introduce levels that increase in difficulty (e.g., by increasing the drop speed) after a certain number of lines have been cleared or points have been scored.
   
# 2. **Next Piece Preview**: Show the next tetromino outside the main game board so players can plan their strategy.
   
# 3. **Game Over Detection**: Implement logic to detect when the game board is filled to the point that no new pieces can be placed, signaling game over.
   
# 4. **Pause and Resume**: Allow players to pause the game and resume it, adding controls for a more user-friendly experience.
   
# 5. **High Score Tracking**: Keep track of high scores, either locally using files or through an online database, to add a competitive edge.
   
# 6. **Sound Effects and Music**: Enhance the game atmosphere with sound effects (e.g., for line clears, tetromino rotation, game over) and background music.
   
# 7. **User Interface Enhancements**: Improve the game's visual appeal with a more sophisticated user interface, animations for line clears, and transitions.

# 8. **Configurable Controls**: Allow players to customize their keyboard controls, accommodating different preferences.

# ### Testing and Refinement

# - **Playtest**: Continuously playtest your game to identify any bugs or areas for improvement. User feedback can be invaluable here.
# - **Performance Optimization**: Ensure your game runs smoothly across different devices by optimizing performance where necessary.
# - **Code Refinement**: Refactor your code to improve readability, maintainability, and performance. Look for opportunities to apply design patterns and best practices.

# You've done a great job implementing the essential features of Tetris. Each new feature or refinement now will only make your game more engaging and enjoyable for players. If you have specific features in mind or need further assistance with any aspect of your game development journey, feel free to ask!

################ User: ############################

# next iteration: Game Over Detection

# ### Iteration 10: Implementing Game Over Detection

# Game over occurs in Tetris when a new piece cannot be placed at the top of the board without overlapping existing blocks. To implement game over detection, you need to check if the position where the new piece spawns is already occupied. This check should be performed right after a new piece is created and before it's added to the board.

# Let's add game over detection to your Tetris clone:

# ```python
# class Game:
#     def __init__(self):
#         # Initialization code (unchanged)
#         self.score = 0  # Ensure score is initialized here
#         # Other initializations...

#     # Other methods...

#     def new_piece(self):
#         piece = Tetromino(random.choice(TETROMINOES))
#         if self.check_collision(piece.shape, (piece.x, piece.y)):
#             self.game_over = True  # Game over condition met
#             print("Game Over!")  # For debugging; consider showing a message on the screen
#         return piece

#     def run(self):
#         while not self.game_over:
#             current_time = pygame.time.get_ticks()
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.game_over = True
#                 # Handling other events...

#             # Game loop logic...

#             self.screen.fill((0, 0, 0))
#             # Drawing the game state...
#             self.draw_grid()
#             self.draw_piece(self.current_piece)
#             self.draw_score()  # Make sure this method is defined to draw the score
#             pygame.display.flip()
#             self.clock.tick(60)

#         # After exiting the game loop, you can add logic to display the final score,
#         # ask the player if they want to play again, etc.

# # Make sure all other methods like draw_score are implemented as previously discussed.
# ```

# ### Key Points:

# - **Game Over Check**: The check is performed in `new_piece` by seeing if the new piece's starting position collides with existing blocks on the board. If there's a collision, it sets `self.game_over` to `True`.
# - **Handling Game Over**: Once `self.game_over` is set to `True`, the game loop will exit. You can then display a game over message to the player, show the final score, and potentially offer options to restart the game or exit.
# - **Displaying Messages**: While the print statement is used here for simplicity, consider using Pygame's text rendering capabilities to display game over messages and scores on the game window for a more integrated user experience.

# ### Enhancing User Experience:

# - **Game Over Screen**: Create a dedicated game over screen with options for the player to restart the game or quit.
# - **Transition Effects**: Adding simple effects or transitions when the game ends can make the experience feel more polished.
# - **Score Display**: Ensure the final score is prominently displayed on the game over screen, encouraging players to beat their high score in future games.

# Implementing game over detection is crucial for completing the game loop and providing a clear end-point to the game. It sets the stage for adding more advanced features, like high score tracking and player options post-game over, enhancing replayability and engagement.


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

#     def run(self):
#         while not self.game_over:
#             current_time = pygame.time.get_ticks()
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.game_over = True
#                 # Handling other events...

#             # Game loop logic...

#             self.screen.fill((0, 0, 0))
#             # Drawing the game state...
#             self.draw_grid()
#             self.draw_piece(self.current_piece)
#             self.draw_score()  # Make sure this method is defined to draw the score
#             pygame.display.flip()
#             self.clock.tick(60)

#         # After exiting the game loop, you can add logic to display the final score,
#         # ask the player if they want to play again, etc.

# # Make sure all other methods like draw_score are implemented as previously discussed.


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

    def run(self):
        while not self.game_over:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                # Handling other events...

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
