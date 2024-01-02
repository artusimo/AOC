from itertools import permutations

class Connection:

    def __init__(self, fr, to, dist):
        self.fr = fr
        self.to = to
        self.dist = dist


class City(dict):

    def __init__(self, name):
        super().__init__()
        self.name = name

        for conn in connections:
            if conn.fr == self.name:
                self[conn.to] = conn.dist
        


f = open('myapp\input_data.txt', 'r')
rows = f.read().splitlines()

connections = []
for row in rows:
    delimiters = [' to ', ' = ']
    for delim in delimiters:
        row = " ".join(row.split(delim))
    result = row.split()
    connections.append(Connection(result[0], result[1], int(result[2])))
    connections.append(Connection(result[1], result[0], int(result[2])))

cities = {}
for conn in connections:
    if conn.fr not in cities.keys():
        cities[conn.fr] = City(conn.fr)


def search_for_city(among):
    global_distance = 0
    it = iter(among.values())
    #for city in it:
    city = next(it)
    for next_city in it:
        if next_city.name in city:
            dist = next_city[city.name] #or dist = city[next_city.name]
            #print(next_city.name, dist)
            global_distance += dist
            city = next_city
    #print(distance)
    return global_distance

min_distance = 0
seqs = [dict(x) for x in permutations(cities.items())]
for seq in seqs:
   global_distance = search_for_city(seq)
   #print(global_distance)
   if global_distance > min_distance:
       min_distance = global_distance
       print("________________")
       

print("Asnwear: ", min_distance)
pass

    


    


