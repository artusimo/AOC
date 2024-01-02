

class Grid():

    time = 0

    def __init__(self):
        self.lights = {}
        for row_no, row in enumerate(rows):
            for col_no, char in enumerate(row):
                self.lights[(row_no, col_no)] = Light(char, row_no, col_no, self)


    def get_light_status(self, *args):
        try:
            stat = self.lights[(args[0], args[1])].get_prev_status()
        except KeyError:
            return False
        return stat



class Light:

    def __init__(self, char, line_no, column_no, grid:Grid):
        self._status = [False]
        if char == '#':
            self._status = [True]
        self.line_no = line_no
        self.column_no = column_no
        self.grid = grid


    #@property
    def get_prev_status(self):
        return self._status[Grid.time - 1]
    
    #@status.setter
    def add_status(self, status:bool):
        self._status.append(status)


    @property
    def neighbours_on(self):
        return self._neighbours_on
    
    #@neighbours_on.setter
    def calc_neighbours_on(self):
        self._neighbours_on = 0
        self._neighbours_on += self.grid.get_light_status(self.line_no - 1, self.column_no + 1)
        self._neighbours_on += self.grid.get_light_status(self.line_no + 0, self.column_no + 1)
        self._neighbours_on += self.grid.get_light_status(self.line_no + 1, self.column_no + 1)
        self._neighbours_on += self.grid.get_light_status(self.line_no + 1, self.column_no + 0)
        self._neighbours_on += self.grid.get_light_status(self.line_no + 1, self.column_no - 1)
        self._neighbours_on += self.grid.get_light_status(self.line_no + 0, self.column_no - 1)
        self._neighbours_on += self.grid.get_light_status(self.line_no - 1, self.column_no - 1)
        self._neighbours_on += self.grid.get_light_status(self.line_no - 1, self.column_no + 0)
        #if self.column_no == 99:
        #    pass

        return self._neighbours_on



f = open('myapp\input_data.txt', 'r')
rows = f.read().splitlines()


grid = Grid()


for t in range(1, 100 + 1):
    Grid.time = t
    print("Time: ", Grid.time)
    for lv in grid.lights.values():
        
        l:Light = lv
        l.calc_neighbours_on()
        #stay on if on and (3 or 4) neigbours on
        if l.get_prev_status() == True and l.neighbours_on in (2, 3):
            l.add_status(True)
        #turn on if off and and 3 neighbours on
        elif l.get_prev_status() == False and l.neighbours_on == 3:
            l.add_status(True)
        else:
            l.add_status(False)

        grid.lights[ 0, 99]._status[-1] = True
        grid.lights[99, 0 ]._status[-1] = True
        grid.lights[99, 99]._status[-1] = True
        grid.lights[ 0, 0 ]._status[-1] = True



    
total_on = sum(lv._status[-1] for lv in grid.lights.values())
print("Total on: ", total_on)
    



