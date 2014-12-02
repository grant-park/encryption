import random
import string

def main():
	clearname = input('Name of cleartext file? ')
	ciphername = input('Name of ciphertext file? ')
	key = int(input('key? '))
	cleartext = readToString(clearname)
	ciphertext = encrypt(cleartext,key)
	writeString(ciphername, ciphertext)

def readToString(m):
	f = open(m)
	data = f.read()
	return data

def writeString(filename,msg):
	f = open(filename,'w')
	f.write(msg)
	f.close()

def encrypt(msg,key):
	encmap = makeMap(key)
	encmsg = ''
	for i in msg:
		encmsg += encmap[i]
	return encmsg

def makeMap(key):
	random.seed(key)
	m = list(string.printable)
	l = list(string.printable)
	random.shuffle(l)
	d = {m[i]: l[i] for i in range(len(m))}
	return d

main()
    
