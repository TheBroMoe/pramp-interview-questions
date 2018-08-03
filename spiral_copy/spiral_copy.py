'''
                        [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
                         
      [1,2,3,...]
      output_array = []
      1. traverse first list from 0 to n
        append to output_array
         stop searching 
      2. append last element of each list
      3. append first to last
      4. append first elemnt of each list
      5. repeat 1. ignore last element
      
     psuedo-code:
      1. traversing left to right (left_col, right_col)
      2.  up to down (top_row, bot_row)
      3. right to left (right_col, left_col)
      4. down to up (bot_row, top_row)
      
      O(n) time
      O(n) space
      
      R = numbers of rows
      C = # cols
      
      
'''

def spiral_copy(inputMatrix):
  total_col = len(inputMatrix[0])  
  total_row = len(inputMatrix)  
  left_col = 0
  right_col = total_col
  top_row = 0  
  bot_row = total_row
  
  output = []
  while top_row <= bot_row and left_col <= right_col:
    for i in range(left_col, right_col):
      output.append(inputMatrix[top_row][i])
    
    top_row += 1

    for j in range(top_row, bot_row):
      output.append(inputMatrix[j][right_col])
    
    right_col -= 1
    
    if top_row <= bot_row:
      for i in range(right_col, left_col):
         output.append(inputMatrix[bot_row][i])
      bot_row -= 1
    
    if left_col <= right_col:
      for j in range(bot_row , top_row):
        output.append(inputMatrix[j][left_col])

      left_col += 1
    
  return output