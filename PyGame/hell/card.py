'''
Created on 2019/08/13

@author: Kai_Kudo
'''
import random
import time
from operator import attrgetter

class Card:
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
        self.rank = num if num!=1 else 14

class Hand:
    def __init__(self, cards):
        self.cards = sorted(cards, key=attrgetter('suit', 'rank'))
        self.cards.reverse()
    def play_card(self, num):
        return self.cards.pop(num)
    
class Field:
    def __init__(self, d_player, d_card):
        self.start = d_player
        self.field_card = [d_card] 
        self.winner = [d_player, d_card]
        self.dealer_suit = d_card.suit
        print_cards(self.field_card)
    def add_card(self, player, new_card):
        self.field_card.append(new_card)
        print_cards(self.field_card)
        if new_card.suit == self.dealer_suit and new_card.rank > self.winner[1].rank:
            self.winner = [player, new_card]

def setup():
    deck = []
    for i in range(52):
        if i//13==0:
            suit = 'd'
        elif i//13==1:
            suit = 'c'
        elif i//13==2:
            suit = 'h'
        elif i//13==3:
            suit = 's'
        deck.append(Card(suit, i%13+1))
    while True:
        try:
            player_num = int(input("player_num > "))
        except ValueError:
            continue
        if 2<=player_num<=10:
            break
    while True:
        try:
            game_way = int(input("one way:1, both ways:2 > "))
        except ValueError:
            continue
        if 1<=game_way<=3:
            break
    while True:
        try:
            me = int(input("Your turn > "))-1
        except ValueError:
            continue
        if 0<=me<player_num:
            break
    if game_way==1:
        game_num = list(range(1,52//player_num+1))
    elif game_way==2:
        game_num = list(range(1,52//player_num+1))+list(reversed(range(1,52//player_num+1)))
    else:
        game_num = list(range(5,52//player_num+1,10))
    player_points = [0]*player_num
    return deck, player_num, me, game_num, player_points
       
def eachturn_setup(dealer, my_hand, me):
    print_hand(my_hand)
    if dealer == me:
        print("dealer:You")
    else:
        print("dealer:Player{}".format(dealer+1))

def deal(deck, player_num, turn):
    players = []
    for i in range(player_num):
        players.append(Hand(deck[i*turn:(i+1)*turn]))
    return players
    
def print_hand(hand):
    print("Your hands:  ",end='')
    print_cards(hand.cards)

def print_cards(cards):
    for card in cards:
        print_suit(card.suit)
        print_num(card.num)
    print("")

def print_suit(suit):
    if suit == 'd':
        print("♦", end='')
    elif suit == 'c':
        print("♣", end='')
    elif suit == 'h':
        print("♥", end='')
    elif suit == 's':
        print("♠", end='')
        
def print_num(num):
    if num==1:
        print("A", end='  ')
    elif num==11:
        print("J", end='  ')
    elif num==12:
        print("Q", end='  ')
    elif num==13:
        print("K", end='  ')
    else:
        print(num, end='  ')
        
def pred(turn, dealer, player_num):
    player_pred = [0]*player_num
    hell_num = -1
    for player in range(dealer,player_num+dealer):
        player %= player_num
        if player == (dealer-1)%player_num:
            hell_num = turn-sum(player_pred)
            print("HELL:{}".format(hell_num))
        if player == me:
            while True:
                try:
                    pred = int(input("your_pred > "))
                except ValueError:
                    continue
                if 0<=pred<=turn:
                    if pred==hell_num:
                        print("Oh, it's HELL!!")
                    else:
                        break
            print("You predicted {}".format(pred))
        else:
            pred = random.randrange(turn)//3
            if pred==hell_num:
                print("Player{} predicted {}".format(player+1, pred))
                print("Oh, it's HELL!!")
                pred += 1
            print("Player{} predicted {}".format(player+1, pred))
        player_pred[player] = pred
    print(player_pred)
    return player_pred

def play(hand, player, this_suit, player_pred, player_amounts):
    if player == me:
        print_hand(hand)
        if len(hand.cards)==1:
            chosen_card = 0
        else:
            while True:
                try:
                    chosen_card = int(input("choose! > "))-1
                except ValueError:
                    print("prediction {}".format(player_pred))
                    print("now\t   {}".format(player_amounts))
                    print_hand(hand)
                    print_suit(this_suit)
                    continue
                if 0<=chosen_card<len(hand.cards):
                    #print([x for x in hand.cards if x.suit==this_suit])
                    if this_suit and len([x for x in hand.cards if x.suit==this_suit])!=0 and this_suit!=hand.cards[chosen_card].suit:
                        print("You must choose the same suit as dealer's!")
                    else:
                        break
            print("You chose: ", end='')
            print_suit(hand.cards[chosen_card].suit)
            print_num(hand.cards[chosen_card].num)
    else:
        if len(hand.cards)==1:
            chosen_card = 0
        else:
            while True:
                chosen_card = random.randrange(len(hand.cards))
                if not(this_suit and len([x for x in hand.cards if x.suit==this_suit])!=0 and this_suit!=hand.cards[chosen_card].suit):
                    break
    return hand.play_card(chosen_card)

def this_turn(turn, player_hands, dealer, player_num, player_amounts, player_pred):
    for phase in range(turn):
        print("\n<Phase {}>\n".format(phase+1))
        this_field = Field(dealer, play(player_hands[dealer], dealer, None, player_pred, player_amounts))
        print_suit(this_field.dealer_suit)
        time.sleep(1)
        for player in range(dealer+1, dealer+player_num):
            player %= player_num
            this_field.add_card(player, play(player_hands[player], player, this_field.dealer_suit, player_pred, player_amounts))
            time.sleep(1)
        if this_field.winner[0]==me:
            print("winner: You")
        else:
            print("winner: Player {}".format(this_field.winner[0]+1))
        player_amounts[this_field.winner[0]] += 1
        dealer = this_field.winner[0]
        del this_field
        time.sleep(2)
    return player_amounts

def culc_result(player_amounts, player_pred, player_num, me, player_points):
    print("result {}".format(player_amounts))
    print("prediction {}".format(player_pred))
    for player in range(player_num):
        if player==me:
            player_str = "You"
        else:
            player_str = "Player " + str(player+1)
        if player_amounts[player]==player_pred[player]:
            print("{} Guessed! +{}".format(player_str, 10+player_amounts[player]*3))
            player_points[player] += 10+player_amounts[player]*3
        elif player_pred[player]==0:
            print("{} failed as 0!! -3".format(player_str))
            player_points[player] -= 3
        else:
            print("{} failed. ±0".format(player_str))
        time.sleep(1)
    print("Points:{}\n".format(player_points))
    time.sleep(2)
    return player_points

def ranking(me, player_points, player_num):
    point_list = sorted(player_points)
    point_list.reverse()
    top_point = None
    for rank in range(player_num):
        top = player_points.index(point_list[rank])
        if player_points[top]!=top_point:
            now_rank = rank
        if top==me:
            top_str = 'You! '
        else:
            top_str = 'Player '+str(top+1)
        top_point = player_points[top]
        print('{:02}. {}\t{}'.format(now_rank+1, top_str, top_point))
        player_points[top] += 1

if __name__ == '__main__':
    deck, player_num, me, game_num, player_points = setup()
    for i, turn in enumerate(game_num):
        random.shuffle(deck)
        print("\n<<turn {}>>\n".format(i+1))
        dealer = i%player_num
        player_amounts = [0]*player_num
        player_hands = deal(deck, player_num, turn)
        eachturn_setup(dealer, player_hands[me], me)
        player_pred = pred(turn, dealer, player_num)
        time.sleep(1)
        player_amounts = this_turn(turn, player_hands, dealer, player_num, player_amounts, player_pred)
        player_points = culc_result(player_amounts, player_pred, player_num, me, player_points)
    ranking(me, player_points, player_num)
        