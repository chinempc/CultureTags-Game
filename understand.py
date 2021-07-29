import time
from threading import Thread

# Player class
class Player:
    def __init__(self, name = 'Guest'):
        self.__name = name
        self.__score=10     # Start the user off with a initial score
    def AddScore(self): self.__score += 3
    def DeductScore(self): self.__score -= 1
    def GetScore(self): return self.__score
    def GetName(self): return self.name
    def SetName(self, name): self.__name = name
    def ReadName(self): return self.name
    def __str__(self):  return f'{self.name}, Score: {self.score}'


# Game Manager class
    # The leaderboard will be a function that will print out the player array in decrementing order
class gameManager:
    def __init__(self):
        self.PlayerLimit = 10
        self.Players = []
        self.LeaderBoard = []
        self.mainMenus()

    def Instruction(self):
        print("\n\n\n")
        with open('gameInstructions.txt', 'r') as file:
            FileContents = file.read()
            print(FileContents)

    def mainMenus(self):
        print("1: HOW TO PLAY")
        print("2: START A NEW GAME")
        print("3: MAKE A NEW CARD")
        print("0: EXIT")
        UserInput = int(input("Please enter one of the following.\n Choice: "))
        while UserInput != 0:
            if UserInput == 1:
                self.Instruction()
                UserInput = 5
            elif UserInput == 2:
                self.PlayGame()
                UserInput = 5
            elif UserInput == 3:
                self.AddNewCard()
                UserInput = 5
            else:
                if UserInput != 5:
                    print("Invalid input!\n\n")
                print("1: HOW TO PLAY")
                print("2: START A NEW GAME")
                print("3: MAKE A NEW CARD")
                print("0: EXIT")
                UserInput = int(input("Please Choose one of the follwing.\nChoice: "))
        print("Thank you for playing")

    def mainMenu(self):
        print("1: HOW TO PLAY")
        print("2: START A NEW GAME")
        print("3: MAKE A NEW CARD")
        print("0: EXIT")
        UserInput = int(input("Please select one of the following options.\nYour Choice: "))
        while UserInput > 3 or UserInput < 0:
            UserInput = int(input("Please select one of the following options.\nYour Choice: "))
        if UserInput == 1: self.Instruction()
        elif UserInput == 2: self.PlayGame()
        elif UserInput == 3: self.AddNewCard()
        else:
            print("Thanks for playing!")
    
    def PlayGame(self):
        # Initialize players and their names.
        self.AddPlayer()
        ''' 
        Just for printing out the list of players
        for i in range(len(self.Players)):
            print(self.Players[i].name)
            print(self.Players[i].GetName())
        '''
        # Print out the first card to player 1
        nextGame = True
        while nextGame:
            pass

    def SortLeaderBoard(self, board):
        if len(board) == 1:
            return board
        # Split the array in two parts
        LeftBoard = board[:len(board)//2]
        RightBoard = board[len(board)//2:]

        # Merge both halfs into a sorted board
        SortLeaderBoard(LeftBoard)
        SortLeaderBoard(RightBoard)

        # Merge both halfs into a sorted array.
        LeftIndex = 0
        RightIndex = 0
        Index = 0
        while LeftIndex < len(LefttIndex) and RightIndex < len(RightBoard):
            if LeftBoard[LeftIndex].GetScore() > RightBoard[RightIndex].GetScore():
                board[Index] = LeftBoard[LeftIndex]
                LeftIndex += 1
            else:
                board[Index] = RightBoard[RightIndex]
                RightIndex += 1
            Index += 1

        # Append anything left on the left
        while LeftIndex < len(LeftBoard):
            board[Index] = LeftBoard[LeftIndex]
            LeftIndex += 1
            Index += 1

        # Append anything left in the right 
        while RightIndex < len(RightIndex):
            board[Index] = RightBoard[RightIndex]
            RightIndex += 1
            Index += 1
        self.LeaderBoard = board

    def AddPlayer(self):
        NumofPlayers = int(input("Enter the number of players in this game: "))
        print(f"There will be {NumofPlayers} players in this game.")
        while NumofPlayers > self.PlayerLimit or NumofPlayers < 0:
            NumofPlayers = int(input("INVALID INPUT! Must be between 1 and 10.\n# of players: "))
        for i in range(NumofPlayers):   # ISSUE: INFINTE LOOP
            name = input(f"Enter the name of player {i+1}: ")
            check = input(f"{name}, is that correct?\n(yes or no): ")
            while check.lower() != "yes":
                print(f"Your input {check} vs 'yes' are not the same.")
                name = input(f"Ok, renter the name of player {i+1}: ")
                check = input(f"{name}, is that correct?\n(yes or no): ")
            NewPlayer = Player(name)
            self.Players.append(NewPlayer)
        self.LeaderBoard = self.Players      # Leaderboard is ordered from 
	
    def AnswerQuestion(self):             
    	answer = None
    	def timeout():
        	time.sleep(90)              # 90 seconds to answer question       
        	if answer != None:
            		return
        	print("Times Up")
    	Thread(target = timeout).start()
    	answer = input("Input answer: ")
    	return answer


'''
    def addNewCard(self):
        pass
'''

def main():
	game1 = gameManager()

if __name__ == "__main__":
	main()
