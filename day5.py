import threading

def handler(signum, frame):
    print("Timeout !")
    raise TimeoutError("Timeout atteint")

def convert(line):
    numbers = []
    for number in line:
        numbers.append(int(number))
    return numbers

def lazy(seeds):
    seeds2 = []
    for i in range(0,len(seeds)-1):
        if i % 2 == 0:
            j = seeds[i+1]
            for k in range(0,j):
                seeds2.append(seeds[i]+k)
    return seeds2

def lazy(seeds):
    seeds2 = []
    for i in range(0,len(seeds)-1):
        if i % 2 == 0:
                seeds2.append(seeds[i])
    return seeds2


def seeds_fertilizers(filepath):
    file = open(filepath,'r')
    lines = file.readlines()
    seeds = (lines[0].split(":"))[1]
    seeds = seeds.split(" ")
    while '' in seeds:
        seeds.remove('')
    seeds = convert(seeds)
    seeds2 = compute(seeds)
    check = []
    for seed in seeds2:
        check.append(False)
    lines.remove(lines[0])    
    for line in lines:
        if "map" in line or not line.strip():
            save = line
            for i in range(0,len(check)):
                check[i] = False
            continue
        else:
            line = line.split(" ")
            conditions = convert(line)
            for i in range(0,len(seeds2)):
                seed = seeds2[i]
                if seed >= conditions[1] and seed <= conditions[2]+conditions[1] and not check[i]: 
                #if seed in range(conditions[1],conditions[2]+conditions[1]+1):
                    seeds2[i] = conditions[0] + (seed - conditions[1])
                    check[i] = True
    min = seeds2[0]
    for seed in seeds2:
        if seed < min:
            min = seed
    return min


def seeds_fertilizers_2(filepath):
    file = open(filepath,'r')
    lines = file.readlines()
    seeds = (lines[0].split(":"))[1]
    seeds = seeds.split(" ")
    while '' in seeds:
        seeds.remove('')
    seeds = convert(seeds)
    lines.remove(lines[0])
    min = None
    for i in range(0,len(seeds)-1):
        if i % 2 == 0:
            for k in range(0,seeds[i+1]):
                seed = seeds[i] + k
                check = False    
                for line in lines:
                    if "map" in line or not line.strip():
                        save = line
                        check = False
                        continue
                    else:
                        line = line.split(" ")
                        conditions = convert(line)
                        if seed >= conditions[1] and seed <= conditions[2]+conditions[1] and not check: 
                                seed = conditions[0] + (seed - conditions[1])
                                check = True
                if min == None:
                    min = seed
                else:
                    if min > seed:
                        min = seed
                              

    return min

def seeds_fertilizers_weird(filepath):
    file = open(filepath,'r')
    lines = file.readlines()
    seeds = (lines[0].split(":"))[1]
    seeds = seeds.split(" ")
    while '' in seeds:
        seeds.remove('')
    seeds = convert(seeds)
    lines.remove(lines[0])
    min = None
    for i in range(0,len(seeds)-1):
        if i % 2 == 0:
            seed = seeds[i]
            check = False    
            for line in lines:
                if "map" in line or not line.strip():
                    save = line
                    check = False
                    continue
                else:
                    line = line.split(" ")
                    conditions = convert(line)
                    if seed >= conditions[1] and seed <= conditions[2]+conditions[1] and not check: 
                            seed = conditions[0] + (seed - conditions[1])
                            check = True
            if min == None:
                min = seed
                while min in range(seeds[i],seeds[i]+seeds[i+1]):
                        seed = min
                        check = False    
                        for line in lines:
                            if "map" in line or not line.strip():
                                save = line
                                check = False
                                continue
                            else:
                                line = line.split(" ")
                                conditions = convert(line)
                                if seed >= conditions[1] and seed <= conditions[2]+conditions[1] and not check: 
                                        seed = conditions[0] + (seed - conditions[1])
                                        check = True
                        min = seed
            else:
                if min > seed:
                    min = seed
                    while min in range(seeds[i],seeds[i]+seeds[i+1]):
                        seed = min
                        check = False    
                        for line in lines:
                            if "map" in line or not line.strip():
                                save = line
                                check = False
                                continue
                            else:
                                line = line.split(" ")
                                conditions = convert(line)
                                if seed >= conditions[1] and seed <= conditions[2]+conditions[1] and not check: 
                                        seed = conditions[0] + (seed - conditions[1])
                                        check = True
                        min = seed
                                        

    return min

# Fonction pour exécuter le calcul avec un timeout
def run_with_timeout():
    global resultat
    try:
        resultat = seeds_fertilizers_2("input.txt")
        return resultat
    except TimeoutError:
        pass
    

# Définir le timeout en secondes
timeout = 6000

# Créer un thread pour le calcul
calc_thread = threading.Thread(target=run_with_timeout)

# Démarrer le thread
calc_thread.start()

# Attendre jusqu'à ce que le thread soit terminé ou jusqu'à ce que le timeout soit atteint
calc_thread.join(timeout)

if calc_thread.is_alive():
    print("Calcul interrompu après le timeout")
else:
    print("Calcul terminé avant le timeout")


if __name__ == '__main__':
    resultat = run_with_timeout()
    print(resultat)

   