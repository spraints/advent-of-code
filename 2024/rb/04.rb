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
