README.txt
Sherilyn Tejada-Martinez and Alexandra Miranda
Intro to Cryptography
AES/DES Chatprogram

Dependancies:
	- pycrypto - external python module
	- random - built in
	- fractions - built in
	- math - built in
	- sympy - external python module
	- os - built in
	- platform - built in

This was coded mostly in python 3.5.2

To run: two separate terminals must be available
	- in the first:
		$ python3 Server.py
		#this will wait for a client to connect - second terminal
	- in the second:
		$ python3 Client.py
		#this will connect, print out the given elgamal keys and wait for input.

To remove the printed keys:
	- in Server.py comment out line 41
	- in Client.py comment out line 38

To remove the printed out encrypted text:
	- in Server.py comment out line 86