import copy

class gameStateTree: 
    
    def __init__(self, currentBoard):
        self.currentBoard = currentBoard
        self.possibleGameStates = []
        self.score = 0
        
    def getPossibleGameStates(self, board, player):
        for i in range(0,3):
            for j in range(0,3):
                if (board[i][j] == "_" and player == "Max"): # 2 means theres no symbol on that box
                    newGameState = copy.deepcopy(board)
                    newGameState[i][j] = "X"
                    self.possibleGameStates.append(gameStateTree(newGameState))
                    
                elif (board[i][j] == "_" and player == "Min"):
                    newGameState = copy.deepcopy(board)
                    newGameState[i][j] = "O"
                    self.possibleGameStates.append(gameStateTree(newGameState))
        
        for gameState in self.possibleGameStates:   
            
            isFinal, score = self.isTerminalState(gameState.currentBoard, player)
            scores = []
            
            if isFinal:
                gameState.score = score
            else:
                gameState.getPossibleGameStates( gameState.currentBoard, "Max" if player == "Min" else "Min")
        # player = "Max" if player == "Min" else "Min"

        
        reward = max(state.score for state in self.possibleGameStates) if player == "Max" else min(state.score for state in self.possibleGameStates)

        self.score = reward

    def isTerminalState(self, board, player): 
        score = 10 if player == "Max" else -10
        # checking horizontal and vertical
        for i in range (0,3):
            if (board[i][0] == board[i][1] == board[i][2] and board[i][1] in ["X","O"]):
                return True, score
            if (board[0][i] == board[1][i] == board[2][i] and board[1][i] in ["X","O"]):
                return True, score
            
        # checking diagonals
        if ( board[0][0] == board [1][1] == board[2][2] and board[1][1] in ["X","O"]):
            return True, score
        
        if (board[2][0] == board [1][1] == board[0][2] and board[2][0] in ["X","O"]):
            return True, score
        
        # checking if there are moves left
        return self.boardIsFilled(board), 0
 
    
    def boardIsFilled(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    return False
        return True
    


def printBoard(GS):
    for state in GS.possibleGameStates:
        print(f"{state.currentBoard[0]} score:{state.score}")
        print(state.currentBoard[1])
        print(state.currentBoard[2])
        print()
        
TTTBoard = [["X", "O", "_"],
            ["X", "X", "_"],
            ["_", "_", "O"]]
    
           
x = gameStateTree(TTTBoard)
x.getPossibleGameStates(x.currentBoard, "Min")

printBoard(x)

