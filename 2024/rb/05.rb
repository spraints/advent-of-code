require "set"

$verbose = false
$verbose2 = false

order, manuals = ARGF.read.split("\n\n")
$rules = Hash.new { |h,k| h[k] = {followed_by: [], preceded_by: []} }
order.lines.each do |line|
  a, b = line.strip.split("|").map(&:to_i)
  $rules[a][:followed_by] << b
  $rules[b][:preceded_by] << a
end
manuals = manuals.lines.map { |line| line.strip.split(",").map(&:to_i) }

def correct?(manual)
  no = Set.new
  manual.each do |v|
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

def mid(a)
  a[a.size / 2]
end

part1 = manuals.sum { |m| correct?(m) ? mid(m) : 0 }
puts "Part 1: #{part1}"

def corrected(manual)
  return [0] if correct?(manual)

  #chunks = []
  #manual.each do |v|
  #  if r = $rules[v]
  #    before, after, dont_care = split_chunks(chunks, r)
  #    if before.empty? && after.empty?
  #      chunks << [v]
  #    elsif before.empty?
  #      chunks = [ [ v, after ] ] + dont_care
  #    elsif after.empty?
  #      chunks = [ [ before, v ] ] + dont_care
  #    elsif before == after
  #      raise "todo b==a: #{v} (#{r})\nchunks = #{chunks}\nbefore = #{before}\nafter = #{after}\ndont_care = #{dont_care}"
  #    else
  #      chunks = [ [ before, v, after ] ] + dont_care
  #    end
  #  else
  #    chunks << [v]
  #  end
  #end
  #res = chunks.flatten

  res = manual.sort { |a, b|
    if r = $rules[a]
      if r[:preceded_by].include?(b)
        # wrong order
        1
      elsif r[:followed_by].include?(b)
        # right order
        -1
      else
        0
      end
    else
      0
    end
  }

  puts "#{manual} should be #{res}" if $verbose2
  res
end

def split_chunks(chunks, rule)
  before = chunks.reject { |c| (c.flatten & rule[:preceded_by]).empty? }
  after  = chunks.reject { |c| (c.flatten & rule[:followed_by]).empty? }
  dont_care = chunks - before - after
  [before, after, dont_care]
end

part2 = manuals.sum { |m| mid(corrected(m)) }
puts "Part 2: #{part2}"
