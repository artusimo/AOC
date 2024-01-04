from itertools import permutations

#represents relation between every two cities
class Connection:

    def __init__(self, fr, to, dist):
        self.fr = fr
        self.to = to
        self.dist = dist


#city as dict with name, key is other city name, value is distance to it
class City(dict):

    def __init__(self, name):
        self.name = name

        #from global list of connections, store only those starting in current city
        for conn in CONNECTIONS:
            if conn.fr == self.name:
                self[conn.to] = conn.dist
        
#parse input and convert to objects and save to global CONNECTIONS list
def read_input():
    f = open('myapp\input_data.txt', 'r')
    rows = f.read().splitlines()

    global CONNECTIONS
    CONNECTIONS = []
    for row in rows:
        delimiters = [' to ', ' = ']
        for delim in delimiters:
            row = " ".join(row.split(delim))
        result = row.split()
        CONNECTIONS.append(Connection(result[0], result[1], int(result[2])))
        CONNECTIONS.append(Connection(result[1], result[0], int(result[2])))

#creates global network of cities and distances between them
def create_network():
    global CITIES
    CITIES = {}
    for conn in CONNECTIONS:
        if conn.fr not in CITIES.keys():    #avoid duplicate Connections (A -> B same as A <- B)
            CITIES[conn.fr] = City(conn.fr)


def search_for_city(among):
    global_distance = 0
    it = iter(among.values())   #get city iterator
    city = next(it)     #take first city in sequence as default point
    for next_city in it:    #try all other cities
        if next_city.name in city:  #is there a connection from city to next city?
            dist = next_city[city.name] #get distance to next city
            global_distance += dist #add distance to total distance travelled so far
            city = next_city    #next city becomes default in next iteration
    return global_distance  #returns distance travelled thru cities in this sequence

#find min travel distance by trying all possible sequences of cities
def solve():
    global MIN_DISTANCE
    MIN_DISTANCE = 0
    seqs = [dict(x) for x in permutations(CITIES.items())]  #get list of possible city sequences
    for seq in seqs:   #test each sequence
        global_distance = search_for_city(seq)  #compute distance for this sequence
        if global_distance > MIN_DISTANCE:  #if shorter global_distance is found, use it as MIN_DISTANCE
            MIN_DISTANCE = global_distance


read_input()
create_network()  
solve()

print("Answear: ", MIN_DISTANCE)


    


    


