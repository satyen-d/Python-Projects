# Email Sending Application
from smtplib import*

#Reciver's Mail ID
to = input("Enter recipant Email ID:\n")

#Email Body
content = input("Enter Content:\n")

#Email Function
def SendMail(to, content):
    #SMTP Protocol
    server = SMTP("smtp.gmail.com", 587)
    #Initialising SMTP Protocol
    server.ehlo()
    #Starting Server
    server.starttls()
    #Gmail Details
    server.login("pythontest1281@gmail.com", "python12#")
    #Send Mail Details
    server.sendmail("pythontest1281@gmail.com", to, content)
    #END
    server.close

#Function Call
SendMail(to, content)
