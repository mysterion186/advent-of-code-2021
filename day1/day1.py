def read_file(filename) : 
    file_list = []
    with open(filename,'r') as f :
        lines = f.readlines()
        for line in lines :
            file_list.append(int(line.replace('\n', '')))
    return file_list

file_list = read_file("day1.txt")

def day_1_v1(file_name):
    file_list = read_file(file_name)
    result_dict = {}
    # création du dictionnaire qui va contenir les valeurs 
    increasing_count = 0 
    for k in range(1,len(file_list)): 
        if file_list[k] > file_list[k-1]:
           increasing_count +=1
    # for key in result_dict : 
    #     if result_dict[key] == "increasing":
    #         increasing_count +=1 
    return increasing_count 

print(f"Pour la version 1 le résultat est {day_1_v1('day1.txt')}")

def day_1_v2(file_name):
    file_list = read_file(file_name)
    sliding_values = [] 
    # calcul de la moyenne glissante sur 3 valeurs 
    for k in range(1,len(file_list)-1):
        sliding_values.append(file_list[k-1]+file_list[k]+file_list[k+1])
    increasing_count = 0
    for k in range(1,len(sliding_values)):
        if sliding_values[k] > sliding_values[k-1] :
            increasing_count +=1 
    return increasing_count

print(f"Pour la version 2 le résultat est {day_1_v2('day1.txt')}")