# standard deck of playing cards, with the Kings removed (48 Cards)
import os
import random

#Player1_score = 0
#Player2_score = 0 

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
# Gameplay
def print_hand(player_num, hand):
    print("Player " + str(player_num) + " hand:")
    for i in range(len(hand)):
        card = hand[i]
        print(str(i + 1) + ": " + card["rank"] + " of " + card["suit"])
#Playing one round
def play_round(leader, p1_hand, p2_hand):
    print_hand(1, p1_hand)
    print_hand(2, p2_hand)

    if leader == 1:
        print("Player 1 goes first.")
        lead_index = int(input("Player 1 - choose a card number to play: ")) - 1
        lead_card = p1_hand.pop(lead_index)

        print("Player 2 - follow suit if you can.")
        follow_index = int(input("Choose a card number to play: ")) - 1
        follow_card = p2_hand.pop(follow_index)
    else:
        print("Player 2 goes first.")
        lead_index = int(input("Player 2 - choose a card number to play: ")) - 1
        lead_card = p2_hand.pop(lead_index)

        print("Player 1 - follow suit if you can.")
        follow_index = int(input("Choose a card number to play: ")) - 1
        follow_card = p1_hand.pop(follow_index)

    print("Lead card: " + lead_card["rank"] + " of " + lead_card["suit"])
    print("Follow card: " + follow_card["rank"] + " of " + follow_card["suit"])

    # Decide winner
    if follow_card["suit"] == lead_card["suit"]:
        if follow_card["value"] > lead_card["value"]:
            winner = 2 if leader == 1 else 1
        else:
            winner = leader
    else:
        winner = leader

    print("Player " + str(winner) + " wins the round.")
    return winner