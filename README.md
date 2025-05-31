# Pygame-x-and-o

A simple implementation of a Tic-Tac-Toe ("X and O") game using [Pygame](https://www.pygame.org/). This project serves as an educational example of building a graphical board game in Python with Pygame.

## Features

- Classic Tic-Tac-Toe gameplay on a 3x3 grid
- "X" always goes first
- Click-based interface to place Xs and Os
- Detects wins and draws

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/TheSebitzu/Pygame-x-and-o.git
   cd Pygame-x-and-o
   ```

2. **Install dependencies:**
   ```sh
   pip install pygame
   ```

## Usage

Start the game with:
```sh
python main.py
```

- Play by clicking on the grid to place Xs and Os.
- The game automatically announces the winner or a draw.

## How It Works

- The game window is created using Pygame and displays a 3x3 grid.
- Players take turns clicking empty cells to place their symbol (X or O), with "X" always starting first.
- After each move, the game checks the board for a win or draw.
- When the game ends, a message is displayed announcing the outcome.

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/)

## License

This project is licensed under the MIT License.

---

*Made by [TheSebitzu](https://github.com/TheSebitzu)*
