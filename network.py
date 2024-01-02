class Wire():

    def __init__(self, split_parts:list, creator):
        self.name = split_parts[-1]
        self.oper = ''
        match len(split_parts):
            case 3:
                try:
                    self._input1 = int(split_parts[0])
                except ValueError:
                    self._input1 = Network.network_output(split_parts[0])
            case 4:
                self.oper = split_parts[0]
                try:
                    self._input1 = int(split_parts[1])
                except ValueError:
                   self._input1 = Network.network_output(split_parts[1])
            case 5:
                try:
                    self._input1 = int(split_parts[0])
                except ValueError:
                    self._input1 = Network.network_output(split_parts[0])

                self.oper = split_parts[1]

                try:
                    self._input2 = int(split_parts[2])
                except ValueError:
                    self._input2 = Network.network_output(split_parts[2])
            case _:
                print('ERROR: Unusual input')
     

    @property
    def input1(self):
        return self._input1
    @property
    def input2(self):
        return self._input2
    @property
    def output(self):
        return self._output
    

    def calc_output(self):
        
        if self.oper == 'AND':
            self._output = self._input1 & self._input2
        elif self.oper == 'OR':
            self._output = self._input1 | self._input2
        elif self.oper == 'LSHIFT':
            self._output = self._input1 << self._input2
        elif self.oper == 'RSHIFT':
            self._output = self._input1 >> self._input2
        elif self.oper == 'NOT':
            self._output = 65535 - self._input1
        elif self.oper == '':
            self._output = self._input1
    

class Network():

    net_index = {}
    
    def __init__(self, for_wire:str):
        f = open('myapp\input_data.txt', 'r')
        rows = f.read().splitlines()
        for i, row in enumerate(rows):
            split_parts = row.split(' ')
            if split_parts[-1] == for_wire:
                w = Wire(split_parts, self)
                w.calc_output()
                self.net_output = w.output
                __class__.net_index[for_wire] = self
                break
                

    @classmethod
    def network_output(cls, for_wire:str):
        try:
            return cls.net_index[for_wire].net_output
        except KeyError:
            return Network(for_wire).net_output


ntw = Network('a')

print(ntw.net_output)

    
