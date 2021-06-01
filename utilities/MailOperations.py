# Send emails   |   packages : smtplib, json
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#Email Parameters
# To = "ab@gmail.com"     # For multiple emails ['bb@gmail.com','cc@gmail.com']
# Subject = "Subject"
# Body = "Email Body\n"
# SendMail(To,Subject,Body)


global key, user

def SendMail(Subject,Body,To="botnotifier007@gmail.com"):
    #Fetch Credentials 
    with open('JSON/cred.json') as cred_file:
        data = json.load(cred_file)
        user = data["credentials"]["gmail"]["user"]
        key = data["credentials"]["gmail"]["key"]    

    Message = 'Subject: {}\n\n{}'.format("MailBot : " + Subject, "Hi Saurabh, \n \n " + Body + " \n \n \n \n -Email Bot")

    try:
        message = MIMEMultipart()
        message.attach(MIMEText(Body, "html"))
        message['Subject'] = Subject
        msgBody = message.as_string()
        server = smtplib.SMTP_SSL('smtp.gmail.com',465) # for unsecure connection port : 587
        server.ehlo()
        # server.starttls()  upgrading the connection to secure by starting TLS if the connection is in secure
        server.login(user,key)
        server.sendmail(str(user),To,msgBody)
        print("Email has been sent")
    except:
        print("Failed to Send Message")
    finally:
        server.quit
