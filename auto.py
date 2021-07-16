import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from string import Template
import pandas as pd

e = pd.read_csv("test.csv")
#e = pd.read_excel("Contacts.xlsx")

# port for nsut may d
server = smtplib.SMTP(host='smtp.gmail.com', port=465)
server.starttls()
server.login("sample@gmail.com",'password')
body = ("""
Hi there

Test message

Thankyou
""")
subject = "Send emails with attachment"
fromaddr='prahaladsingh271200@mail.com'
#body = "Subject: {}\n\n{}".format(subject,msg)
#Emails,PDF
for index, row in e.iterrows():
    print (row["Emails"]+row["PDF"])
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    filename = row["PDF"]
    toaddr = row["Emails"]
    attachment = open(row["PDF"], "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    #server.sendmail('sender_email',emails,body)

print("Emails sent successfully")

server.quit()
