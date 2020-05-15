import numpy as np
def is_Possible(row,column,k,grid):
  #Returns true if k at position (row,column) is valid
  for i in range(9):
    if grid[row][i] == k:
      return False
    if grid[i][column] == k:
      return  False
  row_block_num = (int)((row)/3)
  column_block_num = (int)((column)/3)
  for r in range((row_block_num*3),(row_block_num*3)+3):
    for c in range((column_block_num*3),(column_block_num*3)+3):
      if grid[r][c] == k:
        return False
  return True
def backtracker(grid):
  for y in range(9):
    for x in range(9):
      if grid[x][y] == 0:
        for k in range(1,10):
          if is_Possible(x,y,k,grid):
            grid[x][y] = k
            backtracker(grid)
            grid[x][y] = 0
        return
  print(grid)