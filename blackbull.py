import hashlib 
import sys


def initial():
	try: ##trying to open the file!
		arquivo = open(sys.argv[2],"r")

	except FileNotFoundError:
		print("The requsted wordlist was not found!")
		exit()

	breakit(arquivo)


	
def breakit(arquivo):	
	
	for key in arquivo: ## if the wordlist exist then clean them
		key = key.strip()
	
		encrypted_word = hashlib.md5(key.encode())
		
		if encrypted_word.hexdigest() == sys.argv[1]:
			print("The hash " + str(encrypted_word.hexdigest()) + " has the key " + key)
			exit()
			
		else:
			print(encrypted_word.hexdigest() + " / " + key)
	
		
	print("Key not found, or the provided hash is not MD5 readable")




if __name__ == "__main__":
	initial()


