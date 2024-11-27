import random 
from db import read_player_money, write_player_money

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = [
    ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6),
    ("7", 7), ("8", 8), ("9", 9), ("10", 10),
    ("J", 10), ("Q", 10), ("K", 10), ("A", 11)
]

deck = [[rank[0], suit, rank[1]] for suit in suits for rank in ranks] * 4  # Multiply by 4 for a full deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def deal_initial_cards(deck):
    player_hand=[deck.pop(), deck.pop()]
    dealer_hand=[deck.pop(), deck.pop()]
    return player_hand, dealer_hand

def draw_card(deck, hand):
    hand.append(deck.pop())

def calculate_score(hand):
    total=0
    aces=0
    
    for card in hand:
        total +=card[2]
        if card[0]=="A":
            aces +=1

    while total > 21 and aces > 0:
        total-=10
        aces -=1

    return total 

def display_hand(hand):
    return ", ".join([f"{card[0]} of {card[1]}" for card in hand])

def get_bet(player_money):
    while True:
        try:
            bet = float(input("Enter your bet amount: "))
            if bet < 5:
                print("Minimum bet is $5.")
            elif bet > 1000:
                print("Maximum bet is $1,000.")
            elif bet > player_money:
                print("You cannot bet more than your current money.")
            else:
                return bet
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    player_money = read_player_money()
    while player_money >= 5:
        if player_money < 5:
            print("You're out of money! Buy more chips to keep playing.")
            break

        shuffle_deck(deck)

        print("BLACKJACK!")
        print("Blackjack payout is 3:2")
        print()
        print(f"Money: ${player_money:.2f}")

        bet = get_bet(player_money)
        player_hand, dealer_hand = deal_initial_cards(deck)

        print("DEALER'S SHOW CARD:")
        print(f"{dealer_hand [0][0]} of {dealer_hand[0][1]}")
        
        print("YOUR CARDS: ")
        print(display_hand(player_hand))

        
        while True:
            action = input("Hit or stand?: ").lower()
            if action == "hit":
                draw_card(deck, player_hand)
                print("YOUR CARDS: ")
                print()
                print(display_hand(player_hand))
                if calculate_score(player_hand) > 21:
                    print("You Busted!")
                    write_player_money(player_money)
                    player_money-=bet
                    print(f"You lose ${bet:.2f}!")
                    break
            elif action=="stand":
                break
            else:
                print("Invalid Input. Please enter 'hit' or 'stand'.")
                    
        if calculate_score(player_hand) <=21:
            print("DEALER'S TURN ")
            while calculate_score(dealer_hand) < 17:
                draw_card(deck, dealer_hand)

            print("DEALER'S CARDS:")
            print(display_hand(dealer_hand))

                
            player_score = calculate_score(player_hand)
            dealer_score = calculate_score(dealer_hand)


            print(f"Your Points: {player_score}")
            print(f"Dealer's Points: {dealer_score}")



            if dealer_score > 21 or player_score>dealer_score:
                if player_score == 21 and len (player_hand) ==2:
                    winnings=round(bet*1.5, 2)
                    print(f"Blackjacck! You win ${winnings:.2f}!")
                    player_money += winnings
                    write_player_money(player_money)
                else:
                    print(f"You win ${bet:.2f}!")
                    player_money += bet
                    write_player_money(player_money)
            elif player_score < dealer_score:
                print("You Lose!")
                player_money -= bet
                write_player_money(player_money)
            else:
                print("It is a tie!")

        print(f"Money: ${player_money:.2f}")

        play_again= input ("Play again? (y/n): ").lower()
        if play_again !="y":
            print("Come back soon!")
            break

    if player_money < 5:
        print("You're out of money! Buy more chips to keep playing.")
    print("Bye!")

        


    player_score= calculate_score(player_hand)
    dealer_score= calculate_score(dealer_hand)

   
if __name__=="__main__":
    main()


