############### Blackjack Project #####################

import random
from replit import clear
from art import logo

def play_game():
    # SET UP GAME ESTABLISH CARD VALUES... ACE CAN BE 1 OR 11
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # CREATE EMPTY LISTS FOR USER AND COMPUTER/DEALER CARDS
    user_cards = []
    computer_cards = []

    keep_playing = True

    # CREATE FUNCTION TO DISTRIBUTE INITIAL CARDS TO PLAYER AND DEALER
    def deal_card():
        return random.choice(cards)

    # EACH PLAYER GETS TWO CARDS TO BEGIN THE GAME
    while len(user_cards) < 2:
        user_cards.append(deal_card())

    while len(computer_cards) < 2:
        computer_cards.append(deal_card())

    # CREATE FUNCTION TO CALCULATE SCORE TO DETERMINE IF THERE IS A BLACKJACK WINNER
    def calculate_score(cards_in_hand):
        if len(cards_in_hand) == 2 and sum(cards_in_hand) == 21: # THIS INDICATES BLACKJACK
            return 0 # returning 0 as a score will end the game (you'll see in the following steps)
        elif sum(cards_in_hand) > 21 and 11 in cards_in_hand: # THIS INDICATES HAVING AN ACE AND CHANGING ITS VALUE TO PREVENT BUSTING OVER 21
            cards_in_hand.remove(11)
            cards_in_hand.append(1)
            return sum(cards_in_hand)
        else:
            return sum(cards_in_hand) # IF NOT BLACKJACK OR BUSTING WITH AN ACE IN YOUR HAND, THEN JUST RETURN YOUR SCORE AND ASK THE USER IF THE WANT ANOTHER CARD

    while keep_playing:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"You're cards are {user_cards}. Current score: {user_score}.")
        print(f"Dealer's first card is {computer_cards[0]}.")
        if user_score == 0 or computer_score == 0 or user_score > 21: # IF PLAYER BLACKJACK OR DEALER BLACKJACK OR BUST, END THE GAME
            keep_playing = False
        else:
            user_answer = input("Do you want another card? (Y/N): ").upper()
            if user_answer == "Y":
                user_cards.append(deal_card())
            else:
                keep_playing = False # DID NOT INCLUDE THE COMPUTER'S/DEALER'S TURN BECAUSE DEALER ALWAYS PLAYS AFTER PLAYER IS DONE (SO AS YOU KEEP PLAYING HE WAITS)

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards) # AFTER YOUR TURN IS DONE, LET DEALER PLAY AND CALCULATE THEIR SCORE BEFORE YOU COMPARE WITH PLAYER SCORE

    def compare(player_score, dealer_score):
        if player_score > 21:
            return "Bust! You lose."
        elif player_score == dealer_score:
            return "Draw!"
        elif player_score == 0:
            return "Blackjack! You win!"
        elif computer_score == 0:
            return "Dealer Blackjack. You lose."
        elif player_score > dealer_score:
            return "You win!"
        else:
            return "Dealer wins."

    print(f"Your final hand: {user_cards}. Final score: {user_score}.")
    print(f"Dealer's final hand: {computer_cards}. Final score: {computer_score}.")
    print(compare(user_score, computer_score))

while input("Do you want to play Blackjack? (Y/N): ").upper() == "Y":
    clear()
    play_game()

############### Blackjack Project Replit Code #####################

# import random
# from replit import clear
# from art import logo
#
#
# def play_game():
#     print(logo)
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     user_cards = []
#     comp_cards = []
#     keep_playing = True
#
#     def deal_card():
#         return random.choice(cards)
#
#     while len(user_cards) < 2:
#         user_cards.append(deal_card())
#
#     while len(comp_cards) < 2:
#         comp_cards.append(deal_card())
#
#     def calculate_score(cards):
#         if len(cards) == 2 and sum(cards) == 21:
#             return 0
#         elif sum(cards) > 21 and 11 in cards:
#             cards.remove(11)
#             cards.append(1)
#             return sum(cards)
#         else:
#             return sum(cards)
#
#     while keep_playing == True:
#         user_score = calculate_score(user_cards)
#         comp_score = calculate_score(comp_cards)
#         print(f"Your cards are {user_cards}. Current score: {user_score}.")
#         print(f"Dealer's first card is {comp_cards[0]}.")
#         if user_score == 0 or comp_score == 0 or user_score > 21:
#             keep_playing = False
#         else:
#             hit = input("Do you want to draw another card? Type 'Y' or 'N': ").lower()
#             if hit == 'y':
#                 user_cards.append(deal_card())
#             else:
#                 keep_playing = False
#
#     while comp_score < 17 and comp_score != 0:
#         comp_cards.append(deal_card())
#         comp_score = calculate_score(comp_cards)
#
#     def compare(user_score, comp_score):
#         if user_score == comp_score:
#             return "It's a draw."
#         elif comp_score == 0:
#             return "Dealer has blackjack. You lose."
#         elif user_score == 0:
#             return "Blackjack! You win."
#         elif user_score > 21:
#             return "Bust. You lose."
#         elif comp_score > 21:
#             return "Dealer busted. You win."
#         elif user_score > comp_score:
#             return "Higher score! You win."
#         else:
#             return "Lower score. You lose."
#
#     print(f"Your final hand: {user_cards}. Final score: {user_score}.")
#     print(f"Dealer's final hand: {comp_cards}. Dealer's final score: {comp_score}.")
#     print(compare(user_score, comp_score))
#
#
# while input("Do you want to play Blackjack? Type 'Y' or 'N': ").lower() == 'y':
#     clear()
#     play_game()