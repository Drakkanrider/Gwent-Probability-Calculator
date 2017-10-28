class Deck:
  size = 0
  deckList = {}
  numSilvers = 0
  numGolds = 0
  numBronzes = 0
  def printDeck(self):
    for key in self.deckList:
      print(key, end=" ")
      print(self.deckList[key])
      
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
deck.load('deck.txt')
  
deck.printDeck()
