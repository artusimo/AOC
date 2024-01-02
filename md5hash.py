import hashlib

start = b'iwrupvqb'

for c in range(1, 99999999):

    unk = str(c).encode()
    input = start + unk
    md5hash = hashlib.md5(input)

    result = md5hash.hexdigest()

    if result[0:6] == "000000":
        print(c, "  ", result)
        break