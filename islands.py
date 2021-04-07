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
    return [count_neighbors(grid, i, j, "1") for j in range(len(grid[i]))]


def numIslands3(grid):
    return [get_row_counts(grid, i) for i in range(len(grid))]


def numIslands4(grid):
    """Contains count_neighbors2 with cmore succint but difficult code."""
    return [[count_neighbors2(grid, i, j, "1") for j in range(len(grid[i]))]
        for i in range(len(grid))]

numIslands1(grid1)
numIslands2(grid1)
numIslands3(grid1)
numIslands4(grid1)