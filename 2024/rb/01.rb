input = ARGF.readlines.map { |line| line.split(/\s+/).map(&:to_i) }
a = input.map { _1.first }
b = input.map { _2 }
puts a.sort.zip(b.sort).map { (_1 - _2).abs }.sum
