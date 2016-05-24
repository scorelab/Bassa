import smtplib
from ConfReader import get_conf_reader

conf = get_conf_reader("email.conf")

def send_mail(toaddrs, msg):
    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login(conf['username'],conf['password'])
    server.sendmail(conf['username'], toaddrs, msg)
    server.quit()
