# standard deck of playing cards, with the Kings removed (48 Cards)
import os
import random

#build cards 
# Define card suits and ranks (excluding Kings)
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = [("Ace", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5),
         ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10),
         ("Jack", 11), ("Queen", 12)]
# Build the deck
def build_deck():
    deck = []
    for suit in suits:
        for rank, value in ranks:
            deck.append({"suit": suit, "rank": rank, "value": value})
    return deck

# Shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Deal cards to players
def deal_cards(deck, num_cards):
    hand = deck[:num_cards]
    del deck[:num_cards]
    return hand

# Reveal the top card
def reveal_top_card(deck):
    if deck:
        card = deck.pop(0)
        print(f"Revealed card: {card['rank']} of {card['suit']}")
        return card
    else:
        print("No more cards to reveal.")
        return None

# Main block for testing
if __name__ == "__main__":
    deck = build_deck()
    shuffle_deck(deck)

    print(f"Deck size: {len(deck)}")
    player1_hand = deal_cards(deck, 8)
    player2_hand = deal_cards(deck, 8)

    print("Player 1 hand:", player1_hand)
    print("Player 2 hand:", player2_hand)
    print(f"Remaining cards in deck: {len(deck)}")

    reveal_top_card(deck)
