# Monte Carlo Tic-Tac-Toe using MCTS

## Student Details

Name: YOUR NAME
Register Number: YOUR REGISTER NUMBER
Course: Foundations of Artificial Intelligence

## 1. Problem Statement

The objective of this project is to develop a Tic-Tac-Toe
agent using Monte Carlo Tree Search (MCTS).

The system uses random game simulations to decide which move
is promising instead of constructing the complete game tree.

The MCTS agent is also compared with a Minimax-based agent.

## 2. Objectives

- Implement Tic-Tac-Toe game logic.
- Implement Monte Carlo Tree Search.
- Demonstrate Selection, Expansion, Simulation and
  Backpropagation.
- Use random rollouts to evaluate possible moves.
- Compare MCTS performance with Minimax.

## 3. MCTS Approach

MCTS consists of four major steps:

1. Selection
2. Expansion
3. Simulation
4. Backpropagation

### Selection

The algorithm selects a promising node using the UCT formula.

### Expansion

A new child node is created for an unexplored move.

### Simulation

A random game is played from the selected node until
the game reaches a terminal state.

### Backpropagation

The simulation result is propagated back through the tree
to update visit and win statistics.

## 4. UCT Formula

UCT =

Win Rate + C × sqrt(log(parent visits) / child visits)

The formula balances exploitation and exploration.

## 5. Minimax Comparison

The project compares MCTS with Minimax.

MCTS uses random simulations to estimate promising moves,
while Minimax searches the game tree using game outcomes.

## 6. How to Run

Clone the repository.

Install dependencies:

pip install -r requirements.txt

Run the comparison:

python src/compare.py

Run tests:

pytest

## 7. Sample Output

MCTS vs Minimax
----------------
Total Games : 20
MCTS Wins   : ...
Minimax Wins: ...
Draws       : ...

The exact result may vary because MCTS uses random
simulations.

## 8. Complexity

MCTS complexity depends mainly on the number of simulations.

If N simulations are performed and each simulation takes
up to D moves, the approximate simulation work is O(ND).

Minimax explores possible game states and can grow
exponentially with search depth.

## 9. Applications

- Game-playing AI
- Decision-making systems
- Search problems
- Robotics planning
- Strategy optimization

## 10. Reflection

The main challenge was implementing the four stages of MCTS
and maintaining statistics for each node.

The project demonstrates how random rollouts can guide the
search without constructing the complete game tree.

## 11. Honesty Note

AI tools and online references were consulted for learning
and implementation guidance. The submitted code was tested
and understood by the student.

## 12. References

1. Sutton, R. S. and Barto, A. G., Reinforcement Learning:
   An Introduction.

2. Browne, C. B. et al., A Survey of Monte Carlo Tree Search
   Methods, IEEE Transactions on Computational Intelligence
   and AI in Games.

3. Russell, S. and Norvig, P., Artificial Intelligence:
   A Modern Approach.
