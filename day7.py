from enum import Enum

class Type(Enum):
    high = 0
    one = 1
    two = 2
    three = 3
    full = 4
    four = 5
    five = 6
class CamelCard:
    def __init__(self):
        self.hand = []
        self.bid = 0
        self.Type = Type.high
def get_rank(char):
    ranks = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    if char in ranks:
        return ranks.index(char)
    else:
        return None
def get_rank2(char):
    ranks = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
    if char in ranks:
        return ranks.index(char)
    else:
        return None
            
def type(camelCard):
    hand = camelCard.hand
    pattern = []
    for i in range(0,len(hand)):
        it = 1
        if any(hand[i] == element[0] for element in pattern):
            continue
        elif i == len(hand)-1:
            pattern.append((hand[i],it))
            break
        for j in range(i+1,len(hand)):
            if hand[i] == hand[j]:
                it += 1
        pattern.append((hand[i],it))
    pattern.sort(key=lambda x: x[1], reverse=True)
    if pattern[0][1] == 5:
        camelCard.Type = Type.five
    elif pattern[0][1] == 4:                
        camelCard.Type = Type.four
    elif pattern[0][1] == 3 and pattern[1][1] == 2:
        camelCard.Type = Type.full
    elif pattern[0][1] == 3:
        camelCard.Type = Type.three
    elif pattern[0][1] == 2 and pattern[1][1] == 2:
        camelCard.Type = Type.two
    elif pattern[0][1] == 2 and pattern[1][1] == 1:
        camelCard.Type = Type.one
    else:
        camelCard.Type = Type.high
    return camelCard

def type_2(camelCard):
    hand = camelCard.hand
    pattern = []
    joker = 0
    for i in range(0,len(hand)):
        it = 1
        if hand[i] == 'J':
            joker += 1
            continue
        if any(hand[i] == element[0] for element in pattern):
            continue
        elif i == len(hand)-1 and hand[i]:
            pattern.append((hand[i],it))
            break
        for j in range(i+1,len(hand)):
            if hand[i] == hand[j]:
                it += 1   
        pattern.append((hand[i],it))
    if pattern == []:
        camelCard.Type = Type.five
        return camelCard    
    pattern.sort(key=lambda x: x[1], reverse=True)
    
    if pattern[0][1]+joker == 5:
        camelCard.Type = Type.five
    elif pattern[0][1]+joker == 4:                
        camelCard.Type = Type.four
    elif pattern[0][1]+joker == 3 and pattern[1][1] == 2:
        camelCard.Type = Type.full
    elif pattern[0][1]+joker == 3:
        camelCard.Type = Type.three
    elif pattern[0][1]+joker == 2 and pattern[1][1] == 2:
        camelCard.Type = Type.two
    elif pattern[0][1]+joker == 2 and pattern[1][1] == 1:
        camelCard.Type = Type.one
    else:
        camelCard.Type = Type.high
    return camelCard            

def camel_cards(filename):
    file = open(filename, "r")
    lines = file.readlines()
    cards = []
    for line in lines:
        line = line.split(" ")
        card = CamelCard()
        card.hand = list(line[0])
        card.bid = int(line[1])
        print(card.hand)
        card = type_2(card)
        if cards == []:
            cards.append(card)
        else:
            check = False
            for i in range(0,len(cards)):
                if card.Type.value > cards[i].Type.value:
                    cards.insert(i,card)
                    check = True
                    break
                elif card.Type.value == cards[i].Type.value:
                    for j in range(0,len(card.hand)):
                        if get_rank2(card.hand[j]) < get_rank2(cards[i].hand[j]):
                            cards.insert(i,card)
                            check = True
                            break
                        if get_rank2(card.hand[j]) > get_rank2(cards[i].hand[j]):
                            break
                if check:
                    break
            if not check:
                cards.append(card)
    total = 0
    for card in cards:
        print(card.hand,card.bid,card.Type)
    for i in range(0,len(cards)):
        total += cards[i].bid*(len(cards)-i)
   
    print(len(cards))
    return total
        
        












if __name__ == '__main__':
    result = camel_cards("input.txt")
    print(result)