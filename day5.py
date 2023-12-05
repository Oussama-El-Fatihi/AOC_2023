
def seeds_fertilizers(filepath):
    file = open(filepath,'r')
    lines= file.readlines()
    seeds = (lines[0].split(":"))[1]
    seeds = seeds.split(" ")
    max = 0
    while '' in seeds:
        seeds.remove('')
    for seed in seeds:
        if int(seed) > max:
            max = int(seed)
    seed_to_fertilizer = []
    for i in range(0,max):
        seed_to_fertilizer.append(i)
    print(seed_to_fertilizer)    






if __name__ == '__main__':
    result = seeds_fertilizers('input.txt')
    print(result)