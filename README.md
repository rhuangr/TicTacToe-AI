# Tic-Tac-Toe AI
## Project Description
This is my first project which involves using artificial intelligence to solve tic-tac-toe

TTT-minimax.py is an implementation of the minimax algorithm.

TTT-value-function.py follows the algorithm described in the book ***Reinforcement Learning An Introduction by Barto and Sutton*** chapter 1.5. The algorithm trains an agent against an opponent with a fixed policy: always win if possible, always prevent a winning move, otherwise take a random move.
> **Note:** The best moves generated are only the best moves given this fixed opponent

## Installation
1. Clone the repository
2. Run either of the individual python files.
	*You can paste the following commands while in the cloned repository directory :thumbsup:
   `python TTT-minimax.py` or `python TTT-value-function.py`*
## Instructions
### For minimax:
- To test specific boards, change the value of `TTTBoard` at the end of the code
- In the following line, set the current player to `"Max"` if the next move played will be X and `"Min"` elsewise.
### For value function:
- In the last line `agent.train(episodes)`, change the value of episodes depending on the amount of games you wish to train the agent on 
