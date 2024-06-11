# Tic-Tac-Toe AI
## Project Description
This is my first project which involves using artificial intelligence to play tic-tac-toe

TTT-minimax.py is an implementation of the minimax algorithm.

TTT-value-function.py follows the algorithm described in the book ***Reinforcement Learning An Introduction by Barto and Sutton***. The algorithm trains an agent against an opponent with a fixed policy: always win if possible, always prevent a winning move, otherwise take a random move.
> **Note:** The best move generated is only the best move given this fixed opponent

## Installation
1. Clone the repository
2. Run the either of the individual python files.
	*You can paste the following commands while in the cloned repository directory :thumbsup:
   `python TTT-minimax.py` or `python TTT-value-function.py`*
## Instructions
### For minimax:
1. To test specific boards, change the value of `TTTBoard` at the end of the code
2. In the following line, set the current player to `"Max"` if the next move played will be X and `"Min"` elsewise.
### For value function:
1. Change the value of episodes, depending on many games you want to in the last line `agent.train(episodes)`
