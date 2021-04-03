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
    for i, row in enumerate(grid):
        for col in range(len(row)):
            pointer = [i, col]
            pointers.append(pointer)
    for pointer in pointers:
        l, r, t, b = 0, 0, 0, 0
        i = pointer[0]
        col = pointer[1]
        if col >= 1:
            l = [i, col-1]
        if col < len(row):
            r = [i, col+1]
        if i > 1:
            t = [i-1, col]
        if i < len(grid):
            b = [i+1, col]
        print(f"l: {l}, r: {r}, t: {t}, b: {b}")
        
# i, col-1, col+1
# col, i-1, i+1        
            
            
# left = 0,0
# pointer = [0,0]
# left
numIslands(grid1)
