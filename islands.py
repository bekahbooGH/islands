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
#   grid2 = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

# grid: List[List[str]]

def numIslands(grid):
    pointers = []
    for i in range(len(grid)):
        for col in range(len(grid[i])):
            pointer = [i, col]
            neighs = 0
            # l, r, t, b = 0, 0, 0, 0
            # i = pointer[0]
            # col = pointer[1]
            if col >= 1:
                # l = grid[i][col-1]
                # print(grid[i][col-1] )
                if grid[i][col-1] == '1':
                    neighs += 1
                    print("l: " + grid[i][col-1], neighs)
            if col < len(grid[i]) - 1:
                # r = grid[i][col+1]
                if grid[i][col+1] == '1':
                    neighs += 1
                    # print("r: " + grid[i][col+1], neighs)
            if i >= 1:
                # t = grid[i-1][col]
                if grid[i-1][col] == '1':
                    neighs += 1
                    print("t: " + grid[i-1][col], neighs)
            if i < len(grid) - 1:
                # b = grid[i+1][col]
                if grid[i+1][col] == '1':
                    neighs += 1
                    # print("b: " + grid[i+1][col], neighs)
            # print(neighs)
            grid[i][col] = neighs
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
