
def main():
    assemble = Assemble("2016/day_23/input.txt", 7)
    assemble.execute()
    print(assemble._registers["a"])

class Assemble:

    def __init__(self, input_file, init_a):
        self._instructions = []
        self._registers = {"a": init_a, "b": 0, "c": 0, "d": 0}
        self._curr_instr = 0
        self._opposites = {"dec": "inc", "tgl": "inc", "inc": "dec", "cpy": "jnz", "jnz": "cpy"}
        self.parse(input_file)

    def parse(self, input_file):
        with open(input_file, "r", encoding="utf-8") as in_file:
            for line in in_file:
                split = line.strip("\n").split(" ")
                instruction = [int(val) if (val.isdigit() or val[0] == "-") else val for val in split]
                self._instructions.append(instruction)

    def execute(self):
        while self._curr_instr < len(self._instructions):
            line = self._instructions[self._curr_instr]
            instruction = line[0]
            ops = line[1:]
            getattr(self, instruction)(*ops)

    def cpy(self, op_1, op_2):
        if isinstance(op_2, str):
            val_1 = self._registers.get(op_1, op_1)
            self._registers[op_2] = val_1
        self._curr_instr += 1

    def inc(self, op):
        if isinstance(op, str):
            self._registers[op] += 1
        self._curr_instr += 1

    def dec(self, op):
        if isinstance(op, str):
            self._registers[op] -= 1
        self._curr_instr += 1

    def jnz(self, op_1, op_2):
        val_1 = self._registers.get(op_1, op_1)
        val_2 = self._registers.get(op_2, op_2)
        if val_1 != 0:
            self._curr_instr += val_2
        else:
            self._curr_instr += 1
    
    def tgl(self, op_1):
        val_1 = self._registers.get(op_1, op_1)
        idx_to_tgl = self._curr_instr + val_1
        if idx_to_tgl < len(self._instructions) and 0 <= idx_to_tgl:
            instr_to_tgl = self._instructions[idx_to_tgl][0]
            self._instructions[idx_to_tgl][0] = self._opposites[instr_to_tgl]
        self._curr_instr += 1

if __name__ == "__main__":
    main()