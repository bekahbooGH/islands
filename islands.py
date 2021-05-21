# Example 1:
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# Output: [
#   ["2","3","2","2","1"],
#   ["3","3","3","1","1"],
#   ["2","2","1","1","0"],
#   ["1","1","0","0","0"]
# ]

# Example 2:
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# grid: List[List[str]]

def numIslands(grid):
    # pointers = []
    for i in range(len(grid)):
        # print(i)
        # print(grid[i])
        for j in range(len(grid[i])):
            # print(col)
            # pointer = [i, col]
            neighs = 0
            # l, r, t, b = 0, 0, 0, 0
            # i = pointer[0]
            # col = pointer[1]
            if j >= 1:
                # l = grid[i][col-1]
                # print(grid[i][j-1] )
                # print(grid[i][col-1])
                # print(l)
                if grid[i][j-1] == '1':
                    neighs += 1
                    # print("l" + "neighs")
                    # print("l: " + grid[i][col-1], neighs)
            if j < len(grid[i]) - 1:
                # r = grid[i][j+1]
                if grid[i][j+1] == '1':
                    neighs += 1
                    # print("r" + "neighs")
                    # print("r: " + grid[i][col+1], neighs)
            if i >= 1:
                # t = grid[i-1][j]
                if grid[i-1][j] == '1':
                    neighs += 1
                    # print("t" + "neighs")
                    # print("t: " + grid[i-1][col], neighs)
            if i < len(grid) - 1:
                # b = grid[i+1][j]
                if grid[i+1][j] == '1':
                    neighs += 1
                    # print("b" + "neighs")
                    # print("b: " + grid[i+1][col], neighs)
            print(neighs)
        grid[i][j] = neighs
        print(grid)
            
            
            # print(pointer)
            
    # print(grid)
            # print(neighs)
    #         pointers.append(pointer)
    # for pointer in pointers:
    #     neighs = 0
    #     l, r, t, b = 0, 0, 0, 0
    #     i = pointer[0]
    #     col = pointer[1]
    #     if col >= 1:
    #         l = grid[i][col-1]
    #         if l == '1':
    #             neighs += 1
    #     if col < len(grid[i])-1:
    #         r = grid[i][col+1]
    #         if r == '1':
    #             neighs += 1
    #     if i > 1:
    #         t = grid[i-1][col]
    #         if t == '1':
    #             neighs += 1
    #     if i < len(grid):
    #         b = [i+1][col]
    #         if b == 1:
    #             neighs += 1
    #     print(neighs)
        # print(f"l: {l}, r: {r}, t: {t}, b: {b}")
        
# i, col-1, col+1
# col, i-1, i+1        
            
            
# left = 0,0
# pointer = [0,0]
# left
numIslands(grid1)

# safe_get(grid, 0, 0) -> "1"
# safe_get(grid, 0, 4) -> "0"
# safe_get(grid, 6, 0) -> "0"
# safe_get(grid, 3, -2) -> "0"

# print(safe_get(grid1, 0, 0))
# print(safe_get(grid1, 0, 4))
# print(safe_get(grid1, 6, 0))
# print(safe_get(grid1, 3, -2)

# def numIslands(grid):
#     counts = []
#     for i in range(len(grid)):
#       row = []
#         # print(i)
#         # print(grid[i])
#       for j in range(len(grid[i])):
#           # print(col)
#           neighs = 0
#           # l, r, t, b = 0, 0, 0, 0
#           if j >= 1:
#               if grid[i][j-1] == '1':
#                   neighs += 1
#           if j < len(grid[i]) - 1:
#               if grid[i][j+1] == '1':
#                   neighs += 1     
#           if i >= 1:
#               if grid[i-1][j] == '1':
#                   neighs += 1    
#           if i < len(grid) - 1: 
#               if grid[i+1][j] == '1':
#                   neighs += 1
#           # print(neighs) 
#           row.append(neighs)
#         # grid[i][j] = neighs
#       counts.append(row)
#         # print(grid)
#       # counts = [row for row in i] for i in range(len(grid))]
#     return counts
# numIslands(grid1)

# def safe_get(grid: List[List[str]], i: int, j: int, default_val: str = "0") -> str:
#   """Returns the value at the i,j coordinate of
#    grid or default_val if coordinate is out of bounds."""
#   if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
#     return grid[i][j]
#   return default_val


# def count_neighbors(grid, i, j, val):
#   neighs = 0
#   if safe_get(grid, i, j-1) == val:
#     neighs += 1
#   if safe_get(grid, i, j+1) == val:
#     neighs += 1
#   if safe_get(grid, i-1, j) == val:
#     neighs += 1 
#   if safe_get(grid, i+1, j) == val:
#     neighs += 1
#   return neighs


# def numIslands2(grid):
#     counts = []
#     for i in range(len(grid)):
#       row = [count_neighbors(grid, i, j, "1") for j in range(len(grid[i]))]
#       counts.append(row)
#     return counts


# numIslands2(grid1)

# expect_grid_1 = [[2, 3, 2, 2, 1], [3, 3, 3, 1, 1], [2, 2, 1, 1, 0], [1, 1, 0, 0, 0]]
# numIslands2(grid1) == expect_grid_1

def safe_get(grid, i, j, default_val="0"):
    """def safe_get(grid: List[List[str]], i: int, j: int, default_val: str = "0") ->
str:Returns the value at the i,j coordinate of
grid or default_val if coordinate is out of bounds."""
    if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
        return grid[i][j]
    return default_val


# def count_neighbors(grid, i, j, val):
#   neighs = 0
#   if safe_get(grid, i, j-1) == val:
#     neighs += 1
#   if safe_get(grid, i, j+1) == val:
#     neighs += 1
#   if safe_get(grid, i-1, j) == val:
#     neighs += 1 
#   if safe_get(grid, i+1, j) == val:
#     neighs += 1
#   return neighs


# def count_neighbors1(grid, i, j, val):
#   d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#   # d = [(0, +1), (0, -1), (+1, 0), (-1, 0)]
#   neighs = 0
#   for di,dj in d:
#     if safe_get(grid, i+di, j+dj) == val:
#       neighs += 1
#   return neighs

# i = 2
# j = 2
# d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# sum(safe_get(grid1, i+di, j+dj) == "1" for di,dj in d)

def count_neighbors2(grid, i, j, val):
    """Another count neighbors option. Cleaner but more less basic."""
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return sum(safe_get(grid1, i+di, j+dj) == "1" for di,dj in d)


def get_row_counts(grid, i):
    """Fxn to get the row counts."""
    return [count_neighbors2(grid, i, j, "1") for j in range(len(grid[i]))]


def numIslands3(grid):
    return [get_row_counts(grid, i) for i in range(len(grid))]


def numIslands4(grid):
    """Contains count_neighbors2 with more succint but difficult code."""
    return [[count_neighbors2(grid, i, j, "1") for j in range(len(grid[i]))]
        for i in range(len(grid))]

# numIslands1(grid1)
# numIslands2(grid1)
numIslands3(grid1)
numIslands4(grid1)

Coord = "tuple(int, int)"
Grid = "list[list[str]]"

def safe_get(grid: Grid, row: int, col: int, default_val: str = "0") -> "str":
  """Returns the value at the row, col coordinate of
   grid or default_val if coordinate is out of bounds."""
  if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
    return grid[row][col]
  return default_val


def coord_neighbors(grid: Grid, row: int, col: int, val: str) -> "list[Coord]":
  """Returns a list of coordinates neighboring (row, col) where value of 
  coordinate is val."""
  neighs = []
  if safe_get(grid, row, col-1) == val:
    neighs.append((row, col-1))
  if safe_get(grid, row, col+1) == val:
    neighs.append((row, col+1))
  if safe_get(grid, row-1, col) == val:
    neighs.append((row-1, col))
  if safe_get(grid, row+1, col) == val:
    neighs.append((row+1, col))
  return neighs


def island_neighbor_coords(grid: Grid) -> "dict[Coord, list[Coord]]":
  """Returns a dictionary whose keys are the coordinates with '1' and values are
  a list of neighboring coordinates with '1'."""
  ret = {}
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] == "1":
        ret[(row, col)] = coord_neighbors(grid, row, col, "1")
  return ret


# def island_coordinates(grid: Grid) -> List[Coord]:
#   """Returns a list of coordinates where value of coordinate is '1'."""
#   islands = []
#   for row in range(len(grid)):
#     for col in range(len(grid[row])):
#       if grid[row][col] == "1":
#         islands.append((row, col))
#   return islands

def island_of(grid: Grid, row: int, col: int) -> "list[Coord]":
  """Returns a list of all coordinates that are a part of the
  island at (row, col) or an empty list if (row, col) is not
  part of an island."""
  if safe_get(grid, row, col, "0") != "1":
    return []
  ret = []
  visited = set()
  queue = [(row, col)]
  while queue:
    coord = queue.pop()
    if coord not in visited:
      visited.add(coord)
      ret.append(coord)
      r,c = coord
      queue.extend(coord_neighbors(grid, r, c, "1"))
  return ret

island_of(grid2, 0, 0)