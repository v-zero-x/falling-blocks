# Falling Blocks

<figure>
  <img src="falling_blocks.png" alt="Falling Blocks">
  <figcaption>Falling Blocks</figcaption>
</figure>


This project is an re-imagination of the classic Tetris® game, developed in Python using the Pygame library. It features core gameplay mechanics such as tetromino falling, rotation, line clearing, and a scoring system. The game ends when the tetrominos stack up to the top of the playing field, with an option to restart once the game is over.

This project was built using the ["Iterative Coding" GPT](https://chat.openai.com/g/g-ZfQ1k76Cv-iterative-coding) developed by vzerox.com to test and demonstrate ChatGPT's ability to generate simple, complete applications and scripts by using an iterative process. This README was also AI-generated with only minor edits made to the initial document.

## Project Description

Falling Blocks was developed iteratively in a human-AI collaboration, utilizing the capabilities of an AI to refine game mechanics, add new features, and ensure a smooth gameplay experience. Each iteration focused on a specific aspect of the game, starting from basic setup to implementing game over logic and a restart feature.

## Installation

To play the Falling Blocks, you'll need Python and Pygame installed on your system.

### Requirements:
- Python 3.11.x
- Pygame

### Installing Pygame

Pygame can be installed via pip. In your terminal or command prompt, run:

```
pip install pygame
```

### Running the Game

To start the game, navigate to the project directory and run:

```
python main.py
```

## How to Play

- **Arrow Left/Right**: Move the tetromino left or right.
- **Arrow Up**: Rotate the tetromino.
- **Arrow Down**: Speed up the tetromino's fall.

The goal is to clear as many lines as possible by completing horizontal lines of blocks without any gaps. The game ends when the blocks reach the top of the board.

## Development Process

The game was developed through a series of iterations, each focusing on adding or refining features. The development was a collaborative effort between a human and an AI, leveraging the AI's ability to generate code and solve programming challenges.

### Iterative Development Overview:

- **Initial Setup (`initial_iterations.py`)**: Establishing the game board, basic tetromino shapes, and movement.
- **Iteration 4 (`iter4.py`)**: Adding game speed control and FPS adjustments.
- **Iteration 5 (`iter5.py`)**: Enhancing collision detection for improved game mechanics.
- **Further Iterations (`iter6.py`, `iter7.py`, etc.)**: Implementing line clearing, scoring, game over detection, and a restart feature.

## Collaborative Human-AI Development

This project showcases the potential of human-AI collaboration in software development. By iteratively refining the game based on AI-generated suggestions and code, we were able to create a feature-complete simple game. This process highlights how AI can assist in problem-solving and creative thinking, contributing to the development of complex projects.

## Files and Iterations

- **[Initial Iterations](iterations/initial_iterations.py)**: The foundation of the game.
- **[Iteration 4](iterations/iter4.py)**: Game speed and FPS adjustments.
- **[Iteration 5](iterations/iter5.py)**: Collision detection improvements.
- **[Further Iterations](iterations/)**: Subsequent files adding additional features.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Trademark Acknowledgement

Tetris® is a trademark of The Tetris Company, LLC. This project is an instructional and research-based endeavor, aimed at demonstrating the application of AI in building simple games, and is not endorsed by, directly affiliated with, or sponsored by The Tetris Company, LLC. The use of the "Tetris" name is for descriptive purposes only and not for profit.
