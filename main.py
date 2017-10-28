DECK_SIZE = 25
NUM_OF_SHIT = 3

class Deck:
  size = 0
  deckList = {}


def draw(numCards, deckSize):
  if deckSize <= 15:
    return 0
  prob = numCards / deckSize
  probNot = (1 - prob)
  return prob + probNot * draw(numCards, deckSize - 1)

def handDraw(numCards, deckSize):
  print(draw(numCards, deckSize))
  


deck = Deck()
with open('deck.txt') as f:
  for line in f:
    if line[-1] == '\n':
      deck.deckList[line[2:-1]] = line[0]
    else:
      deck.deckList[line[2:]] = line[0]
    deck.size = deck.size + int(line[0])
    
for key in deck.deckList:
  print(key, end=" ")
  print(deck.deckList[key])
  
print (deck.size)
