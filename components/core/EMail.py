import smtplib

username = 'bassa.ucsc@gmail.com'
password = 'bassa.123'

def send_mail(toaddrs, msg):
    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login(username,password)
    server.sendmail('bassa.ucsc@gmail.com', toaddrs, msg)
    server.quit()