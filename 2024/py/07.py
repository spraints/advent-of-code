import fileinput
def parse_line(line):
    output, inputs = line.split(":")
    output = int(output)
    inputs = [int(x) for x in inputs.strip().split(" ")]
    return (output, inputs)
equations = [parse_line(line) for line in fileinput.input()]

def is_true(output, inputs):
    options = [inputs[0]]
    i = 1
    while i < len(inputs):
        options = [[opt + inputs[i], opt * inputs[i]] for opt in options if opt <= output]
        options = [opt for pair in options for opt in pair]
        i += 1
    return output in options

part1 = 0
not_true = []
for output, inputs in equations:
    if is_true(output, inputs):
        part1 += output
    else:
        not_true.append((output, inputs))
print("Part 1: {}".format(part1))

def cc1(r):
    f = 10
    x = r // 10
    while x > 0:
        f *= 10
        x //= 10
    return f

def is_true2(output, inputs):
    options = [inputs[0]]
    i = 1
    while i < len(inputs):
        # All the new terms increase the value, so drop anything that's already over the limit.
        options = [opt for opt in options if opt <= output]
        new_opts = []
        f = cc1(inputs[i])
        for opt in options:
            new_opts.append(opt + inputs[i])
            new_opts.append(opt * inputs[i])
            new_opts.append(f * opt + inputs[i])
        options = new_opts
        i += 1
    return output in options

part2 = part1
for output, inputs in not_true:
    if is_true2(output, inputs):
        part2 += output
print("Part 2: {}".format(part2))
