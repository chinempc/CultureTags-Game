"""
Game requirements:
Functions:
	- Menu(option)
		- Displays the user's choice to them
		- Lets the user choose between the following
		- 1: Instructions
		- 2: Play Game
		- 3: Add New Cards
	- instructions()
		- Prints out to the user the instructions to play the game.
		- In the later build this will a graphically outputed, but for now it will be basic text.
		- Either one long print statement or print out from a text file.
	- playGame()
		- Prompts the user to enter the number of players and their names.
		- Presents the first player with a card. (read off the category, acryonym, and hint)
		- Player #1 answers the question:
			- Answers correctly:
				+3 points
			- Answers wrongly:
				-1 point, tries again (1 try only)
		- Display the correct answer and wether the user was correct or not. Then show the leaderboard with score.
		- Move to player #2 and give then a new card
			- User is allowed to skip their turn if they so choose.
				- ASSUMING PLAYER #1 HAS TO PLAY THEIR TURN TO BEGIN THE GAME.
		- Once all players get a turn. Show the current leader and ask if the players would like another round.
			- Question: If someone skips does the next round start before asking for another round?
		- 10 cards to start the game at minimum. Max 10 players.
	- newCards()
		- Allows the user to make a new card (Question:Answer).
		- Confirm that the new card has been added and display the last 3 cards added. (Anything less than 3 show those cards).
CLASSES:
Game {}:
	Variables:
		- Players: Array of Player elements
		- # of players: Int
		- Deck: List of cards
		- Scoreboard: (Find some way to print out players array in decrementing order )
	Functions:
		Games():
			- Calls the menu() function
		Menu():
			- Prints out the 3 options for the user and takes their input.
			- 1: Calls Instructions()
			- 2: Calls playgame()
			- 3: Calls addNewCard()
			- -1: exit the program
		instructions():
			- Prints out the instructions either in a print statement or prints from a text file.
			- Returns back to the menu function
		playGame():
			Variables:
				nextRound: Int
			- do while loop: while nextRound == "YES" (all input will be uppercased to account for typo)
			- Prompt the user to enter the number of players
			- Loop through and fill the players list with the names of each player
			- Print out the first card in the deck under "Player 1's turn"
			- If they get it right increment the player's score by 3. Else decrement
			- Show the right answer and print out the scoreboard.
			- Rotate to the next player
Card {}
	variables:
		- info: Hashtable/Dictionary
Player {}
	Variables:
		- Name: String
		- Score: Int (10)
"""
import CultCards as CC
from CultCards import tabulate
import time
import os
import re
class Player:
	def __init__(self):
		self.__Name="Guest"
		self.__Score=0
	def AddScore(self, score:int): self.__Score+= score
	def GetScore(self): return self.__Score
	def GetName(self, name): self.__Name=name
	def SetName(self):
			return self.__Name
	def __str__(self):
    		return f'{self.__Name}, Score: {self.__Score}'

class LeaderBoard():
    def __init__(self):
            self.Players={}
            self.Winners = []
    def AddtoLeaderBoard(self, Players:dict):
		    self.Players=Players
    def SortLeaderBoard(self):
            PlayerList=list(self.Players)
            n=len(PlayerList)
            for i in range(n-1):
                for j in range(0,n-i-1):
                   if PlayerList[j][1].GetScore() > PlayerList[j+1][1].GetScore():
                      PlayerList[j],PlayerList[j+1] = PlayerList[j+1], PlayerList[j]
            self.Players=dict(PlayerList)
    def GetWinners(self):
            self.SortLeaderBoard()
            PlayerList=list(self.Players.values())
            self.Winners.append(str(PlayerList[0]))
            HighestScore=PlayerList[0].GetScore()
            for i in range(1,len(PlayerList)):
                 if PlayerList[i] == HighestScore:
                    self.Winners.append(str(PlayerList[i]))
    def DisplayWinners(self):
            print(self.Winners)
    def ShowLeaderBoard(self):
            for key in self.Players.keys():
                print(key+"-->"+str(self.Players[key]))
class GameManager():
	def __init__(self):
		self.PartyDeck=CC.Deck()
		self.PlayerLimit=10
		self.GameLB=LeaderBoard()
		self.Players={}
		self.PresentedCard=None
	def Instruction(self):
		with open('gameInstructions.txt', 'r') as f:
			file_contents = f.read()
			print (file_contents)

	def Menu(self):
		Online=True
		SelectionScreen=[["---Culture Tag Menu---"],["1.) Instructions"],["2.) Start Game"],["3.) Add a Card"],["4.) Quit"]]
		ScreenDisplay=tabulate(SelectionScreen,tablefmt="pretty")
		while Online:
			print(ScreenDisplay)
			UserInput=int(input("Enter the respectful options above: "))
			while UserInput<0 and UserInput>4:
					UserInput=input("Invalid input enter 1,2,3 or 4")
			if UserInput == 1:self.Instruction()
			elif UserInput==2: self.PlayGame()
			elif UserInput==3: self.AddNewCard()
			elif UserInput==4:
					print("Good Bye")
					Online=False

	def AddPlayer(self):
		NumofPlayers=int(input("Enter the number of players in this game: "))
		while NumofPlayers>self.PlayerLimit or NumofPlayers<0:
    			NumofPlayers=int(input("Invalid input there must be a number that is at least yourself or at most 10 people\nEnter the number of players: "))
		for i in range(NumofPlayers):
				NewPlayer=Player()
				PlayerType="Player "+str(i+1)
				name=input("Enter your name: ")
				NewPlayer.GetName(name)
				self.Players[PlayerType]=NewPlayer
		self.GameLB.AddtoLeaderBoard(self.Players)


	def PlayGame(self):#Game Logic
		playing=True
		Confirm=""
		rounds=0
		self.AddPlayer()
		while playing==True:
			rounds+=1
			for key in self.Players.keys():
				print(str(key)+" "+str(self.Players[key].SetName())+" Are you ready? press any key to continue: ")
				Ready=input()
				self.PresentedCard = self.PartyDeck[len(self.PartyDeck) - 1]
				self.PartyDeck.ReadTopCard()
				print(self.PresentedCard.GetHint())
				Response=self.AnswerQuestion()
				if Response == "Timelimit":
					print("You blew it you didn't answer in time you lose a point")
					self.Players[key].AddScore(-1)
				elif Response == "Pass":
					print("Ok you wont answer that's fair")
				elif Response == True:
					print("Correct 3 point The answer is "+str(self.PresentedCard.GetAnswer()))
					self.Players[key].AddScore(3)
				elif Response == False:
					print("Incorrect the answer is "+ str(self.PresentedCard.GetAnswer()))
					self.Players[key].AddScore(-1)
				self.PartyDeck.pop()
				self.PartyDeck.ShuffleDeck()
				self.GameLB.SortLeaderBoard()
				self.GameLB.ShowLeaderBoard()
			Confirm=input("Want to play again(y/n)?: ")
			Confirm=Confirm.upper()
			while Confirm[0]!="Y" or Confirm!="N":
				Confirm=input("Invalid input Try entering yes or no")
				Confirm=Confirm.upper()
			if Confirm[0]=="Y":
				pass
			elif Confirm[0]=="N":
				print("And that's the game Here your winners")
				self.GameLB.GetWinners()
				self.GameLB.DisplayWinners()
				self.GameLB.ShowLeaderBoard()
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

	def CheckAnswer(self,Response):
		Answer= self.PresentedCard.GetAnswer()
		A = Answer.replace(" ", "")
		B = Response.replace(" ","")
		while len(B) > len(A) or len(B)<len(A):
			if len(B) > len(A):
				B=B[:-1]
			elif len(B)<len(A):
				B+=" "
		A=A.upper()
		B=B.upper()
		Character=0.0
		for i in range(len(A)):
			if B[i]==A[i]:
				Character+=1.0
			else:
				pass
		Accuracy=Character/len(A)
		if Accuracy > .60:
			return True
		else:
			return False
	def AnswerQuestion(self):
		timer=time.time()+90
		Correct=False
		Answer=input("Say Something to pass the answer Just say 1: ")
		if time.time()>timer and Answer[0]!="1": #If time exceed the time limit and Answer is not 1
			Answer="TimeLimit"
			return Answer
		elif Answer[0]=="1": #If Answer=1 then call a pass
			Answer="Pass"
			return Answer
		else:
			Correct=self.CheckAnswer(Answer)
		return Correct
def main():
	game1 = GameManager()
	game1.Menu()
if __name__ == "__main__":
	main()
