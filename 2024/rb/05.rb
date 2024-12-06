require "set"

$verboase = false

order, manuals = ARGF.read.split("\n\n")
$rules = Hash.new { |h,k| h[k] = {followed_by: [], preceded_by: []} }
order.lines.each do |line|
  a, b = line.strip.split("|").map(&:to_i)
  $rules[a][:followed_by] << b
  $rules[b][:preceded_by] << a
end
manuals = manuals.lines.map { |line| line.strip.split(",").map(&:to_i) }

def correct?(manual)
  manual = manual.dup
  no = Set.new
  while v = manual.shift
    print "#{v} " if $verbose
    if no.include?(v)
      print "NO!" if $verbose
      return false
    end
    if r = $rules[v]
      print "#{r.inspect} " if $verbose
      if a = r[:preceded_by]
        a.each
        no.merge(a)
      end
    end
  end
  true
ensure
  puts if $verbose
end

part1 = manuals.sum { |m| correct?(m) ? m[m.size / 2] : 0 }
puts "Part 1: #{part1}"
