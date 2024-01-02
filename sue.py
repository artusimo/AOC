import re


class Item:

    def __init__(self, name, amount):
        self.name = name.strip()
        self.amount = int(amount)

class Aunt:

    def __init__(self, number):
        self.number = int(number)
        self.maybe = True


f = open('myapp\input_data.txt', 'r')
rows = f.read().splitlines()

aunts = []
for row in rows:
    row_as_list = row.split(',')
    fir = row_as_list[0].split(' ')
    sec = row_as_list[1].split(': ')
    thi = row_as_list[2].split(': ')
    number = fir[1][:-1]
    item0 = Item(fir[2][:-1], fir[3])
    item1 = Item(sec[0], sec[1])
    item2 = Item(thi[0], thi[1])
    aunt = Aunt(number)
    aunt.items = {item0.name:item0.amount, item1.name:item1.amount, item2.name:item2.amount}
    #print(aunt.items)
    aunts.append(aunt)


for aunt in aunts:
    if 'children' in aunt.items.keys() and aunt.items['children'] != 3:
        aunt.maybe = False
    if 'cats' in aunt.items.keys() and aunt.items['cats'] <= 7:
        aunt.maybe = False
    if 'samoyeds' in aunt.items.keys() and aunt.items['samoyeds'] != 2:
        aunt.maybe = False
    if 'pomeranians' in aunt.items.keys() and aunt.items['pomeranians'] >= 3:
        aunt.maybe = False
    if 'akitas' in aunt.items.keys() and aunt.items['akitas'] != 0:
        aunt.maybe = False
    if 'vizslas' in aunt.items.keys() and aunt.items['vizslas'] != 0:
        aunt.maybe = False
    if 'goldfish' in aunt.items.keys() and aunt.items['goldfish'] >= 5:
        aunt.maybe = False
    if 'trees' in aunt.items.keys() and aunt.items['trees'] <= 3:
        aunt.maybe = False
    if 'cars' in aunt.items.keys() and aunt.items['cars'] != 2:
        aunt.maybe = False
    if 'perfumes' in aunt.items.keys() and aunt.items['perfumes'] != 1:
        aunt.maybe = False
    
candidates = [a.number for a in aunts if a.maybe == True]

print(candidates)


        


    

