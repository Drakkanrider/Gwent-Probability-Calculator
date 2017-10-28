import json

class Deck:
  size = 0
  deckList = {}
  numSilvers = 0
  numGolds = 0
  numBronzes = 0
  
  #prints the contents of the deck to screen in the format:
  #Cardname #cards
  def printDeck(self):
    for key in self.deckList:
      print(key, end=" ")
      print(self.deckList[key])
      
  #fills a deck with cards from a file
  #TODO: make the deck use Card objects instead of just card names
  def load(self, file):
    with open(file) as f:
      for line in f:
        if line[-1] == '\n':
          deck.deckList[line[2:-1]] = line[0]
        else:
          deck.deckList[line[2:]] = line[0]
        deck.size = deck.size + int(line[0])
  
class Card:
  name = ''
  strength = 0
  group = ''
  rarity = ''
  loyalty = ''
  faction = ''
  position = ''
  types = []
  text = ''
  mechanics = []
  
  def fillCard(self, dict):
    self.name = dict['name']
    self.strength = dict['strength']
    self.group = dict['group']
    self.rarity = dict['rarity']
    self.loyalty = dict['loyalty']
    self.faction = dict['faction']
    self.position = dict['position']
    self.types = dict['types']
    self.text = dict['text']
    self.mechanics = dict['mechanics']
    
  


class Database:
  data = {}
  
  #function to fill database given the name of a json file as a string
  def fillDatabase(self, file):
     #opens the file
    with open('database.json') as f:    
      data = json.load(f)
    #creates a new Card object for each card in the JSON file, then stores it in the Database's data dict
    for dict in data:
      newCard = Card()
      newCard.fillCard(dict)
      cards.data[newCard.name] = newCard
  
#HYPERGEOMETRIC CALCULATIONS
def draw(numCards, deckSize):
  if deckSize <= 15:
    return 0
  prob = numCards / deckSize
  probNot = (1 - prob)
  return prob + probNot * draw(numCards, deckSize - 1)

def handDraw(numCards, deckSize):
  print(draw(numCards, deckSize))

#pedestrian file input
deck = Deck()
#deck.load('deck.txt')

cards = Database()
cards.fillDatabase
  
print(cards.data['Nature\'s Gift'].faction)