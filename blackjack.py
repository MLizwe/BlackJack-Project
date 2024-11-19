import random 

deck= [("2",2), ("3",3), ("4",4), ("5",5), ("6",6), ("7",7), ("8",8), ("9",9), ("10",10), ("J", 10), ("K",10), ("A", 11)

]*4

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

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
        total +=card[1]
        if card[0]=="A":
            aces +=1

    while total > 21 and aces > 0:
        total-=10
        aces -=1

    return total 

def main():
    player_hand, dealer_hand = deal_initial_cards(deck)

    player_score= calculate_score(player_hand)
    dealer_score= calculate_score(dealer_hand)

    print("Player's Hand:", player_hand)
    print("Player's Score:", player_score)
    print("Dealer's Hand:", dealer_hand)
    print("Dealer's Score:", dealer_score)

if __name__=="__main__":
    main()

