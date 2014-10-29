import smtplib

from email.mime.text import MIMEText

me = "admin@sherbakov.corbina.net"
you = "ashcherbakov@beeline.ru"

fp = open("text","r")
msg = MIMEText(fp.read())
fp.close()

msg['Subject'] = 'The contents of'  
msg['From'] = me
msg['To'] = you

#print msg
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
