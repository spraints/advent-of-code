import fileinput

class Computer:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.ip = 0
        self.outs = []

def main():
    opcodes = [
            adv(),
            bxl(),
            bst(),
            jnz(),
            bxc(),
            out(),
            bdv(),
            cdv(),
            ]
    operands = [
            literal(0),
            literal(1),
            literal(2),
            literal(3),
            register_a(),
            register_b(),
            register_c(),
            # reserved_operand(),
            ]

    comp = Computer()
    for line in fileinput.input():
        line = line.strip()
        if line == "":
            continue
        match line.split(":"):
            case ["Register A", val]:
                comp.a = int(val.strip())
            case ["Register B", val]:
                comp.b = int(val.strip())
            case ["Register C", val]:
                comp.c = int(val.strip())
            case ["Program", p]:
                program = [int(n) for n in p.strip().split(",")]
            case other:
                raise ValueError(f"Invalid line: {line}")

    while comp.ip < len(program):
        opcode = program[comp.ip]
        operand = program[comp.ip+1]
        opcodes[opcode].do(comp, operand, operands[operand])
    print("Part 1: ", ",".join([str(n) for n in comp.outs]))

class adv:
    def do(self, comp, _, cmb):
        comp.a = comp.a >> cmb.val(comp)
        comp.ip += 2

class bdv:
    def do(self, comp, _, cmb):
        comp.b = comp.a >> cmb.val(comp)
        comp.ip += 2

class cdv:
    def do(self, comp, _, cmb):
        comp.c = comp.a >> cmb.val(comp)
        comp.ip += 2

class bxl:
    def do(self, comp, lit, _):
        comp.b = comp.b ^ lit
        comp.ip += 2

class bst:
    def do(self, comp, _, cmb):
        comp.b = comp.b & 0x07
        comp.ip += 2

class jnz:
    def do(self, comp, lit, _):
        if comp.a == 0:
            comp.ip += 2
            return
        comp.ip = lit

class bxc:
    def do(self, comp, _, __):
        comp.b = comp.b ^ comp.c
        comp.ip += 2

class out:
    def do(self, comp, _, cmb):
        comp.outs.append(cmb.val(comp) & 0x07)
        comp.ip += 2

class literal:
    def __init__(self, lit):
        self.lit = lit
    def val(self, _):
        return self.lit

class register_a:
    def val(self, comp):
        return comp.a

class register_b:
    def val(self, comp):
        return comp.b

class register_c:
    def val(self, comp):
        return comp.c

main()
