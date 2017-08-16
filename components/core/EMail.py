import smtplib
from ConfReader import get_conf_reader

conf = get_conf_reader("dl.conf")

def send_mail(toaddrs, msg):
    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login(conf['email']['username'],conf['email']['password'])
    server.sendmail(conf['email']['username'], toaddrs, msg)
    server.quit()
