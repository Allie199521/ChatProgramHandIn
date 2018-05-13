#aes project for crypto
#allie and sherilyn

#Client
import socket
from os import system
import platform
import random
import Elgamal
from Crypto.Cipher import AES

#get the host name
host = socket.gethostname()

#Random port number
port = 12345

#here is the socket, bro
c = socket.socket()

#Connects to the server
c.connect((host, port))

#recieves public keys from Server
keys = c.recv(1024).decode()

#splits the keys and places them into an array
pubkey = keys.split(",")

#Generate private key b with desired bit length
b = random.randint(1,128)
gb = pow(int(pubkey[1]),b) % int(pubkey[0])

#full mask sending to decrypt
gab = pow(int(pubkey[2]), b)%int(pubkey[0])

#for the presentation
print("Key: " + str(gab))

#sending the public key of client to server
c.send(str(gb).encode())

#make aes key
key = gab.to_bytes(32, 'little')

#set IV
IV = 16 * '\x00'

#set mode
mode = AES.MODE_CBC

#set encrypt
encryption = AES.new(key, mode, IV=IV)

#decrypt for AES
decryption = AES.new(key, mode, IV=IV)

#run til break
while 1:

    #Prompts client again for input and assign message to the new input
    message = input("You: ")

    #breaks on certain string
    if '~' in message:
        break

    #find the length of the message
    l = len(message)

    #make sure that the message is evenly divisibl by 16
    if l%16 != 0:
        message = message + ' '*(16-l%16)

    #encrypt
    message = encryption.encrypt(message)

    #Change message into byte size and send to server
    c.send(message)

    #collects the servers message and change it to a string
    data = decryption.decrypt(c.recv(1024)).strip().decode()

    #close server if no data was received
    if not data:
        break

    #Print on the terminal what the server has sent
    print("server: " + str(data))

#closes client connection
c.close()
pf = platform.system()

#check OS for clear instruction
if(pf == 'Linux' or pf == 'Darwin'):
	system('clear')
else:
	system('cls')
