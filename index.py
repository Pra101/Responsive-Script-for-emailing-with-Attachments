import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from string import Template
import pandas as pd

e = pd.read_csv("test5.csv")
#e = pd.read_excel("Contacts.xlsx")

# port for nsut.ac.in may differ
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    server.starttls()
except:
    print 'Something went wrong...'

# to be logined from Official login account
#change the password before sending
server.login('emailsample@gmail.com','password')

body = ("\n\nwe are pleased to inform you that you have qualified for Certification from NSS NSUT CELL for XYZ event\n\n")

subject = "Send emails with attachment"
fromaddr='prahaladsingh271200@mail.com'

#Emails,PDF
for index, row in e.iterrows():
    print ('Sending:  '+row["EMAIL"])
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = subject
    #NAME,EMAIL,ORGANISATION,MESSAGE,CRET_ID
    #msg.attach(MIMEText(body+"""\n"""+row['ORGANISATION']+"""\n"""+row['MESSAGE']+"""\nYOUR ID = """+row['CRET_ID']+"""\nThank You""", 'plain'))
    msg.attach(MIMEText("Hi "+row['NAME']+ body+"\nfrom "+row['ORGANISATION']+"\n"+row['MESSAGE']+"\nThank you", 'plain'))
    #filename = row["CERT_ID"]
    toaddr = row["EMAIL"]

    attachment = open(row["CRET_ID"], "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % row['CRET_ID'])
    msg.attach(part)
    text = msg.as_string()
    
    server.sendmail(fromaddr, toaddr, text)
    #server.sendmail('sender_email',emails,body)

print("Emails sent successfully")
server.quit()
