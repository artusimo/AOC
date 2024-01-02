from itertools import combinations

f = open('myapp\input_data.txt', 'r')
rows = f.read().splitlines()

containers = {}
for i, row in enumerate(rows):
    containers[i] = int(row)

combs = 0
min_cnt = 4
for cnt in range(4, 9):
    
    for c in combinations(containers.items(), cnt):
        if sum([v[1] for v in c]) == 150:
            if cnt <= min_cnt:
                min_cnt = cnt
                print(c)
                combs += 1

            
    #break


    



print("Combinations :", combs, min_cnt)
        

    