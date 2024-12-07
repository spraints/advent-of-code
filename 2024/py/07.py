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
part1 = sum([output for output, inputs in equations if is_true(output, inputs)])
print("Part 1: {}".format(part1))
