import os


def encrypt_text(string):
  d_set = []
  hash_ = ''
  user_cookie = open('cookie.txt','r')
  cookie = user_cookie.read().strip().split('\n')
  alphabet = "abcdefghijklmnopqrstuvwxyz 1234567890?.,'!"
  new_hash = []
  
  for i in range(len(alphabet)):
    d_set.append(cookie[i])
  
  for alph_num in string:
    new_hash.append(d_set[alphabet.index(alph_num)])
  
  return(''.join(new_hash))

def decrypt_text(hash):
  d_set = []
  user_cookie = open('cookie.txt','r')
  cookie = user_cookie.read().strip().split('\n')
  alphabet = "abcdefghijklmnopqrstuvwxyz 1234567890?.,'!"
  new_hash = []
    
  for i in cookie:
    d_set.append(i)
  
  for Str in hash:
    new_hash.append(alphabet[d_set.index(Str)])
    
  return(''.join(new_hash))  

  
while True:
  print('Choose Mode:\n\nType E to encrypt text\nType T to decode encryption')
  mode = input(">>").lower()
  
  if mode == 'e':
    os.system('cls')
    new_string =  input('<Text to encrypt>').lower()
    os.system('cls')
    print("Generated Hash: "+encrypt_text(new_string)+"(CTRL+C)\n \n \n \n")
    
  elif mode == 't':
    os.system('cls')
    new_string =  input('<Hash to decrypt>').lower()
    print("Decrypted Hash: "+decrypt_text(new_string)+"(CTRL+C)\n \n \n \n")
  
  
  else:
    os.system('cls')
