input = ARGF.readlines.map { |line| line.split(/\s+/).map(&:to_i) }
a = input.map { _1.first }.sort
b = input.map { _2 }.sort

puts "part 1: #{a.zip(b).map { (_1 - _2).abs }.sum}"

# Check if there are any repeats in the first list.
bc = b.group_by(&:itself).transform_values(&:size)
bc.default = 0
puts "part 2: #{a.sum { bc[_1] * _1 }}"
