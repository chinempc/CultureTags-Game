#Game requirements:
#Functions:
#	- Menu(option)
#		- Displays the user's choice to them
#		- Lets the user choose between the following
#		- 1: Instructions
#		- 2: Play Game
#		- 3: Add New Cards
#	- instructions()
#		- Prints out to the user the instructions to play the game.
#		- In the later build this will a graphically outputed, but for now it will be basic text.
#		- Either one long print statement or print out from a text file.
#	- playGame()
#		- Prompts the user to enter the number of players and their names.
#		- Presents the first player with a card. (read off the category, acryonym, and hint)
#		- Player #1 answers the question:
#			- Answers correctly:
#				+3 points
#			- Answers wrongly:
#				-1 point, tries again (1 try only)
#		- Display the correct answer and wether the user was correct or not. Then show the leaderboard with score.
#		- Move to player #2 and give then a new card
#			- User is allowed to skip their turn if they so choose.
#				- ASSUMING PLAYER #1 HAS TO PLAY THEIR TURN TO BEGIN THE GAME.
#		- Once all players get a turn. Show the current leader and ask if the players would like another round.
#			- Question: If someone skips does the next round start before asking for another round?
#		- 10 cards to start the game at minimum. Max 10 players.
#	- newCards()
#		- Allows the user to make a new card (Question:Answer).
#		- Confirm that the new card has been added and display the last 3 cards added. (Anything less than 3 show those cards).
#----------------------------------------------------------------------------------------------------------------------------------------#

# Title of the Game 
print       ("#CultuarlTag Game")
print ("------------------------------")
print ("------------------------------")

#Asking the player for their name
name = input("what is your player name ?")
print ("------------------------------------")
print ("------------------------------------")
print (" Welcome to #Cultural Tag : " + name)
print ("------------------------------------")
print ("------------------------------------")

Menu = input("\tTo continue the game you would need to choice following options before the game can begin :)" + name +""+":" )
menu_options = {

    1: 'Instructions',
    2: 'Play Game',
    3: 'Add New Cards',
    4: 'Skip',
}
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():#Intructions sting 
     print('\twhen a player grabs a card, they should show their team the #CultureTag (acronym) and give hints to help them guess the phrase of the game.')
def option2():#Playing the Game
     print('Handle option \'Option 2\'')

def option3():#Adding new Cards
     print('Handle option \'Option 3\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print("Thanks for reading the #CultualTag game plan" +" "+ name + " you can now being the the game.")
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


