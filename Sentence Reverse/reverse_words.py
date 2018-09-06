'''

arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', #perfect
                'm', 'a', 'k', 'e', 's', '  ',# makes
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ] # practice

  
  [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
          
  method 1: save each sererate word into a list
  append char by char into the new array
  
  arr[0:6] --> output[n-7:n-1]
  
'''

  
''' while start_ptr < n
  
    if arr[start_ptr] == " ":
      output[end_ptr] 
      
    counter += 1
    start_ptr += 1
    end_ptr -= 1
 '''
  
def reverse_words(arr):
  n = len(arr)
  
  output = [' '] * n
  
  size = 0
  
  start_ptr = 0
  
  end_ptr = n

  # loop through array
  while start_ptr < n:
    if arr[start_ptr] == " ":
      output[end_ptr:(end_ptr + size)] = arr[(start_ptr - size):start_ptr]
      size = 0
    else: 
       size += 1
    
    start_ptr += 1  
    end_ptr -= 1
  
  output[:size] = arr[n-size:]
  return output
  
      