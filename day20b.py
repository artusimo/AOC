# --- Day 20: Infinite Elves and Infinite Houses ---

# To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

# Each Elf is assigned a number, too, and delivers presents to houses based on that number:

# The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
# The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
# Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....
# There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.

# So, the first nine houses on the street end up like this:

# House 1 got 10 presents.
# House 2 got 30 presents.
# House 3 got 40 presents.
# House 4 got 70 presents.
# House 5 got 60 presents.
# House 6 got 120 presents.
# House 7 got 80 presents.
# House 8 got 150 presents.
# House 9 got 130 presents.



# The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.

# With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?
#-----------------------------------------------
#Solution:


#House receives gifts from elves and counts them
class House:

    def __init__(self, address):
        self.address = address
        self.present_cnt = 0

    def receive(self, quantity):
        self.present_cnt += quantity


class Elf:
    """
    Represents an elf from Day20 AOC 2015. His instance distributes presents to house whose address is given by an integer series specific for the elf.
    """
    #elves register of type {House.address : [elf0, elf1... elfn]}
    #value represents a list of elves applicable to a given house
    elves_by_house = {}

    def __init__(self, number:int, houses:dict):

        #identifies elf
        self.number:int = number

        #houses to serve
        self.houses:dict = houses

        #generator of House.address to be visited next
        self.next_house_gen = (x * self.number for x in self.to_inf())
        #alt: self.next_house_gen = (x * self.number for x in range(1, 99999999))

        #first address to be visited
        self.next_address = self.next_house_gen.__next__()

        #add elf to the register for first address
        Elf.elves_by_house.setdefault(self.next_address, []).append(self)
        
        #how many deliveries elf made
        self.deliveries_made = 0

    #generate inifinite series
    def to_inf(self):
        init = 1
        while True:
            yield init
            init += 1

    #delivers to next house in his House.address generator
    def deliver(self):
        #elf stops after 50 houses (by instructions)
        if self.deliveries_made < 50:
            #house receives amount of gifts determined by elf number and multipled by 11
            self.houses[self.next_address].receive(self.number*11)
            self.deliveries_made += 1
            self.register()

    #generate new House.address and save to static dict
    def register(self):
        self.next_address = self.next_house_gen.__next__()
        Elf.elves_by_house.setdefault(self.next_address, []).append(self)



#gifts distribution to houses picked by elf's generator
def solve():
    houses = {} #slovnik s domy #houses
    i = 0

    #indefinite series of houses and elves. For each new house, a new elf is created
    while True:
        i += 1
        #for every new House, #new Elf is generated
        h = houses[i] = House(i)    
        Elf(i, houses)
        #for every existing elf, check if current House is in his address generator
        for e in Elf.elves_by_house[i]:
            if e.next_address == i: #if so, deliver to that house
                e.deliver()
        #task is to find a house with amount of gifts > 29000000
        if h.present_cnt >= 29000000:
            print(h.address) #print answer
            exit()  #end programme

solve()