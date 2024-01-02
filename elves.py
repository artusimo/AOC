import re

f = open('myapp\input_data.txt', 'r')
row = f.read().splitlines()
row = row[0]

row_repl = []
def calc(row:str, iter_no:int = 0):
    print("iter_no: ", iter_no, "Result:", len(row))
    if iter_no == 50:
        exit()
    d_repl = ''
    next_i = 0
    for i in range(len(row)):
        if i < next_i:
            continue
        amount = 1
        for j in range(i + 1, len(row)):
            if row[i] == row[j]:
                amount += 1
            else:
                break
            
            if i + amount == len(row):
                break

            
        next_i = i + amount 
        d_repl = d_repl + str(amount) + row[i]

        
        
        if i + amount == len(row):
            break
    row_repl.append(d_repl)
    print(row_repl[-1])
    iter_no += 1
    calc(row_repl[-1], iter_no)


calc(row)


