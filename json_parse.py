import json

f = open('myapp\input_data.txt', 'r')

data = json.load(f)


tot = 0
def asdad(data):
    global tot
    if type(data) == dict and "red" not in data.values():
        return sum(map(asdad, data.values()))
    if type(data) == list:
        return sum(map(asdad, data))
    if type(data) == int:
        return data
    return tot

print(asdad(data))




