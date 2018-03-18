class memory():
    def __init__(self, tape_size=55):
        self.tape_size = tape_size
        self.tape = [[0] for x in range(tape_size)]
        self.pointer = 0

    #function that helps __repr__ print the arrow that points towards our currently selected cell
    #by grabbing the length of all cells before it and offsetting itself by that amount
    def _arrow(self):
        arrow = ""
        for i, x in enumerate(self.tape):
            
            total_length = len(str(self.tape[i][0])) + 2
            
            if i != self.pointer:
                arrow += " " * total_length

            else:
                if total_length % 2 == 1:
                    arrow += " " * int(total_length / 2)
                    arrow += "^"
                    arrow += " " * int(total_length / 2)
                else:
                    arrow += " " * int(((total_length / 2) - 1))
                    arrow += "^"
                    arrow += " " * int((total_length / 2))
                break
        return arrow

    def __repr__(self):
        return "%s\n%s" %("".join([str(x) for x in self.tape]), self._arrow())

    def increase_pointer(self):
        if self.pointer == self.tape_size - 1:
            self.pointer = 0
        else:
            self.pointer += 1

    def decrease_pointer(self):
        if self.pointer == 0:
            self.pointer = self.tape_size - 1
        else:
            self.pointer -= 1

    def increase_cell(self):
        self.tape[self.pointer][0] += 1

    def decrease_cell(self):
        self.tape[self.pointer][0] -= 1

    def input_number(self, cell_input):
        self.tape[self.pointer][0] = cell_input

    def current_value(self):
        return self.tape[self.pointer][0]

if __name__ == "__main__": 
    mem = memory(55)
    print(mem.tape)
    


