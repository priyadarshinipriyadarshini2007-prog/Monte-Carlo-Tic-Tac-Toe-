# Monte Carlo Tic-Tac-Toe using MCTS

## 1. Problem Statement

Develop a Tic-Tac-Toe game agent using Monte Carlo Tree Search (MCTS). The system should select the best move by performing random game simulations instead of constructing the complete game tree. The performance of MCTS is also compared with the Minimax algorithm.

## 2. Objectives

- To implement a Tic-Tac-Toe game using Python.
- To implement Monte Carlo Tree Search.
- To demonstrate Selection, Expansion, Simulation and Backpropagation.
- To use random rollouts to guide the search.
- To compare MCTS with the Minimax algorithm.
- To develop an intelligent game-playing agent.

## 3. Technologies Used

- Python
- Monte Carlo Tree Search (MCTS)
- Minimax Algorithm
- GitHub

## 4. Dataset

No external dataset is required for this project. The game board and possible moves are generated dynamically during gameplay.

## 5. Methodology

The MCTS algorithm works through four main stages:

1. Selection – Select the most promising node using the UCT formula.
2. Expansion – Add an unexplored move to the search tree.
3. Simulation – Perform random moves until the game reaches a terminal state.
4. Backpropagation – Update the visit count and win statistics of the nodes.

These steps are repeated for a fixed number of iterations. The move with the highest number of visits is selected as the best move.

## 6. System Architecture

The system consists of the following components:

User
↓
Tic-Tac-Toe Board
↓
MCTS Agent
↓
Selection
↓
Expansion
↓
Simulation
↓
Backpropagation
↓
Best Move
↓
Game Result

## 7. Implementation

The project is implemented in Python using the following components:

- Tic-Tac-Toe board representation
- Winning condition checking
- Available move generation
- MCTS Node
- Selection using UCT
- Expansion of unexplored moves
- Random simulation
- Backpropagation of results
- Minimax algorithm for comparison
- Game interface for the user

## 8. Results

The MCTS agent successfully selects moves by using repeated random simulations. It can play Tic-Tac-Toe without generating the complete game tree.

MCTS and Minimax are compared based on their method of selecting moves. MCTS uses simulations and exploration, while Minimax systematically evaluates possible game states.

## 9. Screenshots

Add screenshots of:

- Tic-Tac-Toe game board
- MCTS agent selecting a move
- Game result
- MCTS vs Minimax comparison

## 10. How to Run

1. Install Python.
2. Download or clone this repository.
3. Open the project folder.
4. Run the following command:

```bash
python main.py
