import copy
import random


class Agent:
    def __init__(self, boardObject) -> None:
        self.epsilon = 0.01
        self.initialState = boardObject
        self.currentState = boardObject
        self.wins = 0
        self.losses = 0
        self.currentEpisode = 1
        self.totalEpisodes = -1
    
    def resetBoard(self):
        self.currentState = self.initialState

    def takeStep(self):
        
        nextAction = self.getNextAction(self.currentState)
        if ( nextAction == None):
            return self.currentState.value

        self.takeAction(nextAction)
        
        if self.currentEpisode == self.totalEpisodes:
            printBoard(self.currentState)
            
        previousState = self.currentState
        nextAction = self.getEnemyAction( self.currentState)
        if (nextAction == None):
            return self.currentState.value
        self.enemyTakeAction(nextAction)
        
        if self.currentEpisode == self.totalEpisodes:
            printBoard(self.currentState)
            
        nextStateValue = self.takeStep()
        previousState.value = previousState.value + (1/(previousState.timestep))*(nextStateValue - previousState.value)

        return previousState.value
    
    
    def train(self, number):
        self.totalEpisodes = number
        self.wins = 0
        self.losses = 0
        while (self.currentEpisode <= number):
            self.takeStep()
            if self.currentState.value == 1:
                self.wins += 1
            else:
                self.losses +=1

            self.resetBoard()
            # if self.cycles%10 == 0:
            #     print(self.wins / self.cycles)
            self.currentEpisode+=1
            
        print( f"wins: {self.wins}, losses: {self.losses}")
        
        
       
    def getNextAction(self, boardObject):
        if len(boardObject.nextPossibleStates) == 0:
            agent.reward = boardObject.value
            return None
        epsilonCheck = random.random()

        if epsilonCheck > self.epsilon:
            maxValue = max(states.value for states in boardObject.nextPossibleStates)
            bestActions = [states for states in boardObject.nextPossibleStates if states.value == maxValue]
            return bestActions[0] if len(bestActions)==1 else bestActions[random.randint(0, len(bestActions )- 1)]
        else:
            return self.currentState.nextPossibleStates[random.randint(0, len(self.currentState.nextPossibleStates)- 1)]
        
    def takeAction(self, action):
        self.currentState = action

    def getEnemyAction(self, boardObject):
        if len(boardObject.nextPossibleStates) == 0:
            return None
        
        selfCanWin, i, j = self.canWin(boardObject.board, "O")
        if selfCanWin:
            # print(f"opponent took a winning move at {self.cycles}th iteration")
            return next(state for state in boardObject.nextPossibleStates if (state.i == i and state.j == j))
        
        opponentCanWin, i, j = self.canWin(boardObject.board, "X")
        if opponentCanWin:
            return next(state for state in boardObject.nextPossibleStates if (state.i == i and state.j == j))
        # uncomment this block to make the enemy always occupy the middle tile if possible
        # for state in boardObject.nextPossibleStates:
        #     if state.i == state.j == 1:
        #         return state
        return boardObject.nextPossibleStates[random.randint(0, len(boardObject.nextPossibleStates) - 1)]
            
    def enemyTakeAction(self, action):
        self.currentState = action

    def canWin(self, board, opponent):
        for i in range(0,3):
            for j in range(0,3):
                if (board[i][j] == "_"):
                    board[i][j] = opponent

                    if isTerminalState(board, opponent, i, j):
                        board[i][j] = "_"
                        return True, i, j
                    board[i][j] = "_"
        return False, None, None
    
class boardState:
    def __init__(self, board, currentPlayer, timestep, i, j) -> None:
        self.board = board
        self.value = 0.5
        self.player = currentPlayer
        self.nextPossibleStates = []
        self.timestep = timestep
        #previous moves
        self.i = i
        self.j = j

        
    def setAllStates(self, board, player):
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    newGameState = copy.deepcopy(board)
                    newGameState[i][j] = player
                    newState = boardState(newGameState, "O" if player == "X" else "X", self.timestep + 1 if player =="X" else self.timestep, i, j)
                    self.nextPossibleStates.append(newState)

                    if isTerminalState(newGameState, player, i, j):
                        setStateValue(newState, 1 if player == "X" else 0)
                    elif boardIsFilled(newGameState):
                        setStateValue(newState, 0)
                    else:
                        newState.setAllStates(newGameState, newState.player)
    
def setStateValue(boardObject, value):
    boardObject.value = value

def isTerminalState(board, player, i , j): 
    
    # checking horizontal and vertical
    if (board[i][0] == board[i][1] == board[i][2] and board[i][1] == player):
        return True
    
    if (board[0][j] == board[1][j] == board[2][j] and board[1][j] == player):
        return True
        
    # checking diagonals
    if (i,j) in [(0,0), (0,2), (1,1), (2,0), (2,2)]:
        if ( board[0][0] == board [1][1] == board[2][2] and board[1][1] == player):
            return True
        
        if (board[2][0] == board [1][1] == board[0][2] and board[2][0] == player):
            return True
    

def boardIsFilled(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                return False

    return True


def printBoard(state):
    if state.value == 0.5:
        print("Enemy action")
        print(f"{state.board[0]}")
    else:
        print(f"Agent took action [{state.i}][{state.j}]")
        print(f"{state.board[0]} Win%: {state.value}")
    print(state.board[1])
    print(state.board[2])
    print()

TTTBoard = [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]
                
originalBoard = boardState(TTTBoard, "X", 0, None, None)
originalBoard.setAllStates(originalBoard.board, originalBoard.player)

agent = Agent(originalBoard)
agent.train(5000)
