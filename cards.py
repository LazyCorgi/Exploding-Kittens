class Card:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def func(self):
        return False

bombcat=Card("炸弹",0)
defuse=Card("拆弹",1)
nope=Card("不行",2)
attack=Card("攻击",2)
future=Card("预见未来",2)
reverse=Card("反转",2)
skip=Card("跳过",2)
write=Card("改写未来",2)
shuffle=Card("洗牌",2)

# card=[
#     bombcat,defuse,nope,attack,future,reverse,skip,write,shuffle
# ]