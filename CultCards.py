from tabulate import tabulate

# What does import pandas as pd mean
#------------------------------------
#Import = “Bring this functionality or library to my python script”
#Pandas = The library you want to import, in this case, it’s pandas
#As = The python nomenclature for creating as alias. This is a fancy way of taking a long word and referencing it as a short word
#pd = The standard short name for referencing pandas 

import pandas as pd # Used for importing,creating and exporting a CDV file"Culture_Tag.csv"
import random # Random generates numbers between 0 and 1.

class Card: #Data set that allows to set all content of the card in this Data set
    def  __init__(self):
        self.__Acronym="?"
        self.__Answer="?"
        self.__Category="?"
        self.__Hint="?"
        self.__FrontofCard=self.GetFrontofCard()
        self.__BackofCard=self.GetBackofCard()

    def  __init__(self,Acr,Ans,Cat,Hint): # setting the content of the card in this constructor
        self.__Acronym=Acr
        self.__Answer=Ans
        self.__Category=Cat
        self.__Hint=Hint
        self.__FrontofCard=self.GetFrontofCard()
        self.__BackofCard=self.GetBackofCard()

    def __str__(self): #when class used as a print or converted to string, it will print Acronym, Answers, Category, and Hint
        return (str(self.__Acronym) +" , " + str(self.__Answer) +", " + str(self.__Category)+ ", "+ str(self.__Hint))
    def GetAcronym(self): return self.__Acronym #Returns Acronym
    def GetAnswer(self): return self.__Answer #Returns Answer
    def GetCategory(self): return self.__Category #Returns Category
    def GetHint(self):return self.__Hint #Returns Hint
    def GetFrontofCard(self):
        CardText= [["Category: "+self.__Category],["Acronym: "+self.__Acronym], ["Hint: " + self.__Hint]]
        CardDisplay=tabulate(CardText, tablefmt="fancy-grid")
        return CardDisplay
    def GetBackofCard(self):
        CardText= [["Answer: "+self.__Answer]]
        CardDisplay=tabulate(CardText, tablefmt="fancy-grid")
        return CardDisplay
    def GetBothSides(self):
        return (self.__FrontofCard+"\n"+self.__BackofCard)

class Deck(): #This Deck will get the card details from the Culture_Tag.csv, convert them into card classes and store them in
    def __init__(self):
        self.Deck=[]
        self.DeckString=[]
        self.GenerateDeck()
        self.ShuffleDeck()

    def GenerateDeck(self):# Creating a Generated Deck 
        data = pd.read_csv('Culture_Tag.csv', encoding="ISO-8859-1")
        for index, row in data.iterrows():
            A=Card(row['ACR'],row['ANS'],row['Category'],row['Hint'])
            self.Deck.append(A)
            self.DeckString.append(str(A))
            
    def ClearDeck(self): # Creating a clear deck 
        self.Deck.clear()
        self.DeckString.clear()
        
    def ShuffleDeck(self):random.shuffle(self.Deck) #Use the random function to shuffle deck
        
    def ReadDeck(self):print(self.DeckString)
        
    def ReadTopCard(self):print(self.Deck[len(self.Deck)-1].GetFrontofCard())
        
    def ReadBottomCard(self): print(self.Deck[0].GetFrontofCard())
        
    def CreateCard(self,Question:str,Answer:str,Category:str="?",Hint:str="?"):
        for i in self.Deck:
            if Question == i.GetAcronym() and Answer == i.GetAnswer():
                return False
        data = pd.read_csv('Culture_Tag.csv', encoding="ISO-8859-1")
        newrow=data.shape[0]+1
        data.loc[newrow,'ACR']=Question
        data.loc[newrow,'ANS']=Answer
        data.loc[newrow,'Category']=Category
        data.loc[newrow,'Hint']=Hint
        data.to_csv('Culture_Tag.csv',index=False)
        A=Card(Question,Answer,Category,Hint)
        self.Deck.append(A)
        self.DeckString.append(str(A))
        return True
        
