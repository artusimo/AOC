from itertools import permutations

class Table(list):

    def __init__(self):
        pass

class Person:

    def __init__(self, name, num, satis:dict, table:dict):
        self.name = name
        self.num = num
        self.satis = satis
        self.table = table

    @property
    def left_adj(self):
        return self.table[self.num - 1]
    
    @property
    def right_adj(self):
        if self.num + 1 >= len(self.table):
            return self.table[0]
        return self.table[self.num + 1]
    
    
f = open('myapp\input_data.txt', 'r')
rows = f.read().splitlines()

persons = []
for row in rows:
    row_as_list = row[0:-1].split(' ')
    rate = int(row_as_list[3])
    if row_as_list[2] == 'lose':
        rate = - rate
    if row_as_list[0] not in (p.name for p in persons):
        persons.append(Person(row_as_list[0], len(persons), {row_as_list[-1]:rate}, persons))
    else:
        for p in persons:
            if p.name == row_as_list[0]:
                p.satis[row_as_list[-1]] = rate


max_satis = -9999

for perm in permutations(persons):

    tot_satis = 0
    for p in perm:
        p.table = list(perm)
        p.num = [p.name for p in p.table].index(p.name)
        tot_satis += p.satis[p.right_adj.name] + p.satis[p.left_adj.name]
    if tot_satis > max_satis:
        max_satis = tot_satis
        best_perm = perm


print([p.name for p in best_perm])

print(max_satis)

# min_satis_incr = 9999
# for p in best_perm:
#     p.table = list(best_perm)
#     p.num = [p.name for p in p.table].index(p.name)

#     satis_incr = p.satis[p.right_adj.name]
#     if satis_incr < min_satis_incr:
#         min_satis_incr = satis_incr
#         print(p.name, p.right_adj.name, satis_incr)
#     satis_incr = p.satis[p.left_adj.name]
#     if min_satis_incr < min_satis_incr:
#         min_satis_incr = satis_incr
#         print(p.name, p.left_adj.name, satis_incr)