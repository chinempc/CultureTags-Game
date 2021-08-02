import CultCards as CC
from CultCards import tabulate
import time
import os
import re
from threading import Timer
from threading import Thread

# Player class
class Player: 
    def __init__(self, name = "Guest"):
        self.__Name = name
        self.__Score = 10
        self.__Skip = False
    
    def AddScore(self): self.__Score += 3
    def SubScore(self): self.__Score -= 1
    def GetScore(self): return self.__Score
    def SetName(self, name): self.__Name = name
    def GetName(self): return self.__Name
    def GetSkip(self): return self.__Skip
    def SetSkip(self, skip): self.__Skip = skip
    def __str__(self): return f'{self.__Name}, Score: {self.__Score}'

# LeaderBoard class
class LeaderBoard():
    def __init__(self):
        self.Players = {}
        self.Winners = []

    def AddtoLeaderBoard(self, Players:dict):   self.Players = Players
    def SortLeaderBoard(self):
        # Bubble sort 
        PlayersList = list(self.Players.values())
        keys = list(self.Players.keys())
        n = len(PlayersList)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if PlayersList[j].GetScore() < PlayersList[j+1].GetScore():
                    PlayersList[j], PlayersList[j+1] = PlayersList[j+1], PlayersList[j]
                    keys[j], keys[j+1] = keys[j+1], keys[j]
        self.Players = dict(zip(keys, PlayersList))

    def GetWinners(self):
        self.SortLeaderBoard()
        PlayerList = list(self.Players.values())
        self.Winners.append(str(PlayerList[0]))
        HighestScore = PlayerList[0].GetScore()
        for i in range(1, len(PlayerList)):
            if PlayerList[i] == HighestScore:
                self.Winners.append(str(self.Players[key]))

    def DisplayWinners(self):
        print("\n\nHere are the winners")
        for i in self.Winners:
            print(i)
    
    def ShowLeaderBoard(self):
        SelectionScreen = [["--- Leaderboard ---"]]
        ScreenDisplay = tabulate(SelectionScreen, tablefmt = "pretty")
        print(f"\n{ScreenDisplay}")
        for key in self.Players.keys():
            print(f"{key} --> {self.Players[key]}")
        print("\n\n")

# Game Manager Class
class GameManager():
    def __init__(self):
        self.PartyDeck = CC.Deck()
        self.PlayerLimit = 10
        self.GameLB = LeaderBoard()
        self.Players = {}
        self.PresentedCard = None   
        self.Menu()

    def Instruction(self):
        print("\n\n\n")
        with open('gameInstructions.txt', 'r') as file:
            FileContents = file.read()
            print(FileContents)
        print("\n\n\n")

    def Menu(self):
        Online = True
        SelectionScreen = [["--- Culture Tag Menu ---"], ["1.) Instruction"], ["2.) Start Game"],["3.) Add a Card"],["4.) Quit"]]
        ScreenDisplay = tabulate(SelectionScreen, tablefmt = "pretty")
        while Online:
            print(ScreenDisplay)
            UserInput = int(input("Enter the one of the following options above: "))
            while UserInput < 0 and UserInput > 4:
                UserInput = int(input("Invalid input. Please enter either 1, 2, 3, or 4.\nChoose an option: "))
            if UserInput == 1: self.Instruction()
            if UserInput == 2: self.PlayGame()
            if UserInput == 3: self.AddNewCard()
            if UserInput == 4:
                print("Thanks for playing! Good bye.")
                Online = False
    
    def AddPlayer(self):
        NumberOfPlayers = int(input("Enter the number of players: "))
        while NumberOfPlayers > self.PlayerLimit or NumberOfPlayers < 0:
            NumberOfPlayers = int(input("Invalid input, players must be between 1 and 10.\nEnter the number of players: "))
        for i in range(NumberOfPlayers):
            NewPlayer = Player()
            PlayerType = "Player " + str(i+1)
            name = input(f"Enter the name of player {i+1}: ")
            check = input(f"{name}, is that correct?\n(yes or no): ")
            while check.lower() != "yes":
                if check.lower() != "no":
                    name = input(f"I didn't get that...\nPlease Enter the name of player {i+1}: ")
                else:
                    name = input(f"Ok, renter the name of player {i+1}: ")
                check = input(f"{name}, is that correct?\n(yes or no): ")
            NewPlayer.SetName(name)
            self.Players[PlayerType] = NewPlayer
        self.GameLB.AddtoLeaderBoard(self.Players)

    def PlayGame(self):
        playing = True
        confirm = ""
        rounds = 0
        self.AddPlayer()
        while playing == True:
            rounds += 1
            for key in self.Players.keys():
                print(f"{self.Players[key].GetName()} Ready? You will have 90 seconds to answer. \nPress Enter to continue...")
                Ready = input() # Pause screen
                self.PresentedCard = self.PartyDeck.Deck[len(self.PartyDeck.Deck) - 1]       
                self.PartyDeck.ReadTopCard()
                Response = self.AnswerQuestion()
                if Response == "Timelimit":
                    print("TIMES UP: -1 point")
                    self.Players[key].subScore()    # -1 score
                elif Response == "Pass":
                    print("OK, onto the next player...We will come back to you")
                elif Response == True:
                    print("Correct: +3 Points")     # add logic to print points after each =
                    self.Players[key].AddScore()
                elif Response == False:     # Add logic to let them try twice
                    print("Incorrect: -1 point. You will get to try again.\n")
                    self.Players[key].SubScore()
                self.PartyDeck.Deck.pop()
                self.PartyDeck.ShuffleDeck()
            self.GameLB.SortLeaderBoard()
            self.GameLB.ShowLeaderBoard()
            confirm = input("Would you like to play another round? ('N' : No | 'Y' : Yes ) \n: ")
            while confirm[0].upper() != 'Y' and confirm[0].upper() != 'N':
                confirm = input("Invalid input. Please type in yes or no.\nWould you like to play another round? ('N' : No | 'Y' : Yes ) \n: ")
            if confirm[0].upper() == 'N':
                self.GameLB.GetWinners()
                self.GameLB.DisplayWinners()
                self.GameLB.ShowLeaderBoard()
                playing = False

    def CheckAnswer(self, Response):
        Answer = self.PresentedCard.GetAnswer()
        A = Answer.replace(" ", "")
        B = Response.replace(" ", "")
        while len(B) != len(A):
            if len(B) > len(A):
                B = B[:-1]
            elif len(B) < len(A):
                B += " "
        A = A.upper()
        B = B.upper()
        Character = 0.0
        for i in range(len(A)):
            if B[i] == A[i]:
                Character += 1.0
        Accuracy = Character / len(A)
        if Accuracy > .6:
            return True
        return False

    def AnswerQuestion(self):
        timer = time.time() + 90
        Correct = False
        Answer = input("Take a guess. You may pass by pressing 1 + Enter.\nAnswer: ")
        if time.time() > timer and Answer[0] != "1":
            return "TimeLimit"
        elif Answer[0] == "1":
            return "Pass"
        else:
            Correct = self.CheckAnswer(Answer)
            return Correct
    
    # Threading attempt does not work 
    def TimeCounter(self):
        for i in range(10):
            if self.Answer != None:
                return
            time.sleep(1)



    def AddNewCard(self):
        Confirmation=False
        while Confirmation==False:
            Res=input("Enter your Cards Acronym, Answer, Category(Optional), and Hint(Optional)\n"+"[Example: JD, John Doe, Person, A name that is very anonymous\n]"+"Text: ")
            Modify=re.split(",",Res)
            Result=[]
            if len(Modify)<=1 or len(Modify)>4:
                print("CreationError: You must at least enter an Acronym and Answer and at most enter the Category and Hint\n")
            else:
                for i in Modify:
                    A=""
                    if i==" "or i=="":
                        A="?"
                    else:
                        if i[:1]==" " and i[-1:]==" ":
                            A=i[1:-1]
                        else:
                            if i[:1] == " ": #Check if there is a space in front of the character
                                A=i[1:]
                            elif i[-1:] == " ":
                                A=i[:-1]
                            else:
                                A=i
                        Result.append(A)
                        if len(Modify) !=4:
                            for i in range(4-len(Modify)):
                                Result.append("?")
                        if Result[1]=="?":
                            print("CreationError: You must at least enter an Acronym and Answer and at most enter the Category and Hint\n")
                            Result.clear()
                        else:
                            print(Result)
                            Confirm=input("Is this your final Result (Y/N): ")
                            Confirm=Confirm.upper()
                            if Confirm[0]=="Y":
                                Confirmation=self.PartyDeck.CreateCard(Result[0].upper(),Result[1],Result[2],Result[3])
                                if Confirmation==False:
                                    print("Sorry this acronym is already taken\n")
                                else:
                                    print("New Card has been created")
                            else:
                                pass


            



def main():
    game1 = GameManager()
    '''
    l = CC.Deck()
    l.ReadTopCard()
    '''

if __name__ == "__main__":
	main()