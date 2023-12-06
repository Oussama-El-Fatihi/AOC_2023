def parsing_1(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    times = lines[0].split(":")[1].split(" ")
    distances = lines[1].split(":")[1].split(" ")
    
    while '' in times:
        times.remove('')
    while '' in distances:  
        distances.remove('')
    print(times, distances)         
    times = list(map(int, times))
    distances = list(map(int,  distances))
    print(times, distances)
    return times, distances

def parsing_2(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    times = lines[0].split(":")[1]
    distances = lines[1].split(":")[1]
    return int(times.replace(" ", "")), int(distances.replace(" ", ""))    

def wait_for_it_2(filepath):
    file = open(filepath, "r")
    parsing_2(filepath)
    combinations = 1
    ways = 0
    time, distance = parsing_2(filepath)
    for i in range(1,  time):
        if (time-i)*i > distance:
            ways += 1
        else:    
            if ways > 0:
                break
    print(ways)    
    combinations *= ways
    return combinations        

def wait_for_it_1(filepath):
    file = open(filepath, "r")
    parsing_2(filepath)
    combinations = 1
    times, distances = parsing_1(filepath)
    for j in range(0, len(times)):
        time = times[j]
        distance = distances[j]
        ways = 0
        for i in range(1,  time):
            print("(time-i)*i =", (time-i)*i, "distance =", distance)
            if (time-i)*i > distance:
                ways += 1
                print("check")
            else:    
                if ways > 0:
                    break
        print (ways)    
        combinations *= ways
    return combinations



if __name__ == '__main__':
    result = wait_for_it_1("input.txt")
    print(result)