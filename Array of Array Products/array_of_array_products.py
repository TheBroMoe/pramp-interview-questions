'''
 Given: [8, 10, 2]
 result: [10* 2, 8*2, 8*10]
 
input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
  
 a,b,c,d,e
 
 c = a*b * d*e
 d = (a*b*c) * e
 
 
  
start -> end ; end -> start

product = 1
              ->
left_array = [1,8,80]
right_array = [1,2,20]
right_array =[20,2,1]
                    <-
                    
for i = 0; i < len(arr); i++{
    product *= arr[i]
    left_array.append(product)
  }

for i = len(arr); i > 0; i++{
    product *= arr[i]
    right_array.append(product)
  }
  
 final_array = []
for i = 0; i < len(arr); i++
   final_array[i] = left_array[i] * right_array[len(arr)-i]
start: 
product
'''
def array_of_array_products(arr):
  # Initialize product
  product = 1
  # Initialize arrays
  start_array = []
  
  n = len(arr)
  
  if n == 0 or n == 1:
    return []

  # Append intermediate products to start_array
  for i in range(n):
    start_array.append(product)
    product *= arr[i]
    
  product = 1
  for i in range(n - 1, -1, -1):
    start_array[i] *= product
    product *= arr[i]
  
  return start_array