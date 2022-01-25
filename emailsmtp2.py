import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'University Admission'
msg['From'] = 'The coding Team of Salam'
msg['To'] = 'mathcoder1995@gmail.com'


with open('email.txt') as myfile:
    data = myfile.read()
    msg.set_content(data)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('abdulsalamyussif.asy@gmail.com', '0208022754')
        server.send_message(msg)
        print('Email sent!')
except:
    print('Error, massage not sent!')