def scratchcards_2(file_path):
    file = open(file_path,'r')
    sum = 0
    i = 0
    winners = []
    for count, line in enumerate(file):
        pass
    cards = []
    for _ in range(count+1):
        cards.append(1)
    print(cards)
    file = open(file_path,'r')    
    for line in file:
            win = 0
            pars = line.split(":")
            set = pars[1].split("|")
            winners = set[0].split(" ")
            numbers = set[1].split(" ")
            while '' in numbers:
                numbers.remove('')
            while '' in winners:
                winners.remove('')
            for number in numbers:
                 if number in winners:
                      winners.remove(number)
                      win = win + 1    
            if numbers[len(numbers)-1].removesuffix('\n') in winners:
                 win = win + 1 
            for j in range(1,win+1):
                 cards[i+j] = cards[i+j] + cards[i]
            i = i + 1
            print(cards)  
    print(cards)
    for card in cards:
         sum = sum + card
    return sum       

def scratchcards(file_path):
    file = open(file_path,'r')
    sum = 0
    winners = []
    numbers = []
    for line in file:
            win = 0
            pars = line.split(":")
            set = pars[1].split("|")
            winners = set[0].split(" ")
            numbers = set[1].split(" ")
            while '' in numbers:
                numbers.remove('')
            while '' in winners:
                winners.remove('')
            print(winners)
            print(numbers)
            for number in numbers:
                 if number in winners:
                      winners.remove(number)
                      if win == 0:
                           win = 1
                      else:
                           win = win*2     
            if numbers[len(numbers)-1].removesuffix('\n') in winners:
                 if win == 0:
                    win = 1
                 else:
                    win = win*2
            sum = sum + win
    return sum       







if __name__ == '__main__':
    result = scratchcards_2('input.txt')
    print(result)
