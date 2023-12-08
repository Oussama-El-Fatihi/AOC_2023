
def haunted_wasteland(filename):
    file = open(filename, "r")
    lines = file.readlines()
    directions = list(lines[0])
    directions.pop()
    lines.remove(lines[0])
    lines.remove(lines[0])
    searched = None
    i = 0
    j = 0
    move = 0
    while True:
        print(move)
        line = lines[j]
        terms = line.split("=")[0]
        terms = terms.replace(" ", "").strip()
        left = line.split("=")[1].split(",")[0]
        right = line.split("=")[1].split(",")[1]
        right = right.replace(")", "").strip()
        left = left.replace("(", "").strip()
        if searched == None:
            if directions[i] == 'R':
                searched = right
            else:
                searched = left 
            i += 1
            move += 1
        else:
            if searched != terms:
                j += 1
                if j == len(lines):
                    print("loop terms")
                    j = 0
                continue
            if searched == terms:
                if directions[i] == 'R':
                    searched = right
                else:
                    searched = left
                i += 1
                move += 1
            if searched == "ZZZ":
                return move
        if i == len(directions):
            print("loop directions")
            i = 0
        j += 1
        if j == len(lines):
            print("loop termd")
            j = 0
    



if __name__ == '__main__':
    result = haunted_wasteland("input.txt")
    print(result)