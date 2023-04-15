import random
import itertools

deck = list(itertools.product(range(1, 14), [
            "Heart", "Diamod", "Club", "Spade"]))

# The Deck
# print(deck)

# Shuffle
random.shuffle(deck)

# Drawing the cards
print("You have:")
for card in range(4):
    # print(card)
    print(deck[card][0], "of", deck[card][1])
