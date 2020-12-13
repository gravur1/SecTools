#!/usr/bin/python
import sys
import email
import imaplib

if len(sys.argv) !=5:
	print "Usage: "+sys.argv[0]+" user password servername port"
	sys.exit(0)


username = sys.argv[1]
password = sys.argv[2]
server = sys.argv[3]
serverport = sys.argv[4]


mail = imaplib.IMAP4(server, serverport)
mail.login(username,password)

rp, lista=mail.list()

if rp != 'OK':
	print "No inbox(es) identified"
	sys.exit(0)

print("Inboxes and respective emails:\n")
for linha in lista:
	inbox=(linha.split(" "))[2].strip("\"")
	mail.select(inbox)	
	if inbox != '.':			
		print(inbox)
		rp2, data = mail.search(None, "ALL")
		if data != [b'']:
			#print("Imprimindo emails:\n")
			for emailLinha in data[0].split(" "):
				rp3, email = mail.fetch(emailLinha, '(RFC822)')
				print(email)
				print("")
