
with open('day4.txt', 'r') as f:
    lines = f.readlines()

# random number used to play bingo 
game_input = [int(k) for k in lines[0].replace("\n","").split(",")]#lines[0].replace('\n', '')




# class that represents a number 
class Case : 
    def __init__(self,value):
        self.value = value
        self.is_not_marked = True # True means that the case is not marked and False means that the case is marked

    
    # function for marking a number
    def set_status(self):
        if self.is_not_marked :
            self.is_not_marked = False

# class that represents the bingo board 
class Bingo :
    def __init__(self):
        self.numbers = [] # list that will contains all the numbers present in the board

    # function to add a number to the board
    def add_numbers(self,case):
        self.numbers.append(case)
    
    # boolean to find if a number is present in the board
    def check_numbers(self,number):
        for elt in self.numbers :
            if elt.value == number and elt.is_not_marked: # look only for unmarked number
                elt.set_status()
                return True
        return False

    # boolean to find if it's a winning board 
    def check_winning_board(self):
        # check horizontally if all numbers are marked 
        row,col = 5,5 
        for k in range(row):
            count = 0
            for i in range(col):
                if not self.numbers[k*row+i].is_not_marked : 
                    count += 1
                    # self.numbers[[k*row+i]].set_status()
            if count == 5 : 
                return True
        
        for k in range(row):
        # check vertically if all numbers are marked
            count = 0
            for i in range(col):
                if not self.numbers[k+row*i].is_not_marked : 
                    count += 1
                    # self.numbers[k+row*i].set_status()
            if count == 5 : 
                return True
        return False       

    # function to test if 2 boards are equals 
    def __eq__(self,other):
        if len(self.numbers) != len(other.numbers):
            return False
        else : 
            for k in range(len(self.numbers)):
                if self.numbers[k].value != other.numbers[k].value or self.numbers[k].is_not_marked != other.numbers[k].is_not_marked : 
                    return False
        return True 

    # function to display_board 
    def display_board(self,final_value):
        row,col = 5,5 
        winning_board = []
        for k in range(row):
            for i in range(col):
                print(self.numbers[k*row+i].value,end=" ")
                winning_board.append(self.numbers[k*row+i])
            print()
        
        # sum of unmarked numbers
        sum = 0
        for elt in winning_board : 
            if elt.is_not_marked : 
                sum += elt.value
        return sum*final_value


temp = """57 80 91 40 12
62 36 72  0 20
55 60 25 92 96
14  2 17 18 86
 1  4 90 66 38"""



# get all the board for the game 
all_board = []
current_board = 0
current_line = 2 # the board's info starts at line 3 on the input file 
temp = []
while current_line< len(lines):
    if lines[current_line] != "\n" and current_line!=len(lines)-1 :
        for elt in lines[current_line].replace("\n","").split(): 
            temp.append(int(elt)) 
        current_line += 1
    elif lines[current_line]=="\n" :
        current_board +=1 
        current_line +=1
        all_board.append(temp)
        temp = []
    elif current_line==len(lines)-1 : 
        for elt in lines[current_line].replace("\n","").split(): 
            temp.append(int(elt))
        all_board.append(temp)
        current_line +=1

all_game_board = []
# create all game board 
for k in range(len(all_board)):
    all_game_board.append(Bingo())
    for elt in all_board[k]:
        all_game_board[k].add_numbers(Case(elt))

still_playing = True # boolean to make sure that we stop at the first winning board 
# playing bingo game on all board 
for k in game_input:
    for game in all_game_board : 
        game.check_numbers(k)
        if game.check_winning_board():
            result = game.display_board(k)
            still_playing = False 
            break
    if not still_playing :
        break

print(f"Pour la version 1 le résultat est {result}")

# function to check if a list already contains a board 
def board_in_list(board_list,board):
    for elt in board_list :
        if board == elt : 
            return True
    return False

test_1 = """22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19"""
test_2 = """3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6"""
test_3 = """14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


# board_1 = [int(k) for k in test_1.split()]
# board_2 = [int(k) for k in test_2.split()]
# board_3 = [int(k) for k in test_3.split()]

# all_board = [board_1,board_2,board_3]


all_game_board = []
# create all game board 
for k in range(len(all_board)):
    all_game_board.append(Bingo())
    for elt in all_board[k]:
        all_game_board[k].add_numbers(Case(elt))

#game_input = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
still_playing = True # boolean to make sure that we stop at the first winning board 
board_set = []
# playing bingo game on all board 
for k in game_input:
    for game in all_game_board : 
        if not board_in_list(board_set,game):
            game.check_numbers(k)
            if game.check_winning_board():
                board_set.append(game)
                print("k",k)
                result = game.display_board(k)
                print(result)
    if not still_playing :
        break

print(len(all_game_board))
