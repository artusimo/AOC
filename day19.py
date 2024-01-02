

f = open('myapp\input_data.txt', 'r')
rows = f.read().splitlines()

substitutions = {}
for row in rows:
    row_as_list = row.split(' ')
    if row_as_list[0] not in substitutions.keys():
        substitutions[row_as_list[0]] = [row_as_list[2]]
    else:
        substitutions[row_as_list[0]].append(row_as_list[2])
    

f = open('myapp\input_data2.txt', 'r')
molecule = f.readline()

tot_substituents = []
for pos, seg in enumerate(molecule):
    if molecule[pos:pos+2] in substitutions.keys():
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