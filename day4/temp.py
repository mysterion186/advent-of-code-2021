
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

    def __eq__(self,other):
        if len(self.numbers) != len(other.numbers):
            return False
        else : 
            for k in range(len(self.numbers)):
                if self.numbers[k].value != other.numbers[k].value or self.numbers[k].is_not_marked != other.numbers[k].is_not_marked : 
                    return False
        return True 

temp = """57 80 91 40 12
62 36 72  0 20
55 60 25 92 96
14  2 17 18 86
 1  4 90 66 38"""

game_input = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
test_2 = """3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6"""


# get all the board for the game 
all_board = [[int(k) for k in test_2.split()]]
bingo_1 = Bingo()
bingo_2 = Bingo()

for elt in all_board[0] : 
    bingo_1.add_numbers(Case(elt))
    bingo_2.add_numbers(Case(elt))
all_board[0][0] = Case(27)
for elt in all_board[0] : 
    bingo_2.add_numbers(Case(elt))

print(bingo_1==bingo_2)