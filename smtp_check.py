import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
#server = smtplib.SMTP(host='smtp.gmail.com', port=465)
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    server.starttls()
except:
    print 'Something went wrong...'
server.login('emailsample@gmail.com','password')

#server.starttls()
server.lo
body = ("""HI This is just to check whether my email system works or not""")
Subject=("""Just to check whether my emailing system works or not""")

fromaddr='prahaladsingh271200@hgmaild.com'
toaddr='bhavdhi@gmail.com'
msg = MIMEMultipart()
msg['From']=fromaddr
msg['Subject']=Subject
msg.attach(MIMEText(body))
text=msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()