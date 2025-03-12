# FastAPI Game API

## Description

This is an API built using FastAPI that implements board game mechanics with support for various AI algorithms, such as Minimax and Monte Carlo.

## Installation

To run the API, install the required dependencies:

```bash
pip install fastapi uvicorn
```

Then, start the server with:

```bash
uvicorn main:app --reload
```

## Endpoints

### 1. `POST /start_game`
**Description**: Initializes a new game.

**Parameters**:
- `n` (int) - Board size.

**Returns**:
- `game` (list) - Initial game state.

### 2. `POST /get_valid_moves`
**Description**: Returns a list of valid moves for the player.

**Parameters**:
- `tab` (list) - Current game state.
- `player` (int) - Player number.

**Returns**:
- `valid_moves` (list) - List of available moves.

### 3. `POST /make_move`
**Description**: Makes a move for the player.

**Parameters**:
- `tab` (list) - Current game state.
- `move` (tuple) - Move to be made.
- `player` (int) - Player number.

**Returns**:
- `new_game_state` (list) - Updated game state.
- `winner` (int) - Winner number or 0 if the game is still ongoing.

### 4. `POST /generate_move_minmax`
**Description**: Generates the best move for the player using the Minimax algorithm.

**Parameters**:
- `game` (list) - Current game state.
- `depth` (int) - Search depth.
- `if_alphabeta` (bool) - Whether to use Alpha-Beta pruning.

**Returns**:
- `best_move` (tuple) - Best move.

### 5. `POST /generate_move_monte_carlo`
**Description**: Generates the best move for the player using the Monte Carlo algorithm.

**Parameters**:
- `game` (list) - Current game state.
- `time` (int) - Time limit for analysis.

**Returns**:
- `best_move` (tuple) - Best move.

## Author
This project was created to demonstrate Minimax and Monte Carlo algorithms in the game Clonium.

