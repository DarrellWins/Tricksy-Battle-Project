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
# Gameplay
# Print hand
def print_hand(player_num, hand):
    print("Player " + str(player_num) + " hand:")
    for i in range(len(hand)):
        card = hand[i]
        print(str(i + 1) + ": " + card["rank"] + " of " + card["suit"])

# Play one round
def play_round(leader, p1_hand, p2_hand):
    print_hand(1, p1_hand)
    print_hand(2, p2_hand)

    if leader == 1:
        print("Player 1 goes first.")
        lead_index = int(input("Player 1 - choose a card number to play: ")) - 1
        lead_card = p1_hand.pop(lead_index)

        print("Player 2 - choose a card to follow.")
        follow_index = int(input("Player 2 - choose a card number to play: ")) - 1
        follow_card = p2_hand.pop(follow_index)
    else:
        print("Player 2 goes first.")
        lead_index = int(input("Player 2 - choose a card number to play: ")) - 1
        lead_card = p2_hand.pop(lead_index)

        print("Player 1 - choose a card to follow.")
        follow_index = int(input("Player 1 - choose a card number to play: ")) - 1
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

# Main loop version of Tricksy Battle
def play_game():
    deck = build_deck()
    shuffle_deck(deck)

    player1_hand = deal_cards(deck, 8)
    player2_hand = deal_cards(deck, 8)
    player1_score = 0
    player2_score = 0
    leader = random.choice([1, 2])
    round_num = 1

    while round_num <= 16:
        print("\n=== Round " + str(round_num) + " ===")
        print("Score -> Player 1: " + str(player1_score) + " | Player 2: " + str(player2_score))

        winner = play_round(leader, player1_hand, player2_hand)

        if winner == 1:
            player1_score += 1
            leader = 1
        else:
            player2_score += 1
            leader = 2

        reveal_top_card(deck)
        round_num += 1

        # Deal 4 more cards if needed
        if len(player1_hand) == 4 and len(player2_hand) == 4 and len(deck) >= 8:
            player1_hand += deal_cards(deck, 4)
            player2_hand += deal_cards(deck, 4)

        # Early end if one player hits 9 and other has at least 1
        if (player1_score >= 9 and player2_score >= 1) or (player2_score >= 9 and player1_score >= 1):
            print("Game ends early — no way for the other player to win.")
            break

    print("\n=== Final Score ===")
    print("Player 1: " + str(player1_score))
    print("Player 2: " + str(player2_score))

    if player1_score == 0:
        print("Player 2 shot the moon and wins with 17 points!")
    elif player2_score == 0:
        print("Player 1 shot the moon and wins with 17 points!")
    elif player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Run game
play_game()
