#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText

me = "admin@sherbakov.corbina.net"
#you = "ashcherbakov@beeline.ru"
#
#login = "user"
#password = "12345"


with open("users","r") as f:
	users = f.readlines()

#remove whitespace/newline symbols
for i in range(len(users)):
	users[i] = users[i].rstrip()

def send(login,password,mail):
	mesg = "login: %s\npass: %s\n" % (login, password)
	msg = MIMEText(mesg)
	
	msg['Subject'] = 'Authentication data for FTTB devices'  
	msg['From'] = me
	msg['To'] = mail

	#print msg
	print "sending message to %s" % mail
	s = smtplib.SMTP('localhost')
	s.sendmail(me, [mail], msg.as_string())
	s.quit()

for user in users:
	data = user.split(":")
	mail = data[0]
	password = data[1]
	data = mail.split("@")
	login = data[0]
	send(login,password,mail)
