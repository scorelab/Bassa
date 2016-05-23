import smtplib
from ConfReader import conf_reader

conf = conf_reader("email.conf")

def send_mail(toaddrs, msg):
    conf_reader()
    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login(conf['username'],conf['password'])
    server.sendmail(conf['username'], toaddrs, msg)
    server.quit()
