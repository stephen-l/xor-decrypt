import sys

def xor(data, key):
	l = len(key)
	decoded = ""
	for i in range(0, len(data)):
		decoded += chr(ord(data[i]) ^ ord(key[i % l]))
	return decoded
  
if not len(sys.argv) == 4:
	print "Usage: %s file key outputfile" % sys.argv[0]
else:
	with open(sys.argv[1], 'r') as myfile:
		data=myfile.read()
	key = sys.argv[2]
	fo = open(sys.argv[3], "wb")
	fo.write(xor(data,key))
	fo.close()
