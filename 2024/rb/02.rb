def safe?(report, tolerance: 0)
  steps = report.each_cons(2).map { |a, b| step_type(b - a) }
  steps.all? { |s| s == :inc } || steps.all? { |s| s == :dec }
end

def step_type(diff)
  case diff
  when 1, 2, 3
    :inc
  when -1, -2, -3
    :dec
  else
    :unsafe
  end
end

input = ARGF.readlines.map { _1.strip.split.map(&:to_i) }
puts "Part 1: #{input.count { safe?(_1) }}"
puts "Part 1: #{input.count { safe?(_1, tolerance: 1) }}"

