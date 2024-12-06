$grid = ARGF.readlines.map(&:strip).map(&:chars)

def xmas?(x, y, dx, dy)
  return false if x + dx*3 < 0 || y + dy*3 < 0
  $grid[x][y] == "X" &&
    $grid[x+dx][y+dy] == "M" &&
    $grid[x+2*dx][y+2*dy] == "A" &&
    $grid[x+3*dx][y+3*dy] == "S"
rescue NoMethodError # read: out of bounds
  false
end

def countxmas(x, y)
  [
    [1,0],
    [0,1],
    [-1,0],
    [0,-1],
    [1,1],
    [-1,-1],
    [1,-1],
    [-1,1],
  ].count { |dx, dy| xmas?(x, y, dx, dy) }
end

part1 = $grid.each_index.sum { |x| $grid[x].each_index.sum { |y| countxmas(x, y) } }
puts "Part 1: #{part1}"

def x_mas?(x, y)
  return false if x == 0 || y == 0
  return false unless $grid[x][y] == "A"
  tl = $grid[x-1][y+1]
  tr = $grid[x+1][y+1]
  br = $grid[x+1][y-1]
  bl = $grid[x-1][y-1]
  ms = [tl, tr, br, bl].count { |c| c == "M" }
  ss = [tl, tr, br, bl].count { |c| c == "S" }
  return false unless ms == 2 && ss == 2
  tl == tr || tl == bl
rescue NoMethodError # read: out of bounds
  false
end

part2 = $grid.each_index.sum { |x| $grid[x].each_index.count { |y| x_mas?(x, y) } }
puts "Part 2: #{part2}"
