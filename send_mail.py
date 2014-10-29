import smtplib
from email.mime.text import MIMEText

me = "admin@sherbakov.corbina.net"
you = "ashcherbakov@beeline.ru"

login = "user"
password = "12345"


def send(login,password):
	mesg = "login: %s\npass: %s\n" % (login, password)
	msg = MIMEText(mesg)
	
	msg['Subject'] = 'Authentication data for FTTB devices'  
	msg['From'] = me
	msg['To'] = you

	#print msg
	s = smtplib.SMTP('localhost')
	s.sendmail(me, [you], msg.as_string())
	s.quit()

send(login,password)
