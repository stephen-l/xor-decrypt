from collections import Counter
import sys

def rotate(string, n): # rotate the key
    return string[n:] + string[:n]

def xor(data, key): # xor each byte while looping through key
    l = len(key)

    decoded = ''
    for i in range(0, len(data)):
        decoded += chr(ord(data[i]) ^ ord(key[i % l]))
    return decoded

def repeats(string): # if the string repeats, remove repetition
    for x in range(1, len(string)):
        substring = string[:x]

        if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
            return substring

with open(sys.argv[1], 'r') as file: # read encrypted file
    s = file.read()

n = 40 # length of key
substr = Counter(s[i: i+n] for i in range(len(s) - n))
key, count = substr.most_common(1)[0]
print(' [+] 40 char common string: %r' % (key))
print(' [+] Finding substring')

key = repeats(key) # remove repetition
n = len(key)

if n != 32:
    print(' [+] New key')

print(' [+] Rotating key')
print(' [+] Looking for MZ')

for i in key: # rotate the key until "MZ\x90" is found
    key = rotate(key,1)
    if 'M' == chr(ord(s[0]) ^ ord(key[0])) and 'Z' == chr(ord(s[1]) ^ ord(key[1])) and '\x90' == chr(ord(s[2]) ^ ord(key[2])):
            print(' [+] MZ\x90 header found')
            print(' [+] Key = %r' % key)
            break

if not len(sys.argv) == 3: # quick cli args
    print('Usage: %s encryptedfile outputfile' % sys.argv[0])
else:
    with open(sys.argv[1], 'r') as myfile:
        data=myfile.read()
    print(' [+] Writing executable')
    fo = open(sys.argv[2], 'wb')
    fo.write(xor(data,key)) # write the new file to disk
    fo.close()
