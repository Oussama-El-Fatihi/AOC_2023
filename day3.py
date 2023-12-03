class Gear:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.num = 0
        self.size = 0

def check_engine(number,i,lines,j):
    it = len(str(number))
    line = lines[i]
    if j - it >= 0 and line[j-it] != ".":
        return True
    if j+1 < len(line) and  line[j+1] not in  {".","\n"}:
        return True
    if i > 0:
        prvs_line = lines[i-1]
        for tem in range(0,it):
            character = prvs_line[j-tem]
            #print(character)
            if character not in  {".","\n"} and not character.isdigit() :
                return True
        
        if j+1 < len(prvs_line) and prvs_line[j+1] not in  {".","\n"} and not prvs_line[j+1].isdigit():
            print(number)
            return True
        
        if (j-it) >=0 and prvs_line[j-it] not in  {".","\n"} and not prvs_line[j-it].isdigit():
            print(number)
            return True
    
    if i < len(lines) - 1:
        nxt_line = lines[i+1]
        for tem in range(0,it):
            character = nxt_line[j-tem]
            #print(character)
            if character not in  {".","\n"} and not character.isdigit() :
                return True
        
        if j+1 < len(nxt_line) and nxt_line[j+1] not in  {".","\n"} and not nxt_line[j+1].isdigit():
            print(number)
            return True
        
        if (j-it) >=0 and nxt_line[j-it] not in  {".","\n"} and not nxt_line[j-it].isdigit():
            print(number)
            return True  
    return False    

def check_engine_2(number,i,lines,j):
    it = len(str(number))
    line = lines[i]
    gear_obj = Gear()
    gear_obj.size = 1
    gear_obj.num = number
    if j - it >= 0 and line[j-it] == "*":
        gear_obj.i = i
        gear_obj.j = j-it
        return gear_obj
    
    if j+1 < len(line) and  line[j+1] == "*":
        gear_obj.i = i
        gear_obj.j = j+1
        return gear_obj
    
    if i > 0:
        prvs_line = lines[i-1]
        for tem in range(0,it):
            character = prvs_line[j-tem]
            if character == "*" :
                gear_obj.i = i-1
                gear_obj.j = j-tem
                return gear_obj
        
        if j+1 < len(prvs_line) and prvs_line[j+1] == "*":
            gear_obj.i = i-1
            gear_obj.j = j+1
            return gear_obj
        
        if (j-it) >=0 and prvs_line[j-it] == "*":
            gear_obj.i = i-1
            gear_obj.j = j-it
            return gear_obj
    
    if i < len(lines) - 1:
        nxt_line = lines[i+1]
        for tem in range(0,it):
            character = nxt_line[j-tem]
            if character == "*":
                gear_obj.i = i+1
                gear_obj.j = j-tem
                return gear_obj
        
        if j+1 < len(nxt_line) and nxt_line[j+1] == "*":
            gear_obj.i = i+1
            gear_obj.j = j+1
            return gear_obj
        
        if (j-it) >=0 and nxt_line[j-it] == "*":
            gear_obj.i = i+1
            gear_obj.j = j-it
            return gear_obj  
    return None    


def geer_ratios(file_path):
    file = open(file_path,"r")
    lines = file.readlines()
    res = 0
    gears = []
    for i in range(0,len(lines)):
        line = lines[i]
        num = 0
        for j in range(0,len(line)):
            character = line[j]
            if character.isdigit():
                num = num*10 + int(character)
            else:                
                if num != 0:
                    gear_obj = None
                    gear_obj = check_engine_2(num,i,lines,j-1)
                    if gear_obj != None :
                        found = False 
                        for gear in gears:
                            if gear.i == gear_obj.i and gear.j == gear_obj.j:
                                found = True
                                gear.num = num * gear.num
                                gear.size = gear.size + 1
                                break
                        if not found:
                            gears.append(gear_obj)
                    num = 0
                else :
                    num = 0
    print(len(gears))
    for gear in gears:
        print(f"i: {gear.i}, j: {gear.j}, num: {gear.num}, size: {gear.size}")
        if gear.size > 1:
            res = res + gear.num
            
    return res                        








if __name__ == '__main__':
    print(geer_ratios("input.txt"))