def read_file(filename) : 
    file_list = []
    with open(filename,'r') as f :
        lines = f.readlines()
        for line in lines :
            file_list.append(line.replace('\n', ''))
    return file_list


file_list = read_file('day3.txt')


def v1(filename):
    file_list = read_file(filename)
    bit_length = len(file_list[0]) # taille d'un bit 
    #print(bit_length)
    gamma,epsilon = "",""
    for k in range(bit_length):
        one_value = 0
        zero_value = 0
        for bit in file_list:
            #print(bit)
            #print(bit[k])
            if bit[k]=="1":
                one_value += 1 
            else : 
                zero_value += 1

        # création du bit 
        if one_value> zero_value:
            gamma +="1"
            epsilon +="0"
        else : 
            gamma += "0"         
            epsilon +="1"
    return int(gamma,2)*int(epsilon,2)

# this function will remove unwanted bit from the working list 
def remove_bit(file_list,value_to_keep,indice):
    new_list = []
    for line in file_list:
        if line[indice]==value_to_keep:
            new_list.append(line)
    return new_list


test = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
# print(file_list[0:10])
# file_list = remove_bit(file_list,"1")
# print()
# print(file_list[0:10])

def find_oxygen(filename):
    file_list = read_file(filename)
    # file_list = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    bit_length = len(file_list[0]) # taille d'un bit 
    #print(bit_length)
    for k in range(bit_length):
        one_value =0
        zero_value = 0
        for bit in file_list:
            if bit[k]=="1":
                one_value += 1 
            else : 
                zero_value += 1
        if one_value >= zero_value : 
            file_list = remove_bit(file_list,"1",k) 
        elif zero_value>one_value : 
            file_list = remove_bit(file_list,"0",k)
        
        if len(file_list)==1 : 
            break 
    return file_list

    
def find_co2(filename):
    file_list = read_file(filename)
    # file_list = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    bit_length = len(file_list[0])
    for k in range(bit_length):
        one_value = 0 
        zero_value = 0
        for bit in file_list: 
            if bit[k]=="1":
                one_value += 1 
            else : 
                zero_value += 1

        if zero_value<=one_value: 
            file_list = remove_bit(file_list,"0",k)
        elif zero_value>one_value :
            file_list = remove_bit(file_list,"1",k)
        if len(file_list)==1 : 
                break 
    return file_list





print("oxygen",find_oxygen("day3.txt"))
print("co2",find_co2("day3.txt"))

def v2(filename):
    oxy = int(find_oxygen(filename)[0],2) 
    co2 = int(find_co2(filename)[0],2)
    return oxy*co2


print(f"Le résultat pour la version 2 est : {v2('day3.txt')}")