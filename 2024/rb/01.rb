input = ARGF.readlines.map { |line| line.split(/\s+/).map(&:to_i) }
a = input.map { _1.first }.sort
b = input.map { _2 }.sort

puts "part 1: #{a.zip(b).map { (_1 - _2).abs }.sum}"

# Check if there are any repeats in the first list.
# p a: a.size, au: a.uniq.size

# p b: b
total = 0
i = 0
mem = {}
a.each do |x|
  if mem[x]
    # p x => mem[x]
    total += mem[x]
  elsif i < b.size
    while b[i] < x
      i += 1
    end
    j = i
    while b[i] == x
      i += 1
    end
    total += mem[x] = x * (i - j)
    # p a: x, i: i, j: j, c: (i - j)
  end
end
puts "part 2: #{total}" # 21271939
