import fileinput
from itertools import batched
from functools import reduce

VIZ = False

class Computer:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.ip = 0
        self.outs = []

    def dup(self):
        other = Computer()
        other.a = self.a
        other.b = self.b
        other.c = self.c
        other.ip = self.ip
        other.outs = [x for x in self.outs]
        return other

    def with_a(self, a):
        new_comp = self.dup()
        new_comp.a = a
        return new_comp

def main():
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
                print(line)
            case other:
                raise ValueError(f"Invalid line: {line}")
    orig_comp = comp.dup()

    run_program(comp, program)
    print("Part 1: ", ",".join([str(n) for n in comp.outs]))

    if VIZ:
        print("Part 2:")
        for i, (op, arg) in enumerate(batched(program, 2)):
            print(f"  [{i*2}]   {type(opcodes[op]).__name__} ({op})  {arg}")
        # a = ?
        # out = []
        # while a > 0:
        #   b = a % 8         # bst 4
        #   b = b ^ 2         # bxl 2
        #   c = a >> b        # cdv 5
        #   b = b ^ 3         # bxl 3
        #   b = b ^ c         # bxc 4
        #   out.append(b % 8) # out 5
        #   a = a >> 3        # adv 3
        #                     # jnz 0
        # goal:
        #  out = [2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0]
        #
        # 1. take the right 3 bits of A (B).
        # 2. flip bit 2 in B.
        # 3. take the bits of a starting at B (C).
        # 4. flip bits 2 and 1 in B.
        # 5. xor B and C to make B.
        # 6. output B.
        # 7. drop the right three bits of A.
        #
        # 
        guess = reduce(lambda x, y: x*8 + y, reversed(program))
        print(f"Guess for part 2: {guess} {guess:x}")
        comp = orig_comp.dup()
        comp.a = guess

        run_program(comp, program)
        print("Part 2: ", ",".join([str(n) for n in comp.outs]))

        for manual_guess in range(1,8):
            comp = orig_comp.dup()
            comp.a = manual_guess
            run_program(comp, program)
            print(f"{manual_guess} => {comp.outs}")

        print("-------")
        # A = 0b...DEF...GHI
        # B = 0bGHI
        # B = 0bG^HI (off)
        # C = 0bDEF (A >> B)
        # B = 0bGH^I
        # B = 0bGH^I ^ 0bDEF
        #
        # starting from the end.
        # 0: want to output 0. Simply, an input of 0b001 => 0.
        # 1: so now, A=0b001GHI and we want an output of 3 (0b011).
        #    G=D H=^E I=F
        #    000
        manual_guess = 0b001000
        comp = orig_comp.dup()
        comp.a = manual_guess
        run_program(comp, program)
        print(f"{manual_guess} => {comp.outs} ({comp.outs == program})")

    a_s = [0]
    for x in reversed(program):
        if VIZ:
            print(f"Find program that will output {x}")
        new_a_s = []
        for a_l in range(8):
            for a_h in a_s:
                a = (a_h << 3) | a_l
                o = first_out(orig_comp.with_a(a), program)
                if VIZ:
                    print(f"   a={a_h}+{a_l} => {a} => {o}")
                if x == o:
                    new_a_s.append(a)
        a_s = new_a_s
    part2 = min(a_s)
    part2comp = orig_comp.with_a(part2)
    run_program(part2comp, program)
    print("Part 2: ", min(a_s))
    print("        ", ",".join([str(x) for x in part2comp.outs]))

def first_out(comp, program):
    while comp.ip < len(program):
        opcode = program[comp.ip]
        operand = program[comp.ip+1]
        if VIZ:
            show_state(comp)
            print(f"operation {type(opcodes[opcode]).__name__} ({opcode}) {operand} {type(operands[operand]).__name__}")
        opcodes[opcode].do(comp, operand, operands[operand])
        if len(comp.outs) > 0:
            return comp.outs[0]

def run_program(comp, program):
    while comp.ip < len(program):
        opcode = program[comp.ip]
        operand = program[comp.ip+1]
        if VIZ:
            show_state(comp)
            print(f"operation {type(opcodes[opcode]).__name__} ({opcode}) {operand} {type(operands[operand]).__name__}")
        opcodes[opcode].do(comp, operand, operands[operand])
    if VIZ:
        show_state(comp)

def show_state(comp):
    print(f"ip={comp.ip} a={comp.a:x} b={comp.b:x} c={comp.c:x}")

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
        comp.b = cmb.val(comp) & 0x07
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

main()
