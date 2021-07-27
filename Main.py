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
import re
class Player:
    def __init__(self):
        self.__Name="Guest"
        self.__Score=0
    def AddScore(self, score): self.__Score+= score
    def ShowScore(self): return self.__Score
    def GetName(self, name): self.__Name=name
    def ReadName(self): return self.__Name
class GameManager():
	def __init__(self):
		self.PartyDeck=CC.Deck()
	def Instruction(self):
		file = open('gameInstructions.txt', 'r')
		file_contents = f.read()
		print (file_contents)
		file.close()
This viral game is simple to play (or is it?). Grab a card, show your team the #CultureTag (acronym) and give hints to help them guess the phrase without saying what it is. Can’t figure it out? Pass! Just get through as many answers as possible before your time runs out!")
	def AddMenu(self):
		pass
	def Games(self):
		pass
	def PlayGame(self):
		pass

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
	game1.menu()
				
if __name__ == "__main__"
	main()
