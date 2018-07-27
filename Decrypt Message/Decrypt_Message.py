'''
TIPS FOR SELF:
  - When evaluating your own example: try to take shortcuts to save time

Given: word = "flgxswdliefy"
want: "encyclopedia"

step 1: Decrypt the first letter
  - Convert to ASCII value; 
      f: 102
  - Subtract 1; 
      102 - 1 = 101
      
  - Move value to be in range of a - z  (97 - 122) ASCII values by adding 26
      101 within range 97-122
   
   - Convert value back to a character
      101: e
      
step 2: Given the decrypted previous letter 'prev' and it's value after the second step of encryption, 'second_step_prev'
  - Convert current letter to ascii value
      l: 108
      
  - Subtract value with second_step_prev
      108 - 102 = 6
      
  - Add multiples of 26 to be in range of a-z ASCII value (97-122)
      6 + 4 * 26 = 110
  
  - 3 parts
    * Convert result back to character:
        110 : n
        
    * Store ASCII value in prev
        prev = 110
    
    * Add ASCII value to second_step_prev for decryption of next letter
        second_step_prev += prev 

step 3: Append to decrypyted and repeat step 2 for next character until entire string is decrypted

Algorithm: 
enc[n] = dec[n] + second_step[n - 1] + 26 * m
dec[n] = enc[n] - second_step[n - 1] - 26 * m



'''
'''
Character -> ASCII:
number = ord(char)

Ascii -> Character:
char = chr(number)
'''  

def decrypt(word):
  second_step = 1
  decrypt_word = ""

  for index in range(len(word)):
    new_letter_ascii = ord(word[index])
    new_letter_ascii -= second_step

    while new_letter_ascii < ord('a'):
      new_letter_ascii += 26

    decrypt_word += chr(new_letter_ascii)
    second_step += new_letter_ascii

  return decrypt_word
 