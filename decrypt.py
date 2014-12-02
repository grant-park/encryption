import random
import string

def main():
	ciphername = input('Name of ciphertext file? ')
	decryptname = input('Name of file you want the decrypted message in? ')
	key = int(input('key? '))
	l = makeMap(key)
	ciphertext = readToString(ciphername)
	v = decrypt(ciphertext,l,key)
	writeString(decryptname, v)

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

def decrypt(msg,d,key):
	encmap = invert(makeMap(key))
	encmsg = ''
	for i in msg:
		encmsg += encmap[i]
	return encmsg

def invert(encmap):
    result = {}
    for i,value in encmap.items():
        result[value] = i
    return result


main()
    
