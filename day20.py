


class House:

    def __init__(self, address):
        self.address = address
        self.present_cnt = 0
        self.visited_by = []

    def receive(self, quantity):
        self.present_cnt += quantity


class Elf:

    def __init__(self, number, houses:dict):
        self.number = number
        self.houses = houses
        self.reset_tour()
        self.next_address = self.genus.__next__()

    def reset_tour(self):
        self.genus = (x * self.number for x in range(1, 99999))

    def deliver(self):
        new_address = self.next_address
        if new_address <= len(self.houses):
            self.houses[new_address].receive(self.number*10)
            self.houses[new_address].visited_by.append(self.number)
            self.next_address = self.genus.__next__()


max_present_cnt = 0
houses = {}
elves = [None]
i = 0
while True:
    i += 1
    h = houses[i] = House(i)
    elf = Elf(i, houses)
    
    elves.append(elf)
    for e in elves:
        if e != None and e.next_address == i:
            e.deliver()
    if h.present_cnt > max_present_cnt:
        print(h.present_cnt)
        max_present_cnt = h.present_cnt
    #print(h.present_cnt)
    if h.present_cnt >= 29000000: #my puzzle input
        print(h.address)
        break

