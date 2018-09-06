'''

given: uneven str of brackets
want: counter to balance str
left_count, right_count = 0, 0
"(()"

"(((" .........
")))()"
  unblanced_brackets = 0
 left : 0
 right : 0
 if right:
  right += 1
  if left:
  left += 1
  
  if right > left:
    unbalanced_brackets += right - left
  right -= right - left
  
  if left > right:

")()" : 2

left_count : 2
right_count : 1
output: 1

if left_count == right_count return 0

“())(”
left_count : 2
right_count : 2

right > left :
  
for char in text:
  if char == "("
    left_count += 1
  elif char == ")"
    right_count += 1
'''
# 
def bracket_match(text):
  
  if not text:
    return 0
  
  left_count = 0
  right_count = 0
  unbalanced_bracket = 0
  
  for char in text:
    if char == '(':
      left_count += 1
    
    elif char == ')':
      right_count += 1
    
    if right_count > left_count:
      diff = right_count - left_count
      unbalanced_bracket += diff
      
      right_count -= diff
  
  if left_count > right_count:
    unbalanced_bracket += left_count - right_count
  
  return unbalanced_bracket

if __name__ == "__main__":
  
  print(bracket_match("(()"))
  print(bracket_match("())("))  