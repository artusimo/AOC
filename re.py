import re

f = open('myapp\input_data3.txt', 'r')
rows = f.read().splitlines()

specs_tot = 0
new_spec_tot = 0
all_tot = 0
orig_tot = 0
tot_incr = 0
for row in rows:

    specs = 0
    print("-------------------------")
    print(row, "        original")

    row_orig_first = row
    row_orig = row
    doublequotes = re.findall(r'\"', row)
    specs = specs + len(doublequotes)
    row = re.sub(r'\"', r'\"', row)
    print(row, "    after doublequotes ", len(row) - len(row_orig))


    row_orig = row
    pattern = r'\\(?!")(?!x)'
    backslashes = re.findall(pattern, row)
    specs = specs + len(backslashes)
    row = re.sub(pattern, r'\\\\', row)
    print(row, "    after backslashes ", len(row) - len(row_orig))



    row_orig = row
    pattern = r'\\x[a-z0-9]{2}'
    singlequotes = re.findall(pattern, row)
    if len(singlequotes) > 0:
        specs = specs + len(singlequotes)*3
    row = re.sub(pattern, r'\\\\x27' , row)
    print(row, "    after singlequotes ", len(row) - len(row_orig))
    


    row_orig = row
    row = '"' + row + '"'
    
    
    print(row, "    after wrap: ", len(row) - len(row_orig))
    incr = len(row) - len(row_orig_first)
    print("incr: ", incr)
    tot_incr += incr
    #specs_tot += specs
print("________")
print("total incr:",  tot_incr)


