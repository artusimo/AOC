# --- Day 7: Some Assembly Required ---
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

# For example:

# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
#------------------------
#Solution:

#Wire has 1 or 2 inputs and 0 or 1 operator (gate)
class Wire():

    #construct Wire from flat input
    def __init__(self, split_parts:list):

        #name comes from last non-white literal
        self.name = split_parts[-1]

        #if gate not given, leave empty string
        self.oper = ''

        #rows are of different structures, identified by row length
        match len(split_parts):
            case 3:
                try: #always try to find input value as literal from flat file
                    self._input1 = int(split_parts[0])
                except ValueError: #if input given by preceeding wire's output, create sub-Network for the predecessor
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
    def output(self):
        return self._output
    
    #define operation based on operator
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
        elif self.oper == '': #if no operator
            self._output = self._input1
    

class Network():

    #register for all calculated wires
    net_index = {}
    
    def __init__(self, for_wire:str):
        #read input from .txt
        f = open('myapp\input_data.txt', 'r')
        rows = f.read().splitlines()
        #searches for all rows = wires to find 
        for row in rows:
            split_parts = row.split(' ')
            #until finds input wires needed
            if split_parts[-1] == for_wire:
                #for input wire, create object from flat file
                w = Wire(split_parts) #constructor finds all Wire's inputs recursively
                w.calc_output() #when created, Wire has all inputs to calculate output
                self.net_output = w.output
                #after calculation, add wire to register
                __class__.net_index[for_wire] = self
                break
                
    
    @classmethod
    def network_output(cls, for_wire:str):
        """
        Try to get output from Wire given by user. If not given by input file, calculate it using previous wire (pre-previous, etc.).
        """
        try: #get specified wire's output
            return cls.net_index[for_wire].net_output
        except KeyError: #if not in register, calculate, then save to register
            return Network(for_wire).net_output

#ask for any wire's input ('a' by instruction)
#creates only the subset of network that is needed (not entire network) for given wire,
#so unnecessary calculations (e.g. behind 'a') are ommited
ntw = Network('a')

print("Answer: ", ntw.net_output)

    
