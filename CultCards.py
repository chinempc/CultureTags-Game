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
        self.Acronym="?"
        self.Answer="?"
        self.Category="?"
        self.Hint="?"
        
    def  __init__(self,Acr,Ans,Cat,Hint): # setting the content of the card in this constructor
        self.Acronym=Acr
        self.Answer=Ans
        self.Category=Cat
        self.Hint=Hint

    def __str__(self): #when class used as a print or converted to string, it will print Acronym, Answers, Category, and Hint
        return (str(self.Acronym) +" , " + str(self.Answer) +", " + str(self.Category)+ ", "+ str(self.Hint))
    def GetAcronym(self): return self.Acronym #Returns Acronym
    def GetAnswer(self): return self.Answer #Returns Answer
    def GetCategory(self): return self.Category #Returns Category
    def GetHint(self):return self.Hint #Returns Hint

class Deck: #This Deck will get the card details from the Culture_Tag.csv, convert them into card classes and store them in
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
        
    def ReadTopCard(self):print(self.Deck[len(self.Deck)-1])
        
    def ReadBottomCard(self): print(self.Deck[0])
        
    def CreateCard(self,Question:str,Answer:str,Category:str="?",Hint:str="?"):
        
        data = pd.read_csv('Culture_Tag.csv', encoding="ISO-8859-1")
        newrow=data.shape[0]+1
        
        data.loc[newrow,'ACR']=Question
        data.loc[newrow,'ANS']=Answer
        data.loc[newrow,'Category']=Category
        data.loc[newrow,'Hint']=Hint
        data.to_csv('Test.csv',index=False)
        A=Card(Question,Answer,Category,Hint)
        
        self.Deck.append(A)
        self.DeckString.append(str(A))
        
        
