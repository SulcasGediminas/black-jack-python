import random

def calculate_hand_value(hand):
    hand_value = 0
    for card in hand:
        if card[0] == 'A':
            hand_value += 11
        elif card[0].isdigit():
            hand_value += int(card[0])
        else:
            hand_value += 10
    return hand_value

def draw_card():
    suit = random.choice(['♠', '♥', '♣', '♦'])
    rank = random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
    return rank + suit

def play_blackjack():
    print("Welcome to Blackjack!")
    money = 500
    min_bet = 1

    while money > 0:
        print(f"\nYou are starting with ${money}. Would you like to play a hand? ")
        play_hand = input().lower()
        if play_hand == "yes":
            print(f"Place your bet:")
            bet = float(input().strip())
            if bet < min_bet:
                print(f"The minimum bet is ${min_bet}.")
                continue
            player_hand = [draw_card(), draw_card()]
            dealer_hand = [draw_card(), draw_card()]
            print(f"\nYou are dealt: {', '.join(player_hand)}")
            print(f"The dealer is dealt: {dealer_hand[0]}, Unknown")

            while calculate_hand_value(player_hand) < 21:
                print(f"\nYou now have: {', '.join(player_hand)}")
                print("Would you like to hit or stay?")
                choice = input().lower()
                if choice == "hit":
                    player_hand.append(draw_card())
                elif choice == "stay":
                    break
                else:
                    print("That is not a valid option.")
            
            if calculate_hand_value(player_hand) > 21:
                print(f"\nYour hand value is over 21 and you lose ${bet} :(")
                money -= bet
            else:
                while calculate_hand_value(dealer_hand) < 17:
                    dealer_hand.append(draw_card())
                if calculate_hand_value(dealer_hand) > 21:
                    print(f"\nDealer busts with a hand value of {calculate_hand_value(dealer_hand)}.")
                    print(f"You win ${bet}!")
                    money += bet
                elif calculate_hand_value(dealer_hand) >= calculate_hand_value(player_hand):
                    print(f"\nDealer wins with a hand value of {calculate_hand_value(dealer_hand)}.")
                    print(f"You lose ${bet} :(")
                    money -= bet
                else:
                    print(f"\nYou win with a hand value of {calculate_hand_value(player_hand)}!")
                    print(f"You win ${bet}!")

play_blackjack()
# print(draw_card())