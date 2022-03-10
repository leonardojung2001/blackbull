import hashlib
import sys


arquivo = open(sys.argv[2],"r")

for key in arquivo:
	key = key.strip()
	
	encrypted_word = hashlib.md5(key.encode())

	if encrypted_word.hexdigest() == sys.argv[1]:
		print("o hash " + str(encrypted_word.hexdigest()) + " tem a chave " + key)
		exit()
	else:
		print(encrypted_word.hexdigest() + " / " + key)
		
print("Chave não encontrada!")








