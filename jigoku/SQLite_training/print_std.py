'''
Created on 2019/08/16
@author: Kai_Kudo
'''


def print_hand(hand):
    print("Your hands:  ", end='')
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
    if num == 1:
        print("A", end='  ')
    elif num == 11:
        print("J", end='  ')
    elif num == 12:
        print("Q", end='  ')
    elif num == 13:
        print("K", end='  ')
    else:
        print(num, end='  ')