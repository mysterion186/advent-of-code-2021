def read_file(filename) :
    file_list = []
    with open(filename,'r') as f :
        lines = f.readlines()
        for line in lines :
            file_list.append(line.replace('\n', ''))
    return file_list

file_list = read_file("day2.txt")
for line in file_list[0:5]:
        action = line.split(' ')[0]
        value = int(line.split(' ')[1])
        print(action, value)

# up -> decreases 
# down -> increases 

def day_v1(filename):
    file_list = read_file(filename)
    x,y = 0,0 # initilisation des coordonnées en 0,0 
    for line in file_list :
        action = line.split(' ')[0]
        value = int(line.split(' ')[1])
        if action == "forward" :
            x += value 
        elif action == "up":
            y-=value
        else :
            y+= value
    return x*y
print(f"La réponse pour la version 1 est {day_v1('day2.txt')}")


def day_v2(filename):
    file_list = read_file(filename)
    x,y,aim = 0,0,0 # initilisation des coordonnées en 0,0 
    for line in file_list :
        action = line.split(' ')[0]
        value = int(line.split(' ')[1])
        if action == "forward" :
            x += value 
            y += value*aim
        elif action == "up":
            aim-=value
        else :
            aim+= value
    return x*y  
print(f"La réponse pour la version 2 est {day_v2('day2.txt')}")