
'''
Given: Array, limit
Want: [index01, index02]; Array[index01] + Array[index02] == limit
where index01 > index02

Ideal Sol:
N = len(arr)
O(N) time
O(1) 

lim -= arr[0] = 17
if 17 in arr
return 

diff = limit - arr[i]
arr_ind = {}
arr_ind[arr[i]] = i

if diff in arr_ind:


ex:  input:  arr = [4, 6, 10, 15, 16],  lim = 21
  for element in arr
    store element and index in dict
    
  for element in arr
    diff = limit - element
    
    if arr_ind[diff] == Null
      continue
    otherwise
      return [arr_ind[arr[i]], arr_ind[arr[j]]] where i > j
 
 return []
 Watch out for hashing an item weight before looking up in the map its complement

'''

def get_indices_of_item_wights(arr, limit):
  arr_ind = {}
  
  for ind, num in enumerate(arr):
    
    diff = limit - num
    complement_index = arr_ind.get(diff, -1)
    if complement_index != -1:
      return [ind, complement_index]

    else:
      arr_ind[num] = ind

      
      
      
  return []

arr = [4, 6, 10, 15, 16]
limit = 21

print(get_indices_of_item_wights(arr, limit))