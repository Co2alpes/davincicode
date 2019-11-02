import hashlib
import socket
import subprocess
import sys
from datetime import datetime
import errno
import random
import mechanize

print(" ___________                                                __     ")
print(" \_   _____/___________    _____   ______  _  _____________|  | __ ")
print("  |    __) \_  __ \__  \  /     \_/ __ \ \/ \/ /  _ \_  __ \  |/ / ")
print("  |     \   |  | \// __ \|  Y Y  \  ___/\     (  <_> )  | \/    <  ")
print("  \___  /   |__|  (____  /__|_|  /\___  >\/\_/ \____/|__|  |__|_ \ ")
print("      \/               \/      \/     \/                        \/ ")


print(" [1] BRUTEforce sha224 ")
print(" [2] Port scanner ")
print(" [3] DOS ")

choice = int(raw_input=(" => ")

if choice == 1:
  while  True:
    try:
        wordlist_user=raw_input('entrez votre wordlist : ')
        wordlist=open(wordlist_user,'r')
        hash=raw_input('entrez votre hash sha224: ')
        
          break
    execpt:
        print('pas de fichier portant ce nom !! \n')
      
    for world in wordlist.readlines():
    word=word.strip('\n')
    wordlist_hash=hashlib.sha224(word).hexdigest()
    
    if(hash==wordlist_hash):
        print('password FOUND ====>' +word)
        break
    else:
        print('password NOt found !!')
        
        
if choice ==1:        
    
