import hashlib
import sys


arquivo = open(sys.argv[2],"r") #third parameter is the path of the wordlist 

for key in arquivo:
	key = key.strip() #remove all the garbage in string, such as "\n"
	
	encrypted_word = hashlib.md5(key.encode()) #encode the word in the wordlist

	if encrypted_word.hexdigest() == sys.argv[1]: #check if the generated encrypted word is the same of the given hash 
		print("The hash " + str(encrypted_word.hexdigest()) + " has de key: " + key)
		exit()
	else:
		print(encrypted_word.hexdigest() + " / " + key)
		
print("Key not found!")




#file not found error
#unsuported hash type



