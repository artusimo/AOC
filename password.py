import string

f = open('myapp\input_data.txt', 'r')
rows = f.read().splitlines()
row = rows[0]

alphabet = list(string.ascii_lowercase)
numbers = list(range(0, len(alphabet)))
index_letter = dict(zip(numbers, alphabet))
letter_index = {v:k for k, v in iter(index_letter.items())}

def at_least_three_straight(pswd:str):
    for x in range(len(pswd)-2):
        if letter_index[pswd[x+1]] - letter_index[pswd[x]] == 1:
            if letter_index[pswd[x+2]] - letter_index[pswd[x+1]] == 1:
                return True
    return False

def no_iol(pswd:str):
    for ch in ("iol"):
        if ch in pswd:
            return False
    return True

def double_pair(pswd:str):
    for x in range(len(pswd)-4):
        if letter_index[pswd[x+1]] - letter_index[pswd[x]] == 0:
            for y in range(x+2, len(pswd)-1):
                if letter_index[pswd[y+1]] - letter_index[pswd[y]] == 0:
                    return True
    return False

class single_digit_list(list):

    def __init__(self, row:str):
        for ch in row:
            self.append(letter_index[ch])
   
    def incr_to_nine(self, posit:int):
        try:
            if self[posit] < 25:
                self[posit] += 1
                return self
            else:
                self[posit] = 0 
                posit -= 1
                self.incr_to_nine(posit)
        except IndexError as er:
            print(er.args, "Max pswd value reached.")

    def get_as_letter(self):
        row_as_letter = []
        for d in row_as_digit:
            row_as_letter.append(index_letter[d])
        return row_as_letter


row_as_digit = single_digit_list(row)
print(row_as_digit.get_as_letter(), "(Default)" )
for i in range(1, 999999):
    row_as_digit.incr_to_nine(len(row_as_digit)-1)
    subj_to_test = row_as_digit.get_as_letter()
    if at_least_three_straight(subj_to_test) and no_iol(subj_to_test) and double_pair(subj_to_test):
        print(''.join((x) for x in subj_to_test), " at iteration ", i)
        break






        

    

#print(numval)
    
