'''
                     
                        [[0,    1,    0,    1,    0],
                         [1,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]
 R = total rows
 C = totals cols
 R * C
 total_islands = 0
 row_cur = 0
 col_cur = 0
 
 visited[(row, col)] = True
 
 if hit unvisited 1:
  mark as visited
  check adjacent 1's
  
  increment total_islands
 otherwise:
  continue
 

'''

def check(row, col, num_rows, num_cols, visited, queue):

  # Row check (not reading outside of bounds)
  # Column check (not reading outside of bounds)
  # Checking if you already visited:
  
  if row < num_rows and col < num_cols and col >= 0 and row >= 0:
    if visited[(row, col)] == False:
      queue.append([row, col])
  return queue
  
    
  
def search(row, col, num_rows, num_cols, visited):
  queue = [(row, col)]
  while queue:
    curr_node = queue.remove((row,col))
    
    if visited[curr_node] == False:
      visited[curr_node] = True
      row = curr_node[0]
      col = curr_node[1]
      queue = check(row + 1, col, num_rows, num_cols, visited, queue)
      queue = check(row - 1, col, num_rows, num_cols, visited, queue)
      queue = check(row, col + 1, num_rows, num_cols, visited, queue)
      queue = check(row, col - 1, num_rows, num_cols, visited, queue)

  
   
    
    
  
def get_number_of_islands(binaryMatrix):
  R = len(binaryMatrix)
  C = len(binaryMatrix[0])  
  total_islands = 0

  visited = {}
  
  for i in range(R):
    for j in range(C):
      visited[(i, j)] = False
  
  
  
  for row in range(R):
    for col in range(C):
      if binaryMatrix[row][col] == 1 and visited[(row,col)] == False:
        search(row, col, R, C, visited)
        total_islands += 1
        
  return total_islands