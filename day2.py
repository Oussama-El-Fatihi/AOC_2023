def cube_conundrum(file_path):
    file = open('day2_text.txt','r')
    sum = 0
    r = 12
    g = 13
    b = 14
    for line in file:
            pars = line.split(":")
            temp_r = 0
            temp_g = 0
            temp_b = 0
            game_id = pars[0].removeprefix("Game")
            set = pars[1].split(";")
            for i in set:
                 cube = i.split(",")
                 for j in cube:
                      t = j.split(" ")
                      print(t)
                      if t[2] == "green":
                           temp_g = int(t[1])
                      else:
                           if t[2] == "red":
                                temp_r = int(t[1])
                           else:
                                if t[2] == "blue":
                                    temp_b = int(t[1])
                 if temp_b > b or temp_g > g or temp_r > r:
                    game_id = 0
                    break
            sum = sum + int(game_id)

    return sum        
                 
                    
def cube_conundrum2(file_path):
    file = open(file_path,'r')
    sum = 0
    r = 0
    g = 0
    b = 0
    for line in file:
            pars = line.split(":")
            temp_r = 0
            power = 1
            temp_g = 0
            temp_b = 0
            r = 0
            g = 0
            b = 0
            #print(sum)
            set = pars[1].split(";")
            for i in set:
                 cube = i.split(",")
                 for j in cube:
                      t = j.split(" ")
                      if "green" in t[2] :
                           temp_g = int(t[1])
                      else:
                           if "red" in t[2] :
                                temp_r = int(t[1])
                           else:
                                if "blue" in t[2] :
                                    temp_b = int(t[1])
                 if temp_b > b:
                    b = temp_b
                 if temp_g > g:
                    g = temp_g
                 if temp_r > r:
                      r = temp_r
            power = power * r * g *b
            sum = sum + power

    return sum    
        


    








if __name__ == '__main__':
    result2 = cube_conundrum2('input.txt')
    print(result2)