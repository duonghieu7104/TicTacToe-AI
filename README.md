# Tic Tac Toe AI with Negamax Algorithm

## Overview

This project implements a Tic Tac Toe game where an AI uses the **Negamax** algorithm to determine the best move. The Negamax algorithm is a variant of Minimax, commonly used in two-player zero-sum games. In this game, the AI intelligently evaluates possible game states to make optimal moves.

## Negamax Algorithm

The Negamax algorithm is a simplified version of Minimax, exploiting the zero-sum nature of two-player games. It computes the best move for both players using a single evaluation function, reducing the complexity of handling distinct evaluations for the player and the opponent. In this implementation, the AI uses Negamax along with **alpha-beta pruning** to optimize the search and limit unnecessary computations.

### Applications of Negamax

Negamax is widely used in two-player games like Chess, Go, and Tic Tac Toe. Its ability to calculate optimal moves makes it a valuable tool in game development and computer logic. In this project, the algorithm powers the AI in Tic Tac Toe, helping it to evaluate game states and make decisions that lead to victory or a tie.

## Game Explanation: Tic Tac Toe

**Tic Tac Toe** (also known as Noughts and Crosses) is a simple two-player game where players take turns marking spaces in a 3x3 grid. The goal is to align three of your marks (either X or O) in a row, column, or diagonal. The game ends when one player achieves this or when all spaces are filled without a winner (resulting in a tie).

### Rules:
1. The game is played on a 3x3 grid.
2. Two players take turns placing X and O on the grid.
3. The player who successfully places three of their marks in a horizontal, vertical, or diagonal row wins.
4. If all spaces are filled without a winner, the game ends in a draw.

## Negamax in Tic Tac Toe AI

The Negamax algorithm in this project is used by the AI to:
- Predict and evaluate the game state at each possible move.
- Make optimal decisions that either lead to a win or prevent the opponent from winning.
- Utilize **alpha-beta pruning** to reduce the search space and increase efficiency.

By using Negamax, the AI can consistently make intelligent moves, providing a challenging experience for the human player.

## Code Breakdown

### `TicTacToe` Class

The `TicTacToe` class defines the main logic for the game, including AI calculations using Negamax.

#### 1. `__init__(self)`
- Initializes the game board and defines possible moves (X and O).

```python
def __init__(self):
    self.board = None  # Board is initialized later
    self.moves = ['X', 'O']  # Two possible moves: X and O
```
#### 2. `get_free_positions(self)`
Returns a list of available positions on the board for the next move.

```python
def get_free_positions(self):
    return [k for k, v in enumerate(self.board) if v == '-']
```
#### 3. `evaluate(self)`
Evaluates the current state of the board, returning a score:
- 10 if X wins,
- 10 if O wins,
- 0 if no one has won yet.

```python
def evaluate(self):
    # Check rows, columns, and diagonals to determine the winner
    for i in range(0, 9, 3):
        if self.board[i] == self.board[i+1] and self.board[i+1] == self.board[i+2]:
            if self.board[i] == 'X':
                return -10
            elif self.board[i] == 'O':
                return 10
    # Check columns
    for i in range(3):
        if self.board[i] == self.board[i+3] and self.board[i+3] == self.board[i+6]:
            if self.board[i] == 'X':
                return -10
            elif self.board[i] == 'O':
                return 10
    # Check diagonals
    if self.board[0] == self.board[4] and self.board[4] == self.board[8]:
        if self.board[0] == 'X':
            return -10
        elif self.board[0] == 'O':
            return 10
    if self.board[2] == self.board[4] and self.board[4] == self.board[6]:
        if self.board[2] == 'X':
            return -10
        elif self.board[2] == 'O':
            return 10
    return 0
```

#### 4. `negamax(self, move, alpha=-float('inf'), beta=float('inf'), depth=0)`

Implements the Negamax algorithm with alpha-beta pruning to find the best move for the AI.

```python
def negamax(self, move, alpha=-float('inf'), beta=float('inf'), depth=0):
    score = self.evaluate()
    fp = self.get_free_positions()

    if score == 10 or score == -10 or len(fp) == 0:
        return score

    best_value = -float('inf')
    for pos in fp:
        self.board[pos] = self.moves[move]
        value = -self.negamax(not move, -beta, -alpha, depth + 1)
        self.board[pos] = '-'
        best_value = max(best_value, value)
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return best_value
```

#### 5. `findBestMove(self, board)`

Uses Negamax to determine the AI's best move.

```python
def findBestMove(self, board):
    bestVal = -1000
    choices = []
    self.board = board
    
    if len(self.get_free_positions()) == 9:
        return 4  # First move is always in the center

    for pos in self.get_free_positions():
        self.board[pos] = "O"
        val = self.negamax(False)
        self.board[pos] = '-'
        if val > bestVal:
            bestVal = val
            choices = [pos]
        elif val == bestVal:
            choices.append(pos)
    
    if choices != []:
        return random.choice(choices)
    else:
        return None
```
## How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/tictactoe-negamax.git
cd tictactoe-negamax
```

### Step 2: Run
```bash
python tictactoe.py
streamlit tictactoe.py
```
## Resource
- https://github.com/MathCatsAnd/Streamlit-Tic-Tac-Toe
- https://github.com/Cledersonbc/tic-tac-toe-minimax
