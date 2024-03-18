from cards import *
import random
class Player:
    def __init__(self, name):
        self.name=name
        self.hand=[]
def deck_init():
    for i in range(3):
        deck.append(defuse)
    for i in range(5):
        deck.append(nope)
    for i in range(5):
        deck.append(attack)
    for i in range(5):
        deck.append(future)
    for i in range(5):
        deck.append(reverse)
    for i in range(5):
        deck.append(skip)
    for i in range(5):
        deck.append(write)
    for i in range(5):
        deck.append(shuffle)
    random.shuffle(deck)
    for i in range(player_num):
        players[i].hand.append(defuse)
        for j in range(4):
            ncard=deck.pop()
            players[i].hand.append(ncard)
    print("发牌:成功")
    for i in range(player_num-1):
        deck.append(bombcat)
    random.shuffle(deck)
    print("牌堆初始化:成功")

if __name__=="__main__":
    player_num=3
    players=[Player(f"player{i}") for i in range(player_num)]
    player_survive=[i+1 for i in range(player_num)]
    deck=[]
    deck_init()

    
    while player_survive.__len__()>1:
        np=player_survive.pop(0)
        print(f"{players[np].name}的回合：")
        print("手牌：",end='')
        for i in range(players[np].hand.__len__()):
            print(i+1,players[np].hand[i].name,end=' ')
        print()
        print("输入卡片序号出牌，输入0结束回合并抽牌")
        card_num=int(input())
        turnend=False
        while card_num!=0 and turnend==False:
            print(f"{players[np].name}出牌{players[np].hand[card_num-1].name}")
            turnend=players[np].hand[card_num-1].func()
            card_num=int(input())
        if card_num==0:
            ncard=deck.pop()
            print('抽到了'+ncard.name)
            players[np].hand.append(ncard)
        player_survive.append(np)
