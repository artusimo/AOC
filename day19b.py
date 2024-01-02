

f = open('myapp\input_data.txt', 'r')
rows = f.read().splitlines()

substitutions = {}
for row in rows:
    row_as_list = row.split(' ')
    substitutions[row_as_list[2]] = row_as_list[0]


substitutions_ord = {}
for key in sorted(substitutions.keys(), key=len, reverse=True):
    substitutions_ord[key] = substitutions[key]
    

f = open('myapp\input_data2.txt', 'r')
molecule = f.readline()

exchange_cnt = 0
i = 0
while i < 5:
    for so_k in substitutions_ord.keys():
        new_start = 0
        fir_occ = 1
        while fir_occ > 0:
            print(so_k)
            fir_occ = molecule.find(so_k, new_start, len(molecule))
            if fir_occ > -1 :
                exchange_cnt += 1
                new_start = fir_occ + 1
                molecule = molecule.replace(so_k, substitutions_ord[so_k], 1)
    i += 1
        

print("Lenght: ", len(molecule))
print("After exchanges: ", exchange_cnt)
exit()
tot_substituents = []
for pos, seg in enumerate(molecule):
    if molecule[pos:pos+2] in substitutions_ord.keys():
        pot_substituents = substitutions[molecule[pos:pos+2]]

        for i in range(0, len(pot_substituents)):
            substituent = pot_substituents[i]
            molecule_new = molecule[: pos] + substituent + molecule[pos + 2 :]
            tot_substituents.append(molecule_new)

    elif molecule[pos] in substitutions.keys():
        pot_substituents = substitutions[molecule[pos]]

        for j in range(0, len(pot_substituents)):
            substituent = pot_substituents[j]
            molecule_new = molecule[: pos] + substituent + molecule[pos + 1 :]
            tot_substituents.append(molecule_new)


distinct_substituents = []
for sub in tot_substituents:
    if sub not in distinct_substituents:
        distinct_substituents.append(sub)



print("Tot_substituents: ", len(distinct_substituents))