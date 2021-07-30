# Here will be a copy/my work of the deck and card classes

# from tabulate import tabulate
import csv

# Card Class 
class Card:
    def __init__(self, acr, ans, cat, hint):
        self.__Acronym = acr
        self.__Answer = ans
        self.__Category = cat
        self.__Hint = hint

    def __str__(self):
        return f'{self.GetAcr()} + "," + {self.GetAns()} + "," + {self.GetCat()} + "," + {self.GetHint()}'

    def GetAcr(self): return self.__Acronym
    def SetAcr(self, acr): self.__Acronym = acr

    def GetAns(self): return self.__Answer
    def SetAns(self, ans): self.__Answer = ans

    def GetAns(self): return self.__Category
    def SetAns(self, cat): self.__Category = cat

    def GetHint(self): return self.__Hint
    def SetHint(self, hint): self.__Hint = hint


# Deck class 
class Deck:
    def __init__(self):
        self.Deck = []
        self.StringDeck = []
        self.GenerateDeck()
        self.ShuffleDeck()
        self.rounds = 0         # The deck will take in 10 cards from the CSV for each round. next round the next 10 until max rounds is hit. then fill with whats left 
        self.maxRounds = 0      # Starts with 0 this will be changed later

    def GenerateDeck(self):
        with open('Culture_Tag.csv', 'r') as csvFile:
            csvFile = csv.reader(csvFile)

        # Get the # lines for the csv file
        # If round 1 skip over the first iteration 
        if self.rounds == 0:
            next(csvFile)

        # If the max rounds is hit then move to the nearest tenth
        elif self.rounds == self.maxRounds:
            next(csvFile + "Bruh")


    