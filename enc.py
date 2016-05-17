#Russell Anderson
#lab 8
#To use Pythons dictionaries and file I/O to experiment with basic encryption. For our purposes, we will use a simple substitution cipher
#Resources used: http://thelivingpearl.com/2013/06/03/caesar-ciphers-in-python/

#!/bin/usr/python

import string, random, sys, os.path
from sys import argv #import argv module from sys
from random import shuffle #import shuffle module from random library

#if args provided is not equal to exactly 2...
if len(sys.argv)!=2:
	sys.exit("WARNING: YOU MUST  provide exactly 2 arguments on the command line, ex: python (1)enc.py (2)file.txt")

#if the file exists...
if(os.path.isfile(sys.argv[1])):
	file = sys.argv[1]
	encryptFile = "encrypted_" + file #append to encrypted file
else:
	sys.exit("Warning: NOT A KNOWN FILE!") #not a file in directory

#open and read file contents 
f = open(file, 'r')
#new var to hold contents of read file
fInput = f.read()
f.close()

#define list of alphabet
alphaKey = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#var to return random ints to represent alphabet
cipherKey = random.randint(1,25)

#define function to encrypt file
def cipher(fInput, cipherKey):
	#call method to shuffle alphabet
	shuffle(alphaKey)

#blank dictionary to hold cipher
dic={}
for i in range(0,len(alphaKey)):
	dic[alphaKey[i]]=alphaKey[(i+cipherKey)%len(alphaKey)]

#test: zip reverses dic keys and values
#key = dict(zip(dic.values(),dic.keys()))
#print "The subsitution cipher is: \n",(key)

#new file to hold encrypted contents
newFile = ""
for i in fInput.lower(): #convert chars to lower
	if i in dic:
		 i=dic[i] 
	newFile+=i 

#open and write encrypted contents to new file
fileNew = open(encryptFile, 'w')
fileNew.write(str(cipher(fInput, cipherKey))) #typecast cipher func to string
fileNew.close()

#main
print "\n\t*****Substitution Cipher Program*****\n"
print "\n\tEncrypted contents of file: ",newFile
print "\n\tEncrypted file name: ",encryptFile
print "\n\tDecrypted file contents: ",fInput
print "\n\tDecrypted file name: ",file

