class Node:
        def __init__(self):
            self.term = ""
            self.left = ""
            self.right = ""


def haunted_wasteland(filename):
    file = open(filename, "r")
    lines = file.readlines()
    directions = list(lines[0])
    directions.pop()
    lines.remove(lines[0])
    lines.remove(lines[0])
    searched = None
    i = 0
    move = 0
    inputs = []
    for line in lines:
        node = Node()
        terms = line.split("=")[0]
        node.terms = terms.replace(" ", "").strip()
        left = line.split("=")[1].split(",")[0]
        right = line.split("=")[1].split(",")[1]
        node.right = right.replace(")", "").strip()
        node.left = left.replace("(", "").strip()
        inputs.append(node)
    
    while True:
        if i == len(directions):
            i = 0
        if searched == None:
            if directions[i] == 'R':
                searched = inputs[0].right
            else:
                searched = inputs[0].right 
            i += 1
            move += 1
        else:
            for element in inputs:
                if searched == element.terms:
                    if searched == "ZZZ":
                        return move
                    if directions[i] == 'R':
                        searched = element.right
                    else:
                        searched = element.left
                    i += 1
                    move += 1
                    break



if __name__ == '__main__':
    result = haunted_wasteland("input.txt")
    print(result)