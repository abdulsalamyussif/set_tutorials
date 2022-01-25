import smtplib

from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'Traniing Invitation'
msg['From'] = 'Salam Training'
msg['To'] = 'mathcoder1995@gmail.com'

msg.set_content('Test Email from Salam Team')
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('abdulsalamyussif.asy@gmail.com', '0208022754')
    server.send_message(msg)
    server.quit()
except:
    print('Error, massage not sent!')