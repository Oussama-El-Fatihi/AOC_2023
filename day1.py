def string_to_digit(dig):
    if("one" in dig):
        return 1
    if("two" in dig):
        return 2
    if("three" in dig):
        return 3
    if("four" in dig):
        return 4
    if("five" in dig):
        return 5
    if "six" in dig:
        return 6
    if "seven" in dig:
        return 7
    if "eight" in dig:
        return 8
    if "nine" in dig:
        return 9
    return None

with open('input.txt', 'r') as file:
    sum = 0
    for line in file:
        temp = None
        dig = ""
        first = None
        last = None
        for character in line:
            dig = dig + character
            if (string_to_digit(dig) != None):
                if (first == None):
                    first = string_to_digit(dig)
                last = string_to_digit(dig)
                dig = character   
            else:
                if character.isdigit():
                    if (first == None):
                        first = int(character)
                    last = int(character)
                    dig = ""
        
        temp = first*10 + last
        print(temp)
        sum = sum + temp
    
    print(sum)            



    
