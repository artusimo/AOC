

f = open('myapp\input_data.txt', 'r')
rows = f.read().splitlines()

class Deer:

    time = 0

    def __init__(self, name, speed, endurance, rest):
        self.name = name
        self.speed = int(speed)
        self.endurance = int(endurance)
        self.rest = int(rest)
        self.zero_far = 0
        self.reward = 0
        self.time = 0
        self.travel_time = 0
        self.runs = True

    def travel(self):

        
        if self.time >= 137 and self.name == 'Comet':
            pass
        
        if self.time % (self.endurance + self.rest) >= self.endurance:
            self.runs = False
        else:
            self.runs = True

            self.zero_far += self.speed

        self.time += 1

        

    def incr(self):
        self.reward += 1
            
        #self.sections = (time - Deer.time) // (self.endurance + self.rest)
        #if (time - Deer.time) - self.sections*(self.endurance + self.rest) > self.endurance:
        #    extra_wait = (time - Deer.time) - self.sections*(self.endurance + self.rest)
        #else:
        #    extra_wait = 0
        #self.zero_far = self.zero_far - (self.sections*self.rest + extra_wait)*self.speed

deers = {}
for row in rows:
    row_as_list = row.split(' ')
    deers[row_as_list[0]] = Deer(row_as_list[0], row_as_list[3], row_as_list[6], row_as_list[-2])


deers = dict(sorted(deers.items(), key=lambda item: item[1].zero_far))


deer:Deer
for s in range(1, 2503 + 1):
    for d in deers.values():
        deer = d
        deer.travel()
    

    deers = dict(sorted(deers.items(), key=lambda item: item[1].zero_far, reverse=True))
    lead_deer = list(deers.values())[0]
    [d.incr() for d in list(deers.values()) if d.zero_far == lead_deer.zero_far]

deers = dict(sorted(deers.items(), key=lambda item: item[1].reward, reverse=True))
for d in deers.values():
    deer = d
    print(deer.name, deer.reward)




pass


