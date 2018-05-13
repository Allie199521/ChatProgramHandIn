#Server
import Elgamal
from Crypto.Cipher import AES
import socket
from os import system 
import platform, random

host = socket.gethostname()

#Random port number
port = 12345

#this is the socket
s = socket.socket()

#binds address and port
s.bind((host, port))

#listens in up to 2 connections at a time
s.listen(2)

#Accepts connection to the server
conn, addr = s.accept()

#Creates keys to be sent to Client once connected
p,a,g,ga = Elgamal.generateKey(128)

#places keys into a string format seperated by commas
publickeys = str(p) + "," + str(g) + "," + str(ga)

#sends keys to client
conn.send(publickeys.encode())

#collecting public key from client
gb = conn.recv(1024).decode()

#calculate gab
gab = pow(int(gb), a, p)

#printing the key for the presentation
print("Key: " + str(gab))

#turn key to string
key = gab.to_bytes(32, 'little')

#set IV
IV = 16 * '\x00'

#set mode
mode = AES.MODE_CBC

#set encrypt to new AES
encryption = AES.new(key, mode, IV=IV)

#decryption set to the AES
decryption = AES.new(key, mode, IV=IV)

#Prints out the address of who just got connected
print("Connection from: " + str(addr))

#loop til break
while 1:

    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = decryption.decrypt(conn.recv(1024)).strip().decode()

    #If no data is recieved, break
    if not data:
        break

    #Print what the client has sent
    print("client: " + str(data))

    #message to send to client
    data = input("You: ")

    #break upon character
    if '~' in data:
        break

    #make sure to make message of length%16 == 0
    l = len(data)
    if l%16 != 0:
        data = data + ' '*(16-l%16)
    data = encryption.encrypt(data)
    print(str(data))
    #send the data to the client in bytes
    conn.send(data)

#closes connection
conn.close()

#get the current platform
pf = platform.system()

#check to see which command to run to clear
if(pf == 'Linux' or pf == 'Darwin'):
	system('clear')
else:
	system('cls')
